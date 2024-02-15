from token_types import TokenType
from scanner_states import ScannerState

class Language_Html:

	# In html the tags can contain attributes, which can have strings as their values
	# Reserverd words are only reserved words if they are inside < > 
	# <p> html </p>  p is a reserved word, but html is not, because it is not inside brackets
	# Color these as FUNCTION: < > </
	def scan_token(self, character, scanner):
		match character:
			case '<':
				# Inside <  > 
				scanner.set_state(ScannerState.DEFAULT)
				print("Scanner inside html tag")
				# Tag starts or ends
				if scanner.next_is('/'):
					# End tag
					scanner.add_token(TokenType.FUNCTION)
					return True
				elif scanner.next_is('!'):
					# Comment or doctype
					# Comment is <!--text text text -->
					if scanner.next_is('-'):
						if scanner.next_is('-'):
							while scanner.peek() != '' and scanner.isAtEnd() == False:
								if scanner.peek_next(1) == '-' and scanner.peek_next(2) == '-' and scanner.peek_next(3) == '>':
									# The comment ends, consume 3 characters and break
									scanner.advance()
									scanner.advance()
									scanner.advance()
									break
								scanner.advance()
							
							scanner.add_token(TokenType.COMMENT)
							return True
					# doctype is <!DOCTYPE html>
					elif scanner.peek() == 'D': 
						scanner.add_token(TokenType.FUNCTION)
						return True;
				else:
					scanner.add_token(TokenType.FUNCTION)
					return True
			case '>':
				scanner.add_token(TokenType.FUNCTION)
				# Tag ends: everything is text until next <
				scanner.set_state(ScannerState.HTML_TAG)
				print("Scanner outside html tag")
				return True
			# Dont read tabs and whitespace as text even when they are inside html tag
			case '\t':
				return False
			case ' ':
				return False
			case _:
				if scanner.get_state() == ScannerState.HTML_TAG:
					# Everything is text until next tag begins
					while scanner.peek() != '<' and scanner.isAtEnd() == False:
						scanner.advance()
					scanner.add_token(TokenType.TEXT)
					return True
				else:
					# Inside tag brackets, follow general rules
					return False
						
		return False

	def is_user_type_keyword(self, word:str):
		return False

	# Put attributes here
	user_type_keywords = [
		"accept",
		"accept-charset",
		"accesskey",
		"action",
		"align",
		"alt",
		"async",
		"autocomplete",
		"autofocus",
		"autoplay",
		"bgcolor",
		"border",
		"charset",
		"checked",
		"cite",
		"class",
		"color",
		"cols",
		"colspan",
		"content",
		"contenteditable",
		"controls",
		"coords",
		"data",
		"data-*",
		"datetime",
		"default",
		"defer",
		"dir",
		"dirname",
		"disabled",
		"download",
		"draggable",
		"enctype",
		"enterkeyhint",
		"for",
		"form",
		"formaction",
		"headers",
		"height",
		"hidden",
		"high",
		"href",
		"hreflang",
		"http-equiv",
		"id",
		"inert",
		"inputmode",
		"ismap",
		"kind",
		"label",
		"lang",
		"list",
		"loop",
		"low",
		"max",
		"maxlength",
		"media",
		"method",
		"min",
		"multiple",
		"muted",
		"name",
		"novalidate",
		"onabort",
		"onafterprint",
		"onbeforeprint",
		"onbeforeunload",
		"onblur",
		"oncanplay",
		"oncanplaythrough",
		"onchange",
		"onclick",
		"oncontextmenu",
		"oncopy",
		"oncuechange",
		"oncut",
		"ondblclick",
		"ondrag",
		"ondragend",
		"ondragenter",
		"ondragleave",
		"ondragover",
		"ondragstart",
		"ondrop",
		"ondurationchange",
		"onemptied",
		"onended",
		"onerror",
		"onfocus",
		"onhashchange",
		"oninput",
		"oninvalid",
		"onkeydown",
		"onkeypress",
		"onkeyup",
		"onload",
		"onloadeddata",
		"onloadedmetadata",
		"onloadstart",
		"onmousedown",
		"onmousemove",
		"onmouseout",
		"onmouseover",
		"onmouseup",
		"onmousewheel",
		"onoffline",
		"ononline",
		"onpagehide",
		"onpageshow",
		"onpaste",
		"onpause",
		"onplay",
		"onplaying",
		"onpopstate",
		"onprogress",
		"onratechange",
		"onreset",
		"onresize",
		"onscroll",
		"onsearch",
		"onseeked",
		"onseeking",
		"onselect",
		"onstalled",
		"onstorage",
		"onsubmit",
		"onsuspend",
		"ontimeupdate",
		"ontoggle",
		"onunload",
		"onvolumechange",
		"onwaiting",
		"onwheel",
		"open",
		"optimum",
		"pattern",
		"placeholder",
		"popover",
		"popovertarget",
		"popovertargetaction",
		"poster",
		"preload",
		"readonly",
		"rel",
		"required",
		"reversed",
		"rows",
		"rowspan",
		"sandbox",
		"scope",
		"selected",
		"shape",
		"size",
		"sizes",
		"span",
		"spellcheck",
		"src",
		"srcdoc",
		"srclang",
		"srcset",
		"start",
		"step",
		"style",
		"tabindex",
		"target",
		"title",
		"translate",
		"type",
		"usemap",
		"value",
		"width",
		"wrap",
	]

	name = "Html"

	keywords = [
		"DOCTYPE",
		"a",
		"abbr",
		"acronym", # Deprecated
		"address",
		"applet", # Deprecated
		"area",
		"aside",
		"audio",
		"b",
		"base",
		"basefont",
		"bdi",
		"bdo",
		"big", # Deprecated
		"blockquote",
		"br",
		"button",
		"canvas",
		"caption",
		"center", # Deprecated
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
		"dl",
		"dt",
		"em",
		"embed",
		"fieldset",
		"figcaption",
		"figure",
		"font",
		"form",
		"frame",
		"frameset",
		"hr",
		"i",
		"iframe",
		"img",
		"input",
		"ins",
		"kbd",
		"label",
		"legend",
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
		"optgroup",
		"option",
		"output",
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
		"var",
		"video",
		"wbr",
	]

	# Move page layout tags here instead
	primitive_types = [
		"article",
		"body",
		"div",
		"footer",
		"h1",
		"h2",
		"h3",
		"h4",
		"h5",
		"h6",
		"head",
		"header",
		"html",
		"li",
		"ol",
		"p",
		"ul",
	]