from token_types import TokenType

class Language_Bash:

	def scan_token(self, character, scanner):
		match character:
			case '#':
				while scanner.peek() != '' and scanner.isAtEnd() == False:
					scanner.advance()

				scanner.add_token(TokenType.COMMENT)
				return True
			case '$': # Variable access or command. Commands are listed as keywords
				if scanner.next_is('('):
					# TODO is keyword next?
					scanner.add_token(TokenType.KEYWORD)
					return True
				else:
					while (scanner.peek().isalnum() or scanner.peek() == '_') and scanner.isAtEnd() == False:
						scanner.advance()
					scanner.add_token(TokenType.PRIMITIVE_TYPE)
					return True
			case ')':
				scanner.add_token(TokenType.KEYWORD)
				return True
			case '-': # Comparison operators
				is_operator = False
				if scanner.peek() == 'g' and (scanner.peek_next(1) == 't' or scanner.peek_next(1) == 'e'):
					is_operator = True
				elif scanner.peek() == 'l' and (scanner.peek_next(1) == 't' or scanner.peek_next(1) == 'e'):
					is_operator = True
				elif scanner.peek() == 'e' and scanner.peek_next(1) == 'q':
					is_operator = True
				elif scanner.peek() == 'n' and scanner.peek_next(1) == 'e':
					is_operator = True
				
				if is_operator:
					scanner.advance()
					scanner.advance()
					scanner.add_token(TokenType.OPERATOR)
					return True

			case '|':
				scanner.add_token(TokenType.OPERATOR)
				return True

		return False

	def is_user_type_keyword(self, word:str):
		return word in Language_Bash.user_type_keywords


	name = "Bash"
	keywords = [
		"if",
		"else",
		"then",
		"fi",
		"in",
		"do",
		"done"
	]

	user_type_keywords = [
		"echo",
		"ls",
		"cd",
		"mkdir",
		"date",
		"pwd",
		"cat",
		"cp",
		"mv",
		"cp",
		"touch",
		"rmdir",
		"stat"
	]
	primitive_types = []
	builtin_types = []
	