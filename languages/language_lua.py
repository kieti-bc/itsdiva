
from token_types import TokenType

class Language_Lua:

	# If this token is specific to this language
	# add it to scanner and return True
	# Otherwise return false
	def scan_token(self, character, scanner):
		match character:
			case '-':
				if scanner.next_is('-'):
					while scanner.peek() != '' and scanner.isAtEnd() == False:
						scanner.advance()

					scanner.add_token(TokenType.COMMENT)
					return True
			# Todo multi line comments --[[ ]]--

		return False

	def is_user_type_keyword(self, word:str):
		return word in Language_Lua.user_type_keywords

	user_type_keywords = [
		"require",
	]

	name = "Lua"

	keywords = [
		"if",
		"then",
		"elseif",
		"end",
		"function",
		"for",
		"while",
		"do",
		"repeat",
		"until",
		"break",
		"goto",
		"return",
		"not",
		"and",
		"or",
		"in",
		"true",
		"false",
		"nil"
	]

	primitive_types = [
		"local"
	]

	builtin_types = [
		"table",
		"math",
		"string",
		"love"
	]
