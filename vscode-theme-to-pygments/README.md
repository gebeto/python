# vscode-theme-to-pygments

Convert a VS Code color theme (`*-color-theme.json`) into a [Pygments](https://pygments.org/) `Style` subclass, in the shape of [lepture/pygments-styles](https://github.com/lepture/pygments-styles).

Single file, no dependencies beyond the standard library (Pygments is only needed to *use* the generated style, not to generate it).

## Usage

```bash
# print the generated module to stdout
python3 converter.py brogrammer-plus-color-theme.json

# write it to a file
python3 converter.py brogrammer-plus-color-theme.json -o brogrammer_plus.py

# themes can also be fetched straight from a URL
python3 converter.py https://raw.githubusercontent.com/user/repo/main/theme.json -o my_style.py
```

### Options

| Option | Description |
| --- | --- |
| `source` | Path or URL to a VS Code theme JSON file (required) |
| `-o`, `--output` | Output `.py` file; defaults to printing to stdout |
| `--background` | Override the editor background color (e.g. `#1e1e1e`) |
| `--foreground` | Override the default text/foreground color |

## Example output

```python
from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Text,
)


__all__ = ["BrogrammerPlusStyle"]


class BrogrammerPlusStyle(Style):
    """
    Pygments style generated from the VS Code theme 'Brogrammer Plus'.
    """

    name = "brogrammer-plus"
    aliases = ["Brogrammer Plus"]

    background_color = "#121212"
    highlight_color = "#121212"
    line_number_color = "#ffffff99"

    styles = {
        Text: "#ffffffde",
        Comment: "italic #ffffff99",
        Keyword: "bold #e74c3c",
        Name.Class: "#2ecc71",
        Name.Function: "#3498db",
        # ...
    }
```

### Using the generated style

```python
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from brogrammer_plus import BrogrammerPlusStyle

print(highlight("print('hi')", PythonLexer(), HtmlFormatter(style=BrogrammerPlusStyle)))
```

## How it works

1. **Load + strip JSONC.** VS Code theme files are JSON with comments and occasional trailing commas. `strip_jsonc()` removes `//` and `/* */` comments (string-literal aware) and trailing commas before parsing.
2. **Flatten `tokenColors`.** Every entry's scopes become individual `ScopeRule`s, recording foreground, `fontStyle`, and original list position. Space-separated selectors like `meta.object-literal.key string` are matched on their innermost component but flagged `compound`, so a context-dependent rule can't hijack a generic token.
3. **Map Pygments tokens to scopes.** `SCOPE_CANDIDATES` lists, for each Pygments token, the TextMate scopes to try in order of preference. The best match is chosen by: exact scope > ancestor > descendant, then plain rules over compound ones, then specificity, then candidate order, then later position in `tokenColors` (matching VS Code's "last rule wins" semantics).
4. **Pull editor colors.** `editor.background`, `editor.foreground`, `editorLineNumber.foreground`, and a line-highlight/selection background become the class-level attributes.
5. **Generate the module.** Tokens are emitted in a readable grouped order with only the needed `pygments.token` imports.

## Notes and caveats

- TextMate scopes don't map 1:1 onto Pygments token types, so this is a best-effort conversion. Eyeball the result and tweak `SCOPE_CANDIDATES` (or the generated file) for the languages you care about.
- `fontStyle` values `bold`, `italic`, and `underline` carry over; `strikethrough` is dropped since Pygments has no equivalent.
- Some themes (e.g. "-base" variants meant to be merged with a second file) omit `editor.background`/`editor.foreground`. Sensible fallbacks (`#1e1e1e` / `#d4d4d4`) are used and a warning is printed to stderr — pass `--background`/`--foreground`, or merge the variant file yourself first.
- Alpha channels from VS Code colors (e.g. `#ffffff99`) are passed through verbatim; some Pygments formatters ignore them.
