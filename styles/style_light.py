
from token_types import TokenType


class Style_Light:
	name = "Light"

	colors = {
		"background": "White",
		"default": "Black",

		TokenType.KEYWORD: "DarkBlue",
		TokenType.CONSTANT: "Crimson",
		TokenType.USER_TYPE: "DarkMagenta",
		TokenType.PRIMITIVE_TYPE: "DarkOrchid",
		TokenType.COMMENT: "DarkGreen",
		TokenType.DOC_COMMENT: "DarkSeaGreen",
		TokenType.OPERATOR: "MediumBlue",
		TokenType.FUNCTION: "DarkOrange"
	}