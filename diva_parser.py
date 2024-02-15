
from scanner import Scanner
from token_types import Token, TokenType
from scanner_states import ScannerState

# HTML constants
nbsp = "&nbsp;"

class Line_numbering:
	def __init__(self, enabled:bool, first:int, width:int):
		self.enabled = enabled
		self.first = first
		self.width = width
		self.current = first

	def get_next_line_number(self):
		n = self.current
		self.current += 1
		return n

class Parser:

	def __init__(self, source_lines, style:dict, language, user_types, enable_line_numbers, starting_line_number:int, text_size):
		self.code_lines = source_lines
		self.style = style
		self.language = language
		self.user_types = user_types
		self.tab_width = 4
		self.font_size = text_size
		self.scanner_state = ScannerState.DEFAULT

		line_numbering_width = len(str(len(self.code_lines)))
		self.line_numbering = Line_numbering(enable_line_numbers, starting_line_number, line_numbering_width)

	def create_span(self, color, text):
		span = "<span style=\"color:{color};\">{text}</span>".format(color=color, text=text)
		return span

	def create_line_number_span(self):
		width = self.line_numbering.width
		text = "{number!s:>{width}} ".format(number=self.line_numbering.get_next_line_number(), width=self.line_numbering.width)
		text = text.replace(" ", nbsp)
		span = "<span style=\"background-color:{bg_color}; color:{color};\">{text}</span>"\
			.format(bg_color=self.style["line_number_bg"], color=self.style["line_number_fg"], text=text)
		return span

	def create_div(self):
		div = """
<div style=\"\
font-family:monospace;\
font-size:{font_size}em;\
border-width:0.1em;\
border-style:solid;\
border-color:{border_color};\
color:{fg};\
background-color:{bg};\">
""".format(
		font_size=str(self.font_size),
		border_color=self.style["foreground"],
		fg=self.style["foreground"], 
		bg=self.style["background"],
		)
		return div

	def tokenize_line(self, line, language, user_types):
		s = Scanner(self.scanner_state, line, language, user_types)
		tokens = s.get_tokens() # state of scanner changes when reading tokens
		self.scanner_state = s.get_state()
		return tokens

	def convert_token_text(self, token) -> str:
			token.text = token.text.replace('&', "&amp;")
			token.text = token.text.replace('<', "&lt;")
			token.text = token.text.replace('>', "&gt;")
			if token.text.startswith("\"") or token.text.startswith('\''):
				token.text = token.text.replace('\"', "&quot;")
				token.text = token.text.replace('\'', "&apos;")

	def convert_to_html(self, line:str):
		# Tokenize
		tokens = self.tokenize_line(line, self.language, self.user_types)
		# Iterate tokens
		line = ""
		# Create line numbers?
		if self.line_numbering.enabled:
			line += self.create_line_number_span()

		for t in tokens:
			# create spans
			# concatenate
			# Change some characters to html 
			match t.type:
				case TokenType.TAB:
					for tab in t.text:
						if tab == '\t':
							for i in range(self.tab_width):
								line += nbsp
				case TokenType.WHITESPACE:
					for space in t.text:
						if space == ' ':
							line += nbsp
				case TokenType.TEXT:
					self.convert_token_text(t)
					line += t.text
				case _:
					self.convert_token_text(t)
					color = self.style["foreground"]
					class_name = t.type.value
					if class_name in self.style:
						color = self.style[class_name]
					line += self.create_span(color, t.text)

		line += "<br>"
		return line

	def create_html(self) -> list:
		html_lines = []
		div = self.create_div()
		html_lines.append(div)
		for line in self.code_lines:
			try:
				html_lines.append(self.convert_to_html(line))
			except BaseException as ex:
				print(ex)

		html_lines.append("</div>")
		return html_lines