
from token import Token
from token import TokenType

class Scanner:
	def __init__(self, line, language, user_types):
		self.source = line
		self.start = 0
		self.current = 0
		self.tokens = []
		self.language = language
		self.user_types

	def get_tokens(self):
		while(self.isAtEnd() == False):
			self.start = self.current
			self.scan_token()
		return self.tokens

	def isAtEnd(self):
		return self.current >= len(self.source)

	def add_token(self, type):
		token_text = self.source[self.start:self.current]
		self.tokens.append(Token(type, token_text))

	def add_string_token(self):
		# Advance until find another "
		while self.peek() != '\"' and self.isAtEnd() == False:
			self.advance()


		self.advance() # Found terminating "
		self.add_token(type=TokenType.CONSTANT)

	def add_number_token(self):
		while self.peek().isdigit():
			self.advance()

		if self.peek() == "." and self.peek_next().isdigit:
			self.advance()

		while self.peek().isdigit():
			self.advance()

		self.add_token(type=TokenType.CONSTANT)

	# Possible choices
	# variable name -> TEXT
	# keyword -> KEYWORD
	# text( -> FUNCTION
	def add_identifier_token(self):
		while self.peek().isalnum():
			self.advance()

		token_text = self.source[self.start: self.current]

		if token_text in self.language.keywords:
			self.add_token(type=TokenType.KEYWORD)
		if token_text in self.language.primitive_types:
			self.add_token(type=TokenType.PRIMITIVE_TYPE)
		if token_text in self.user_types:
			self.add_token(type=TokenType.USER_TYPE)
		elif self.peek() == "(":
			self.add_token(type=TokenType.FUNCTION)
		else:
			self.add_token(type=TokenType.TEXT)

	def advance(self):
		c = self.source[self.current]
		self.current += 1
		return c

	def next_is(self, character):
		if self.isAtEnd():
			return False
		elif self.source[self.current] != character:
			return False
		else:
			self.current += 1
			return True
		
	def peek(self):
		if self.isAtEnd():
			return ''
		else:
			return self.source[self.current]

	def peek_next(self):
		if self.current + 1 >= len(self.source):
			return ''
		else:
			return self.source[self.current + 1]

	def scan_token(self):
		c = self.advance()
		match c:
			case '(':
				self.add_token(TokenType.LEFT_PAREN)
			case ')':
				self.add_token(TokenType.RIGHT_PAREN)
			case '/':
				if self.next_is('/'):
					while self.peek() != '' and self.isAtEnd() == False:
						self.advance()
					self.add_token(TokenType.COMMENT)
				else:
					self.add_token(TokenType.OPERATOR)
			case '+'|'-'|'*'|'%':
				self.add_token(TokenType.OPERATOR)
			case '!':
				if self.next_is('='):
					self.add_token(TokenType.OPERATOR)
				else:
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
			case '\"':
				self.add_string_token()
			case ' ':
				self.add_token(type=TokenType.WHITESPACE)
			case '\t':
				self.add_token(type=TokenType.TAB)
			case _:
				if c.isdigit():
					self.add_number_token()
				elif c.isalpha():
					self.add_identifier_token()
				else:
					self.add_token(type=TokenType.TEXT)
