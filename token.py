from enum import Enum, auto

class TokenType(Enum):
	KEYWORD = auto()
	CONSTANT = auto()
	USER_TYPE = auto()
	PRIMITIVE_TYPE = auto()
	COMMENT = auto()
	DOC_COMMENT = auto()
	OPERATOR = auto()
	FUNCTION = auto()
	LEFT_PAREN = auto()
	RIGHT_PAREN = auto()
	TEXT = auto()
	WHITESPACE = auto()
	TAB = auto()

class Token:
	def __init__(self, type, text):
		self.type = type
		self.text = text