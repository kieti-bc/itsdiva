from token_types import TokenType

class Language_Javascript:

	def scan_token(self, character, scanner):
		match character:
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
		return False

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
		"const",
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
		"let",
		"long",	
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
		"var",
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
	]