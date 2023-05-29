
from token_types import Token
from token_types import TokenType

class Scanner:
	def __init__(self, line, language, user_types):
		self.source = line
		self.start = 0
		self.current = 0
		self.tokens = []
		self.language = language
		self.user_types = user_types

	def get_tokens(self):
		while(self.isAtEnd() == False):
			try:
				self.start = self.current
				self.scan_token()
			except BaseException:
				# TODO error reporting
				pass
		return self.tokens

	def isAtEnd(self):
		return self.current >= len(self.source)

	def add_token(self, type):
		token_text = self.source[self.start:self.current]
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

		# Could this be a new user type?
		# Is this preceded by WHITESPACE and KEYWORD "Class"?
		if len(self.tokens) >= 2:
			prev_white = self.tokens[-1].type == TokenType.WHITESPACE
			prev_class = self.tokens[-2].type == TokenType.KEYWORD and \
			self.tokens[-2].text == "class"

			if prev_class and prev_white:
				self.user_types.append(token_text)

		if token_text in self.language.keywords:
			self.add_token(type=TokenType.KEYWORD)
		elif token_text in self.language.primitive_types:
			self.add_token(type=TokenType.PRIMITIVE_TYPE)
		elif token_text in self.user_types:
			self.add_token(type=TokenType.USER_TYPE)
		elif self.peek() == "(":
			self.add_token(type=TokenType.FUNCTION)
		else:
			self.add_token(type=TokenType.TEXT)

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

		match c:
			case '/':
				if self.next_is('/'):
					t_type = TokenType.COMMENT
					if self.next_is('/'):
						t_type = TokenType.DOC_COMMENT

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
