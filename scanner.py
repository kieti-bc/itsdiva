
from token_types import Token
from token_types import TokenType
from scanner_states import ScannerState

class Scanner:
	def __init__(self, state, line, language, user_types):
		self.state = state
		self.source = line
		self.start = 0
		self.current = 0
		self.tokens = []
		self.language = language
		self.user_types = user_types

	def get_state(self):
		return self.state

	def set_state(self, new_state):
		self.state = new_state

	def get_tokens(self):
		while(self.isAtEnd() == False):
			try:
				self.start = self.current
				self.scan_token()
			except BaseException as ex:
				print(ex)	
		return self.tokens

	def isAtEnd(self):
		return self.current >= len(self.source)

	# Returns the current text that has been scanned
	def get_current_text(self):
		return self.source[self.start:self.current]

	def add_token(self, type):
		token_text = self.source[self.start:self.current]
		# Notice if type is same as the previous type
		# if the type is same, extend the previous token
		if len(self.tokens) > 0 and type == self.tokens[-1].type:
			self.tokens[-1].text += token_text
		else:
			self.tokens.append(Token(type, token_text))

	# Can be double or single quotes
	def add_string_token(self, quote):
		# Advance until find another "
		while self.peek() != quote and self.isAtEnd() == False:
			self.advance()

		if self.isAtEnd() == True:
			# String did not terminate
			self.add_token(TokenType.TEXT)
		else:
			self.advance() # Found terminating "
			self.add_token(type=TokenType.STRING)

	def add_number_token(self):
		while (True):
			p = self.peek()
			if p.isdigit():
				self.advance()
			elif p == "." and self.peek_next().isdigit:
				self.advance()
			else:
				break

		self.add_token(type=TokenType.NUMBER)

	# Possible choices
	# variable name -> TEXT
	# keyword -> KEYWORD
	# text( -> FUNCTION
	def add_identifier_token(self):
		while self.peek().isalnum() or self.peek() == '_':
			self.advance()

		token_text = self.source[self.start: self.current]

		# Could this be a new user type?
		# Is this preceded by WHITESPACE and language specific user type keyword eg. "Class"?
		if len(self.tokens) >= 2:
			prev_white = self.tokens[-1].type == TokenType.WHITESPACE
			prev_class = self.tokens[-2].type == TokenType.KEYWORD and \
			self.language.is_user_type_keyword(self.tokens[-2].text)

			if prev_class and prev_white:
				self.user_types.append(token_text)

		if token_text in self.language.keywords:
			self.add_token(type=TokenType.KEYWORD)
		elif token_text in self.language.primitive_types:
			self.add_token(type=TokenType.PRIMITIVE_TYPE)
		elif token_text in self.user_types or token_text in self.language.builtin_types:
			self.add_token(type=TokenType.USER_TYPE)
		elif token_text in self.language.user_type_keywords:
			self.add_token(type=TokenType.USER_TYPE)
		elif self.peek() == "(":
			self.add_token(type=TokenType.FUNCTION)
		else:
			self.add_token(type=TokenType.TEXT)

	# Advance to the next character
	def advance(self):
		c = self.source[self.current]
		self.current += 1
		return c

	# Advances if next character is the parameter
	def next_is(self, character):
		if self.isAtEnd():
			return False
		elif self.source[self.current] != character:
			return False
		else:
			self.current += 1
			return True
		
	# Returns next character
	# Returns empty string when at end
	def peek(self):
		if self.isAtEnd():
			return ''
		else:
			return self.source[self.current]

	# Returns next+amount character, 1 by default
	# Returns empty string when at end
	def peek_next(self, amount=1):
		if self.current + amount >= len(self.source):
			return ''
		else:
			return self.source[self.current + amount]

	def scan_token(self):
		c = self.advance()
		l = self.language
		found_language_token = l.scan_token(c, self)
		if found_language_token == True:
			return

		# If reading a multi line comment, then everything
		# is a comment until language notices that the multi line
		# comment has ended
		if self.state == ScannerState.MULTI_LINE_COMMENT:
			self.add_token(TokenType.COMMENT)
			return

		match c:
			case '/':
				if self.next_is('/'):
					t_type = TokenType.COMMENT

					while self.peek() != '' and self.isAtEnd() == False:
						self.advance()

					self.add_token(t_type)
				else:
					self.add_token(TokenType.OPERATOR)
			case '+'|'-'|'*'|'%'|'/':
				if self.next_is('='):
					pass
				self.add_token(TokenType.OPERATOR)
			case '!':
				if self.next_is('='):
					pass
				self.add_token(TokenType.OPERATOR)
			case '=':
				if self.next_is('='):
					self.add_token(TokenType.OPERATOR)
				else:
					self.add_token(TokenType.OPERATOR)
			case '<':
				if self.next_is('='):
					self.add_token(TokenType.OPERATOR)
				else:
					self.add_token(TokenType.OPERATOR)
			case '>':
				if self.next_is('='):
					self.add_token(TokenType.OPERATOR)
				else:
					self.add_token(TokenType.OPERATOR)
			case '\"'|'\'':
				self.add_string_token(c)
			case ' ':
				self.add_token(TokenType.WHITESPACE)
			case '\t':
				self.add_token(TokenType.TAB)
			case _:
				if c.isdigit():
					self.add_number_token()
				elif c.isalpha():
					self.add_identifier_token()
				else:
					self.add_token(TokenType.TEXT)
