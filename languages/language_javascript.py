from token_types import TokenType
from scanner_states import ScannerState

class Language_Javascript:

	def scan_token(self, character, scanner):
		match character:
			# Operators in javascript
			case '+':
				if scanner.next_is(character):
					pass
				scanner.add_token(TokenType.OPERATOR)
				return True
			case '*':
				if scanner.next_is(character):
					if scanner.next_is('='):
						pass
				scanner.add_token(TokenType.OPERATOR)
				return True
			case '=':
				if scanner.next_is(character):
					if scanner.next_is(character):
						pass
				scanner.add_token(TokenType.OPERATOR)
				return True
			case '!':
				if scanner.next_is('='):
					if scanner.next_is('='):
						pass
				scanner.add_token(TokenType.OPERATOR)
				return True
			case '?':
				scanner.add_token(TokenType.OPERATOR)
				return True

			# Multi line comment
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
		return word in Language_Javascript.user_type_keywords

	user_type_keywords = [
		"class"
	]

	name = "Javascript"

	keywords = [
		"abstract",
		"arguments",
		"await",
		"boolean",
		"break",
		"byte",
		"case",
		"catch",
		"char",
		"class",	
		"continue",
		"debugger",
		"default",
		"delete",
		"do",
		"double",
		"else",
		"enum",
		"eval",
		"export",	
		"extends",
		"false",
		"final",
		"finally",	
		"float",
		"for",
		"function",
		"goto",
		"if",
		"implements",
		"import",
		"in",
		"instanceof",
		"int",
		"interface",
		"long",	
		"NaN",
		"native",	
		"new",
		"null",	
		"package",	
		"private",
		"protected",
		"public",
		"return",
		"short",
		"static",
		"super",
		"switch",
		"synchronized",
		"this",
		"throw",
		"throws",
		"transient",	
		"true",
		"try",
		"typeof",
		"void",
		"volatile",
		"while",
		"with",
		"yield",
	]
	

	primitive_types = [
		"undefined",
		"Number",
		"BigInt",
		"String",
		"Boolean",
		"Symbol",
		"Date",
		"Error",
		"const",
		"let",
		"var",
	]