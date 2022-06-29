from pygments.style import Style
from pygments.token import (
    Comment,
    Generic,
    Keyword,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Token,
    Whitespace,
)


class OneDarkStyle(Style):
    """
    Theme inspired by One Dark for Atom

    """

    background_color = "#282C34"

    styles = {
        Token: "#ABB2BF",
        Punctuation: "#ABB2BF",
        Punctuation.Marker: "#ABB2BF",
        Keyword: "#C678DD",
        Keyword.Constant: "#E5C07B",
        Keyword.Declaration: "#C678DD",
        Keyword.Namespace: "#C678DD",
        Keyword.Reserved: "#C678DD",
        Keyword.Type: "#E5C07B",
        Name: "#ABB2BF",
        Name.Attribute: "#E06C75",
        Name.Builtin: "#61AFEF",
        Name.Class: "#E5C07B",
        Name.Function: "#61AFEF",
        Name.Function.Magic: "#56B6C2",
        Name.Other: "#E06C75",
        Name.Tag: "#E06C75",
        Name.Decorator: "#61AFEF",
        Name.Variable.Class: "",
        String: "#98C379",
        Number: "#D19A66",
        Operator: "#8078DD",
        Comment: "#7F848E",
    }
