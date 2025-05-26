
from scanner import Scanner
from token_types import Token, TokenType
from scanner_states import ScannerState
from style_reader import tag_style

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

	def __init__(self, source_lines, style:dict, language, user_types, enable_line_numbers:bool, starting_line_number:int, text_size:float, tab_width:int, draw_border:bool):
		self.code_lines = source_lines
		self.style = style
		self.language = language
		self.user_types = user_types
		self.tab_width = tab_width
		self.font_size = text_size
		self.scanner_state = ScannerState.DEFAULT

		line_numbering_width = len(str(len(self.code_lines)))
		self.line_numbering = Line_numbering(enable_line_numbers, starting_line_number, line_numbering_width)
		self.draw_border = draw_border

	def create_span(self, text:str, style_def:tag_style):
		styleOpen = "<i>" if style_def.slanted else ""
		styleClose = "</i>" if style_def.slanted else ""
		weightOpen = "<b>" if style_def.bold else ""
		weightClose = "</b>" if style_def.bold else ""
		background = f"background-color:{style_def.bg_color};" if style_def.switch_colors else ""

		span = "<span style=\"{background}color:{color};\">{styleOpen}{weightOpen}{text}{weightClose}{styleClose}</span>".format(
			background=background,
			color=style_def.text_color,
			text=text,
			styleOpen=styleOpen, styleClose=styleClose,
			weightOpen=weightOpen, weightClose=weightClose)
		return span

	def create_line_number_span(self):
		width = self.line_numbering.width
		text = "{number!s:>{width}} ".format(number=self.line_numbering.get_next_line_number(), width=self.line_numbering.width)
		text = text.replace(" ", nbsp)
		span = "<span style=\"background-color:{bg_color}; color:{color};\">{text}</span>"\
			.format(bg_color=self.style["line_number_bg"], color=self.style["line_number_fg"], text=text)
		return span

# Use the monospace fonts included by default in Windows, MacOS and linux and fallback to generic monospace
	def create_div(self):
		div = """
<div style=\"\
font-family:Consolas, Monaco, 'Liberation Mono', FreeMono, monospace;\
font-size:{font_size}em;\
{border_settings}
color:{fg};\
background-color:{bg};\
padding:10px;\">
""".format(
		font_size=str(self.font_size),
		border_color=self.style["foreground"],
		fg=self.style["foreground"], 
		bg=self.style["background"],
		border_settings=
""""
border-width:0.1em;\
border-style:solid;\
border-color:{border_color};
""" if self.draw_border else ""
		)
		return div

	def tokenize_line(self, line, language, user_types) -> list:
		s = Scanner(self.scanner_state, line, language, user_types)
		tokens = s.get_tokens() # state of scanner changes when reading tokens
		self.scanner_state = s.get_state()
		return tokens

	def convert_token_text(self, token):
			token.text = token.text.replace('&', "&amp;")
			token.text = token.text.replace('<', "&lt;")
			token.text = token.text.replace('>', "&gt;")
			if token.text.startswith("\"") or token.text.startswith('\''):
				token.text = token.text.replace('\"', "&quot;")
				token.text = token.text.replace('\'', "&apos;")

	def convert_line_to_tokens(self, line:str) -> list:
		return self.tokenize_line(line, self.language, self.user_types)

	def convert_to_html(self, line:str):
		# Tokenize
		tokens = self.convert_line_to_tokens(line)
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
					# Only needed if more than one space
					if len(t.text) > 1:
						for space in t.text:
							if space == ' ':
								line += nbsp
					else:
						line += ' ';
				case TokenType.TEXT:
					self.convert_token_text(t)
					line += t.text
				case _:
					self.convert_token_text(t)
					class_name = t.type.value
					style_def = tag_style(self.style,class_name)
					line += self.create_span(t.text, style_def)

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

	def print_to_text_widget(self, styler:object, text_widget:object) -> object:
		# parses text and inserts it into a Python tkinter text widget
		for line in self.code_lines:
			tokens = []
			try:
				tokens = self.convert_line_to_tokens(line)
			except BaseException as ex:
				print(ex)

			for t in tokens:
				styler.insert_stylized_text(text_widget, self.style, t)
			styler.insert_new_line(text_widget)
