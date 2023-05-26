
from token_types import TokenType

class Language_Python:

	# If this token is specific to this language
	# add it to scanner and return True
	# Otherwise return false
	def scan_token(self, character, scanner):
		match character:
			case '#':
				while scanner.peek() != '' and scanner.isAtEnd() == False:
					scanner.advance()

				scanner.add_token(TokenType.COMMENT)
				return True
			case '/':
				if scanner.next_is('/'):
					scanner.add_token(TokenType.OPERATOR)
					return True
			case '_':
				if scanner.next_is('_'):
					# Python reserved word
					while scanner.peek().isalpha() and scanner.peek() != '_' and scanner.isAtEnd() == False:
						scanner.advance()

					if (scanner.isAtEnd() == False):
						if scanner.peek() == '_' and scanner.next_is('_'):
							scanner.add_token(TokenType.KEYWORD)
							return True

		return False

	name = "python"

	keywords = [
	"and",
	"as",
	"assert",
	"async",
	"await",
	"break",
	"class",
	"continue",
	"def",
	"del",
	"elif",
	"else",
	"except",
	"False",
	"finally",
	"for",
	"from",
	"global",
	"if",
	"import",
	"in",
	"is",
	"lambda",
	"None",
	"nonlocal",
	"not",
	"or",
	"pass",
	"raise",
	"return",
	"True",
	"try",
	"while",
	"with",
	"yield",
	]

	primitive_types = [
		"int",
		"bool",
		"float",
		"complex",
		"str",
		"list",
		"dict",
	]