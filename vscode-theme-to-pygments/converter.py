#!/usr/bin/env python3
"""
vscode_theme_to_pygments.py

Convert a VS Code color theme JSON file (TextMate `tokenColors`) into a
Pygments `Style` subclass, in the style of:
https://github.com/lepture/pygments-styles

Usage:
    python vscode_theme_to_pygments.py THEME.json -o my_style.py
    python vscode_theme_to_pygments.py https://.../theme.json -o my_style.py

    # print to stdout instead of writing a file
    python vscode_theme_to_pygments.py THEME.json

Notes:
- VS Code theme files are JSONC (JSON with // and /* */ comments and
  sometimes trailing commas). Those are stripped before parsing.
- VS Code/TextMate scopes don't map 1:1 onto Pygments token types, so this
  script uses a best-effort table of "for this Pygments token, look for one
  of these TextMate scopes" and picks the most specific match available in
  the theme. Always eyeball the result and tweak `SCOPE_CANDIDATES` below
  (or the generated .py file) for languages you care about.
- Some VS Code theme files (like AposTheme's "-base" variant) intentionally
  omit editor.background/editor.foreground because they're merged with a
  second "variant" file. If those keys are missing, sensible fallbacks are
  used and a warning is printed -- pass --background/--foreground to
  override, or fetch/merge the variant file yourself before conversion.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from dataclasses import dataclass, field


# --------------------------------------------------------------------------
# 1. Fetching / loading + JSONC stripping
# --------------------------------------------------------------------------

def load_text(source: str) -> str:
    """Load raw text from a URL or a local file path."""
    if re.match(r"^https?://", source):
        with urllib.request.urlopen(source) as resp:  # nosec - user-provided URL
            return resp.read().decode("utf-8")
    with open(source, "r", encoding="utf-8") as f:
        return f.read()


def strip_jsonc(text: str) -> str:
    """
    Strip // line comments and /* */ block comments from JSONC, without
    touching // or /* that appear inside JSON string literals. Also removes
    trailing commas before ] or }, which VS Code theme files sometimes have.
    """
    out = []
    i, n = 0, len(text)
    in_string = False
    escape = False
    while i < n:
        c = text[i]
        if in_string:
            out.append(c)
            if escape:
                escape = False
            elif c == "\\":
                escape = True
            elif c == '"':
                in_string = False
            i += 1
            continue

        if c == '"':
            in_string = True
            out.append(c)
            i += 1
            continue

        if c == "/" and i + 1 < n and text[i + 1] == "/":
            while i < n and text[i] not in "\r\n":
                i += 1
            continue

        if c == "/" and i + 1 < n and text[i + 1] == "*":
            i += 2
            while i + 1 < n and not (text[i] == "*" and text[i + 1] == "/"):
                i += 1
            i += 2
            continue

        out.append(c)
        i += 1

    stripped = "".join(out)
    # Remove trailing commas: ", }" or ", ]"
    stripped = re.sub(r",(\s*[}\]])", r"\1", stripped)
    return stripped


def load_theme(source: str) -> dict:
    raw = load_text(source)
    cleaned = strip_jsonc(raw)
    return json.loads(cleaned)


# --------------------------------------------------------------------------
# 2. Flattening tokenColors into scope -> settings
# --------------------------------------------------------------------------

@dataclass
class ScopeRule:
    scope: str
    foreground: str | None
    font_style: str | None
    order: int  # position in the original tokenColors list
    compound: bool  # True if the original selector was "outer inner" (context-dependent)


def flatten_token_colors(theme: dict) -> list[ScopeRule]:
    rules: list[ScopeRule] = []
    for order, entry in enumerate(theme.get("tokenColors", [])):
        settings = entry.get("settings", {}) or {}
        fg = settings.get("foreground")
        font_style = settings.get("fontStyle")
        scopes = entry.get("scope", [])
        if isinstance(scopes, str):
            # VS Code allows a comma-separated string here too.
            scopes = [s.strip() for s in scopes.split(",") if s.strip()]
        for raw_scope in scopes:
            raw_scope = raw_scope.strip()
            if not raw_scope:
                continue
            # A rule scope can itself be space-separated ("meta.foo entity.bar"),
            # meaning "entity.bar nested inside meta.foo" (only when an
            # ancestor "meta.foo" is also present). We match against the last
            # (innermost) component, but flag it as "compound" so it's only
            # used as a last resort against a plain, unconditional rule for
            # the same scope -- otherwise a narrow, context-dependent rule
            # (e.g. "meta.object-literal.key string") could hijack a generic
            # token (e.g. plain "string").
            parts = raw_scope.split(" ")
            innermost = parts[-1]
            compound = len(parts) > 1
            if not innermost:
                continue
            rules.append(ScopeRule(innermost, fg, font_style, order, compound))
    return rules


def classify(theme_scope: str, candidate: str) -> tuple[str, int] | None:
    """Classify how a theme rule's scope relates to a requested candidate
    scope. Returns (kind, specificity) or None if it doesn't apply at all.
    "specificity" is defined so that a larger value is always preferred
    within its kind."""
    if theme_scope == candidate:
        return ("exact", 0)
    if candidate.startswith(theme_scope + "."):
        # theme_scope is a broader ancestor of what we asked for -- prefer
        # the closest (longest) ancestor available.
        return ("parent", len(theme_scope))
    if theme_scope.startswith(candidate + "."):
        # theme_scope is a narrower, more specific descendant of what we
        # asked for -- prefer the one closest to the generic candidate
        # (shortest), since a wildly specific descendant is a poor stand-in
        # for a generic Pygments token.
        return ("child", -len(theme_scope))
    return None


_KIND_RANK = {"exact": 2, "parent": 1, "child": 0}


def find_best_rule(rules: list[ScopeRule], candidates: list[str]) -> ScopeRule | None:
    """Search all candidate scopes (most desirable first) against all theme
    rules, and pick the single best match using, in priority order:
      1. match kind: exact > ancestor ("parent") > descendant ("child")
      2. plain (context-free) rules over compound/context-dependent ones
      3. specificity within the kind (closest ancestor / least-specific descendant)
      4. earlier candidate in our requested list
      5. later position in the theme's tokenColors array (VS Code semantics:
         later rules win on equal specificity)
    """
    best_key = None
    best_rule = None
    for ci, candidate in enumerate(candidates):
        for rule in rules:
            cls = classify(rule.scope, candidate)
            if cls is None:
                continue
            kind, spec = cls
            key = (_KIND_RANK[kind], 0 if rule.compound else 1, spec, -ci, rule.order)
            if best_key is None or key > best_key:
                best_key = key
                best_rule = rule
    return best_rule


# --------------------------------------------------------------------------
# 3. Pygments token -> candidate TextMate scopes
# --------------------------------------------------------------------------
# Ordered dict: for each Pygments token, a list of TextMate scopes to try,
# most-specific/most-desirable first. Feel free to extend/edit this table.

SCOPE_CANDIDATES: list[tuple[str, list[str]]] = [
    # -- Comments --
    ("Comment.Preproc", ["keyword.control.directive", "meta.preprocessor"]),
    ("Comment.Special", ["keyword.other.todo", "keyword.codetag.notation"]),
    ("Comment.Doc", ["keyword.other.documentation", "storage.type.class.jsdoc"]),
    ("Comment", ["comment.line", "comment.block", "comment"]),

    # -- Keywords --
    ("Keyword.Namespace", ["keyword.control.import", "entity.name.namespace"]),
    ("Keyword.Declaration", ["storage.type.class", "storage.type.function", "storage.modifier"]),
    ("Keyword.Constant", ["constant.language"]),
    ("Keyword.Type", ["support.type", "storage.type"]),
    ("Keyword.Reserved", ["keyword.control"]),
    ("Keyword", ["keyword.control", "keyword"]),

    # -- Names --
    ("Name.Namespace", ["entity.name.namespace", "support.module", "support.node"]),
    ("Name.Class", ["entity.name.type.class"]),
    ("Name.Exception", ["support.type.exception", "support.class.exception"]),
    ("Name.Function.Magic", ["support.function.magic"]),
    ("Name.Function", ["entity.name.function", "support.function"]),
    ("Name.Decorator", ["entity.name.function.decorator", "punctuation.decorator", "storage.type.annotation"]),
    ("Name.Attribute", ["entity.other.attribute-name"]),
    ("Name.Tag", ["entity.name.tag"]),
    ("Name.Builtin.Pseudo", ["variable.language.special.self", "variable.language.this"]),
    ("Name.Builtin", ["support.function.builtin", "support.type.object"]),
    ("Name.Variable.Instance", ["variable.object.property"]),
    ("Name.Variable.Global", ["variable.other.global"]),
    ("Name.Variable.Class", ["variable.other.class"]),
    ("Name.Variable", ["variable.other", "variable"]),
    ("Name.Constant", ["variable.other.constant", "support.constant"]),
    ("Name.Label", ["entity.name.label"]),
    ("Name.Property", ["support.type.property-name", "variable.object.property"]),
    ("Name.Entity", ["constant.character.escape", "punctuation.definition.entity"]),

    # -- Numbers --
    ("Number", ["constant.numeric"]),

    # -- Operators --
    ("Operator.Word", ["keyword.operator.word"]),
    ("Operator", ["keyword.operator"]),

    # -- Punctuation --
    ("Punctuation", ["punctuation"]),

    # -- Strings --
    ("String.Doc", ["string.quoted.docstring"]),
    ("String.Escape", ["constant.character.escape"]),
    ("String.Regex", ["string.regexp"]),
    ("String.Symbol", ["constant.other.symbol"]),
    ("String", ["string.quoted", "string"]),

    # -- Generic / markup (diffs, markdown) --
    ("Generic.Heading", ["markup.heading"]),
    ("Generic.Subheading", ["markup.heading.setext"]),
    ("Generic.Emph", ["markup.italic"]),
    ("Generic.Strong", ["markup.bold"]),
    ("Generic.Deleted", ["markup.deleted"]),
    ("Generic.Inserted", ["markup.inserted"]),
    ("Generic.Error", ["invalid.illegal"]),
    ("Generic.Traceback", ["markup.error"]),

    # -- Errors --
    ("Error", ["invalid.illegal", "invalid"]),
]


# --------------------------------------------------------------------------
# 4. fontStyle -> pygments style-string fragments
# --------------------------------------------------------------------------

def font_style_to_pygments(font_style: str | None) -> list[str]:
    if not font_style:
        return []
    parts = [p.strip() for p in font_style.split(" ") if p.strip()]
    out = []
    for p in parts:
        if p in ("bold", "italic", "underline"):
            out.append(p)
        # Pygments has no "strikethrough" -- drop it silently (noted in a
        # comment in the generated file instead of failing).
    return out


# --------------------------------------------------------------------------
# 5. Building the style dict
# --------------------------------------------------------------------------

@dataclass
class TokenStyle:
    color: str | None
    style_words: list[str] = field(default_factory=list)


def build_token_styles(rules: list[ScopeRule]) -> "dict[str, TokenStyle]":
    result: dict[str, TokenStyle] = {}
    for token_name, candidates in SCOPE_CANDIDATES:
        best = find_best_rule(rules, candidates)
        if best is None or not (best.foreground or best.font_style):
            continue
        result[token_name] = TokenStyle(
            color=best.foreground,
            style_words=font_style_to_pygments(best.font_style),
        )
    return result


# --------------------------------------------------------------------------
# 6. Editor-level colors (background / highlight / line numbers / default text)
# --------------------------------------------------------------------------

def get_editor_colors(theme: dict, cli_bg: str | None, cli_fg: str | None) -> dict:
    colors = theme.get("colors", {}) or {}

    background = cli_bg or colors.get("editor.background")
    foreground = cli_fg or colors.get("editor.foreground") or theme.get("colors", {}).get("foreground")
    line_number = colors.get("editorLineNumber.foreground")
    highlight = (
        colors.get("editor.lineHighlightBackground")
        or colors.get("editor.selectionBackground")
        or colors.get("selection.background")
    )

    warnings = []
    if not background:
        background = "#1e1e1e"
        warnings.append(
            "no 'editor.background' found in theme colors -- defaulted to "
            f"{background!r}. This theme file may be a 'base' variant meant "
            "to be merged with another file that supplies surface colors; "
            "pass --background to set it explicitly."
        )
    if not foreground:
        foreground = "#d4d4d4"
        warnings.append(
            "no 'editor.foreground'/'foreground' found in theme colors -- "
            f"defaulted to {foreground!r}. Pass --foreground to override."
        )
    if not highlight:
        highlight = background

    return {
        "background_color": background,
        "foreground": foreground,
        "line_number_color": line_number,
        "highlight_color": highlight,
        "warnings": warnings,
    }


# --------------------------------------------------------------------------
# 7. Code generation
# --------------------------------------------------------------------------

def pascal_case(name: str) -> str:
    words = re.split(r"[^A-Za-z0-9]+", name)
    return "".join(w[:1].upper() + w[1:] for w in words if w)


def slugify(name: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-").lower()
    return slug or "custom-theme"


def render_value(color: str | None, style_words: list[str]) -> str:
    parts = list(style_words)
    if color:
        parts.append(color if color.startswith("#") else f"#{color}")
    return " ".join(parts)


TOKEN_GROUP_ORDER = [
    "Text",
    "Error",
    "Comment", "Comment.Preproc", "Comment.Special", "Comment.Doc",
    "Keyword", "Keyword.Namespace", "Keyword.Declaration", "Keyword.Constant",
    "Keyword.Type", "Keyword.Reserved",
    "Operator", "Operator.Word",
    "Punctuation",
    "Name", "Name.Namespace", "Name.Class", "Name.Exception",
    "Name.Function", "Name.Function.Magic", "Name.Decorator", "Name.Attribute",
    "Name.Tag", "Name.Builtin", "Name.Builtin.Pseudo",
    "Name.Variable", "Name.Variable.Instance", "Name.Variable.Global",
    "Name.Variable.Class", "Name.Constant", "Name.Label", "Name.Property",
    "Name.Entity",
    "Number",
    "String", "String.Doc", "String.Escape", "String.Regex", "String.Symbol",
    "Generic", "Generic.Heading", "Generic.Subheading", "Generic.Emph",
    "Generic.Strong", "Generic.Deleted", "Generic.Inserted", "Generic.Error",
    "Generic.Traceback",
]


def generate_module(theme: dict, token_styles: "dict[str, TokenStyle]", editor: dict) -> str:
    theme_name = theme.get("name", "CustomTheme")
    class_name = pascal_case(theme_name) + "Style"
    style_name = slugify(theme_name)
    alias = theme_name

    used_tokens = [t for t in TOKEN_GROUP_ORDER if t in token_styles]
    # include any tokens matched that weren't in our display-order list
    used_tokens += [t for t in token_styles if t not in used_tokens]

    top_level_needed = sorted({t.split(".")[0] for t in used_tokens} | {"Text", "Error"})

    lines = []
    lines.append("from pygments.style import Style")
    lines.append("from pygments.token import (")
    for t in top_level_needed:
        lines.append(f"    {t},")
    lines.append(")")
    lines.append("")
    lines.append("")
    lines.append(f'__all__ = ["{class_name}"]')
    lines.append("")
    lines.append("")
    lines.append(f"class {class_name}(Style):")
    lines.append('    """')
    lines.append(f"    Pygments style generated from the VS Code theme {theme_name!r}.")
    lines.append('    """')
    lines.append("")
    lines.append(f'    name = "{style_name}"')
    lines.append(f'    aliases = ["{alias}"]')
    lines.append("")
    lines.append(f'    background_color = "{editor["background_color"]}"')
    lines.append(f'    highlight_color = "{editor["highlight_color"]}"')
    if editor.get("line_number_color"):
        lines.append(f'    line_number_color = "{editor["line_number_color"]}"')
    lines.append("")
    lines.append("    styles = {")
    lines.append(f'        Text: "{editor["foreground"]}",')
    for t in used_tokens:
        ts = token_styles[t]
        value = render_value(ts.color, ts.style_words)
        lines.append(f"        {t}: \"{value}\",")
    lines.append("    }")
    lines.append("")

    module = "\n".join(lines)
    return module


# --------------------------------------------------------------------------
# 8. CLI
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", help="Path or URL to a VS Code theme JSON file")
    parser.add_argument("-o", "--output", help="Output .py file (default: print to stdout)")
    parser.add_argument("--background", help="Override editor background color (e.g. #1e1e1e)")
    parser.add_argument("--foreground", help="Override default text/foreground color")
    args = parser.parse_args(argv)

    theme = load_theme(args.source)
    rules = flatten_token_colors(theme)
    token_styles = build_token_styles(rules)
    editor = get_editor_colors(theme, args.background, args.foreground)

    for w in editor["warnings"]:
        print(f"warning: {w}", file=sys.stderr)

    module_src = generate_module(theme, token_styles, editor)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(module_src)
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(module_src)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
