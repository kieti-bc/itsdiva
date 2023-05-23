
from scanner import Scanner

# HTML constants
nbsp = "&nbsp;"

class Parser:


	# CSS class names
	class_names = {
		TokenType.KEYWORD: "kw",
		TokenType.CONSTANT: "ct",
		TokenType.USER_TYPE: "ut",
		TokenType.PRIMITIVE_TYPE: "pt",
		TokenType.COMMENT: "cc",
		TokenType.DOC_COMMENT: "dc",
		TokenType.OPERATOR: "op",
		TokenType.FUNCTION: "ft",
	}

	def __init__(source_lines, style, language, user_types):
		self.code_lines = source_lines
		self.style = style
		self.language = language
		self.user_types = user_types



	def create_span(self, class_name, text):
		span = "<span class=\"{class_name}\">{text}</span>".format(class_name=class_name, text=text)
		return span

	def create_css(self, style):
		css = """
		<style =\" \
		.kw {{ color:{kw_color}; }} \
		.ct {{ color:{ct_color}; }} \
		.ut {{ color:{ut_color}; }} \
		.pt {{ color:{pt_color}; }} \
		.cc {{ color:{cc_color}; }} \
		.dc {{ color:{dc_color}; }} \
		.op {{ color:{op_color}; }} \
		.fc {{ color:{fc_color}; }} \
		\"
		""".format(kw_color=style[TokenType.KEYWORD],
		ct_color=style[TokenType.CONSTANT],
		ut_color=style[TokenType.USER_TYPE],
		pt_color=style[TokenType.PRIMITIVE_TYPE],
		cc_color=style[TokenType.COMMENT],
		dc_color=style[TokenType.DOC_COMMENT],
		op_color=style[TokenType.OPERATOR],
		fc_color=style[TokenType.FUNCTION],
		)
		return css

	def tokenize_line(self, line, language, user_types):
		s = Scanner(line, language, user_types)
		tokens = s.get_tokens()
		return tokens

	def convert_to_html(self, line, style, language, user_types):
		# Tokenize
		tokens = self.tokenize_line(line, language, user_types)
		# Iterate tokens
		line = ""
		for t in tokens:
			# create spans
			# concatenate
			if t.type in style:
				class_name = Parser.class_names[t.type]
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

		div = """
		<div style=\"\
		font-family:monospace;\
		border-width:0.1em;\
		border-style:solid;\
		border-color:Black;\
		color:{fg};\
		background-color:{bg};\"\
		""".format(fg=style["default"], bg=style["background"])

		html_lines.append(div)
		for line in code_lines:
			html_lines.append(self.convert_to_html(line, self.style, self.language, self.user_types))

		html_lines.append("</div>")

		return html_lines