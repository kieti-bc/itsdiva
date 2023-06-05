from enum import Enum, auto

class TokenType(Enum):
	KEYWORD = "keyword"
	NUMBER = "number"
	STRING = "string"
	USER_TYPE = "user_type"
	PRIMITIVE_TYPE = "primitive_type"
	COMMENT = "comment"
	DOC_COMMENT = "doc_comment"
	OPERATOR = "operator"
	FUNCTION = "function"
	TEXT = "text"
	WHITESPACE = "ws"
	TAB = "tab"
	NEWLINE = "newline"

class Token:
	def __init__(self, type, text):
		self.type = type
		self.text = text