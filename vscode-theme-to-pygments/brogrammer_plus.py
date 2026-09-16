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
    line_number_color = "#EEE"

    styles = {
        Text: "#EEE",
        Error: "",
        Comment: "italic #EEE",
        Comment.Preproc: "bold #e74c3c",
        Comment.Special: "bold #e74c3c",
        Comment.Doc: "bold #e74c3c",
        Keyword: "bold #e74c3c",
        Keyword.Namespace: "bold #e74c3c",
        Keyword.Declaration: "#3498db",
        Keyword.Constant: "#6c71c4",
        Keyword.Type: "#3cc9d6",
        Keyword.Reserved: "bold #e74c3c",
        Operator: "bold #e74c3c",
        Operator.Word: "bold #e74c3c",
        Punctuation: "#EEE",
        Name.Namespace: "#3cc9d6",
        Name.Class: "#2ecc71",
        Name.Exception: "#3cc9d6",
        Name.Function: "#3498db",
        Name.Function.Magic: "#3498db",
        Name.Decorator: "#3498db",
        Name.Attribute: "#2ecc71",
        Name.Tag: "#e74c3c",
        Name.Builtin: "#3498db",
        Name.Builtin.Pseudo: "#EEE",
        Name.Variable: "#EEE",
        Name.Variable.Instance: "#EEE",
        Name.Variable.Global: "#EEE",
        Name.Variable.Class: "#EEE",
        Name.Constant: "#2ecc71",
        Name.Label: "#2ecc71",
        Name.Property: "#EEE",
        Name.Entity: "#6c71c4",
        Number: "#6c71c4",
        String: "#f1c40f",
        String.Doc: "italic #EEE",
        String.Escape: "#6c71c4",
        String.Regex: "#3498db",
        String.Symbol: "#6c71c4",
        Generic.Deleted: "#e74c3c",
        Generic.Inserted: "#2ecc71",
        Generic.Error: "",
    }
