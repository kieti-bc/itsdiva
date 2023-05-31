from token_types import TokenType

class Language_Html:

	def add_tag(scanner):
		while scanner.peek().isalpha() and scanner.isAtEnd() == False:
			if scanner.next_is('>'):
				break
			scanner.advance()

		scanner.add_token(TokenType.FUNCTION)

	def scan_token(self, character, scanner):
		match character:
			case '<':
				if scanner.peek().isalpha() or scanner.peek() == '/':
					Language_Html.add_tag(scanner)
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
						scanner.add_identifier_token()
						return True
			case '>':
				scanner.add_token(TokenType.KEYWORD)
				return True
						
		return False

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