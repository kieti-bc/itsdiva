from token_types import TokenType

class Style_Dark:
	name = "Dark"

	colors = {
		"background": "DarkSlateGrey",
		"default": "GhostWhite",

		TokenType.KEYWORD: "CornflowerBlue",
		TokenType.CONSTANT: "LightCoral",
		TokenType.USER_TYPE: "Violet",
		TokenType.PRIMITIVE_TYPE: "Plum",
		TokenType.COMMENT: "SpringGreen",
		TokenType.DOC_COMMENT: "LightGreen",
		TokenType.OPERATOR: "LightCyan",
		TokenType.FUNCTION: "Gold"
	}