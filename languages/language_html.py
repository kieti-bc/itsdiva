from token_types import TokenType
from scanner_states import ScannerState

class Language_Html:

	# In html the tags can contain attributes, which can have strings as their values
	# Reserverd words are only reserved words if they are inside < > 
	# <p> html </p>  p is a reserved word, but html is not, because it is not inside brackets
	def scan_token(self, character, scanner):
		match character:
			case '<':
				if scanner.next_is('/'):
					scanner.add_token(TokenType.FUNCTION)
					scanner.set_state(ScannerState.HTML_TAG)
					return True
				if scanner.next_is('!'):
					# Comment or doctype
					# Comment is <!--text text text -->
					if scanner.next_is('-'):
						if scanner.next_is('-'):
							while scanner.peek() != '' and scanner.isAtEnd() == False:
								if scanner.peek_next(1) == '-' and scanner.peek_next(2) == '-' and scanner.peek_next(3) == '>':
									break
								scanner.advance()
							
							scanner.add_token(TokenType.COMMENT)
							return True
					elif scanner.peek() == 'D': # DOCTYPE?
						# Read until space
						# mark next word as keyword
						scanner.add_identifier_token()
						return True
			case '>':
				scanner.add_token(TokenType.KEYWORD)
				return True
						
		return False

	def is_user_type_keyword(self, word:str):
		return False

	user_type_keywords = []

	name = "Html"

	keywords = [
		"!DOCTYPE",
		"a",
		"abbr",
		"acronym",
		"address",
		"applet",
		"area",
		"article",
		"aside",
		"audio",
		"b",
		"base",
		"basefont",
		"bdi",
		"bdo",
		"big",
		"blockquote",
		"body",
		"br",
		"button",
		"canvas",
		"caption",
		"center",
		"cite",
		"code",
		"col",
		"colgroup",
		"data",
		"datalist",
		"dd",
		"del",
		"details",
		"dfn",
		"dialog",
		"dir",
		"div",
		"dl",
		"dt",
		"em",
		"embed",
		"fieldset",
		"figcaption",
		"figure",
		"font",
		"footer",
		"form",
		"frame",
		"frameset",
		"h1 - <h6>",
		"head",
		"header",
		"hr",
		"html",
		"i",
		"iframe",
		"img",
		"input",
		"ins",
		"kbd",
		"label",
		"legend",
		"li",
		"link",
		"main",
		"map",
		"mark",
		"meta",
		"meter",
		"nav",
		"noframes",
		"noscript",
		"object",
		"ol",
		"optgroup",
		"option",
		"output",
		"p",
		"param",
		"picture",
		"pre",
		"progress",
		"q",
		"rp",
		"rt",
		"ruby",
		"s",
		"samp",
		"script",
		"section",
		"select",
		"small",
		"source",
		"span",
		"strike",
		"strong",
		"style",
		"sub",
		"summary",
		"sup",
		"svg",
		"table",
		"tbody",
		"td",
		"template",
		"textarea",
		"tfoot",
		"th",
		"thead",
		"time",
		"title",
		"tr",
		"track",
		"tt",
		"u",
		"ul",
		"var",
		"video",
		"wbr",
	]

	primitive_types = []