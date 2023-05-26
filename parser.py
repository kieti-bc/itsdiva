
from scanner import Scanner
from token_types import Token, TokenType

# HTML constants
nbsp = "&nbsp;"

# CSS class names
class_names = {
	TokenType.KEYWORD: "kw",
	TokenType.CONSTANT: "ct",
	TokenType.USER_TYPE: "ut",
	TokenType.PRIMITIVE_TYPE: "pt",
	TokenType.COMMENT: "cc",
	TokenType.DOC_COMMENT: "dc",
	TokenType.OPERATOR: "op",
	TokenType.FUNCTION: "fc",
}

class Parser:


	def __init__(self, source_lines, style:dict, language, user_types):
		self.code_lines = source_lines
		self.style = style
		self.language = language
		self.user_types = user_types

	def create_span(self, class_name, text):
		span = "<span class=\"{class_name}\">{text}</span>".format(class_name=class_name, text=text)
		return span

	def create_css(self, style):
		css = """
<style>\
.kw {{ color:{kw_color}; }} \
.ct {{ color:{ct_color}; }} \
.ut {{ color:{ut_color}; }} \
.pt {{ color:{pt_color}; }} \
.cc {{ color:{cc_color}; }} \
.dc {{ color:{dc_color}; }} \
.op {{ color:{op_color}; }} \
.fc {{ color:{fc_color}; }} \
</style>
""".format(kw_color=style[class_names[TokenType.KEYWORD]],
		ct_color=style[class_names[TokenType.CONSTANT]],
		ut_color=style[class_names[TokenType.USER_TYPE]],
		pt_color=style[class_names[TokenType.PRIMITIVE_TYPE]],
		cc_color=style[class_names[TokenType.COMMENT]],
		dc_color=style[class_names[TokenType.DOC_COMMENT]],
		op_color=style[class_names[TokenType.OPERATOR]],
		fc_color=style[class_names[TokenType.FUNCTION]]
		)
		return css

	def tokenize_line(self, line, language, user_types):
		s = Scanner(line, language, user_types)
		tokens = s.get_tokens()
		return tokens

	def convert_token_text(self, token) -> str:
		if token.type == TokenType.COMMENT or \
			token.type == TokenType.DOC_COMMENT or \
			token.type == TokenType.OPERATOR or \
			token.type == TokenType.CONSTANT:
			token.text = token.text.replace('&', "&amp;")
			token.text = token.text.replace('<', "&gt;")
			token.text = token.text.replace('>', "&lt;")
			if token.text.startswith("\"") or token.text.startswith('\''):
				token.text = token.text.replace('\"', "&quot;")
				token.text = token.text.replace('\'', "&apos;")

	def convert_to_html(self, line, style:dict, language, user_types):
		# Tokenize
		tokens = self.tokenize_line(line, language, user_types)
		# Iterate tokens
		line = ""



		for t in tokens:
			# create spans
			# concatenate
			# Change some characters to html 
			self.convert_token_text(t)

			if t.type in class_names:
				class_name = class_names[t.type]
				line += self.create_span(class_name, t.text)
			else:
				match t.type:
					case TokenType.TAB:
						for i in range(4):
							line += nbsp
					case TokenType.WHITESPACE:
						line += nbsp
					case _: 
						line += t.text

		# return
		line += "<br>"
		return line

	def create_html(self) -> list:
		html_lines = []
		html_lines.append(self.create_css(self.style))

		div = """\
<div style=\"\
font-family:monospace;\
border-width:0.1em;\
border-style:solid;\
border-color:Black;\
color:{fg};\
background-color:{bg};\">\
		""".format(fg=self.style["fg"], bg=self.style["bg"])

		html_lines.append(div)
		for line in self.code_lines:
			try:
				html_lines.append(self.convert_to_html(line, self.style, self.language, self.user_types))
			except BaseException:
				pass

		html_lines.append("</div>")

		return html_lines