
from token_types import TokenType
from scanner_states import ScannerState

class Language_Csharp:

	# If this token is specific to this language
	# add it to scanner and return True
	# Otherwise return false
	def scan_token(self, character, scanner):
		match character:
			case '/':
				if scanner.next_is(character):
					t_type = TokenType.COMMENT
					if scanner.next_is(character):
						t_type = TokenType.DOC_COMMENT

					while scanner.peek() != '' and scanner.isAtEnd() == False:
						scanner.advance()

					scanner.add_token(t_type)
					return True
				elif scanner.next_is('*'):
					t_type = TokenType.COMMENT
					scanner.set_state(ScannerState.MULTI_LINE_COMMENT)

					# Read the rest of the line as comment
					while scanner.peek() != '' and scanner.isAtEnd() == False:
						scanner.advance()

					scanner.add_token(t_type)
					return True
			case '*':
				if scanner.get_state() == ScannerState.MULTI_LINE_COMMENT:
					if scanner.next_is('/'):
						t_type = TokenType.COMMENT
						scanner.set_state(ScannerState.DEFAULT)
						scanner.add_token(t_type)
						return True

		return False


	def is_user_type_keyword(self, word:str):
		return word in Language_Csharp.user_type_keywords

	user_type_keywords = [
		"class",
		"struct",
		"enum"
	]

	name = "C#"

	keywords = [
	"abstract",
	"as",
	"base",
	"break",
	"case",
	"catch",
	"checked",
	"class",
	"const",
	"continue",
	"default",
	"delegate",
	"do",
	"else",
	"enum",
	"event",
	"explicit",
	"extern",
	"false",
	"finally",
	"fixed",
	"for",
	"foreach",
	"goto",
	"if",
	"implicit",
	"in",
	"interface",
	"internal",
	"is",
	"lock",
	"namespace",
	"new",
	"null",
	"object",
	"operator",
	"out",
	"override",
	"params",
	"private",
	"protected",
	"public",
	"readonly",
	"ref",
	"return",
	"sealed",
	"sizeof",
	"stackalloc",
	"static",
	"struct",
	"switch",
	"this",
	"throw",
	"true",
	"try",
	"typeof",
	"unchecked",
	"unsafe",
	"using",
	"virtual",
	"void",
	"volatile",
	"while",
	]

	primitive_types = [
	"bool",
	"byte",
	"char",
	"decimal",
	"double",
	"float",
	"int",
	"long",
	"sbyte",
	"short",
	"string",
	"uint",
	"ulong",
	"ushort",
	]