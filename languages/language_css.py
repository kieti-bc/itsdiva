from token_types import TokenType
from scanner_states import ScannerState

class Language_Css:
	"""
	CSS:
	- Kommentit: /* ... */
	- At-rules: @media, @import, @supports, ...
	- Rakennesymbolit: { } : ; (korostetaan kuten HTML:ssä < > )
	- Propertyt yms. hoidetaan listojen + "yleisskannerin" word-säännöillä
	"""

	def scan_token(self, character, scanner):
		match character:
			case '/':
				# CSS kommentti: /* ... */
				if scanner.next_is('*'):
					while scanner.peek() != '' and scanner.isAtEnd() == False:
						# loppu: */
						if scanner.peek() == '*' and scanner.peek_next(1) == '/':
							scanner.advance()  # '*'
							scanner.advance()  # '/'
							break
						scanner.advance()

					scanner.add_token(TokenType.COMMENT)
					return True

				return False

			case '{':
				scanner.set_state(ScannerState.DEFAULT)
				scanner.add_token(TokenType.FUNCTION)
				return True

			case '}':
				scanner.set_state(ScannerState.DEFAULT)
				scanner.add_token(TokenType.FUNCTION)
				return True

			case ':':
				scanner.add_token(TokenType.FUNCTION)
				return True

			case ';':
				scanner.add_token(TokenType.FUNCTION)
				return True

			case '@':
				# At-rule: @media, @import, @supports, ...
				while scanner.peek() != '' and scanner.isAtEnd() == False:
					ch = scanner.peek()
					if ch.isalnum() or ch == '-' or ch == '_':
						scanner.advance()
					else:
						break

				scanner.add_token(TokenType.KEYWORD)
				return True

			case '\t':
				return False

			case ' ':
				return False

			case _:
				return False

		return False

	def is_user_type_keyword(self, word: str):
		return False


	name = "Css"

	user_type_keywords = [
		"align-content",
		"align-items",
		"align-self",
		"all",
		"animation",
		"animation-delay",
		"animation-direction",
		"animation-duration",
		"animation-fill-mode",
		"animation-iteration-count",
		"animation-name",
		"animation-play-state",
		"animation-timing-function",
		"appearance",
		"backdrop-filter",
		"backface-visibility",
		"background",
		"background-attachment",
		"background-clip",
		"background-color",
		"background-image",
		"background-origin",
		"background-position",
		"background-repeat",
		"background-size",
		"border",
		"border-bottom",
		"border-bottom-color",
		"border-bottom-left-radius",
		"border-bottom-right-radius",
		"border-bottom-style",
		"border-bottom-width",
		"border-collapse",
		"border-color",
		"border-image",
		"border-left",
		"border-left-color",
		"border-left-style",
		"border-left-width",
		"border-radius",
		"border-right",
		"border-right-color",
		"border-right-style",
		"border-right-width",
		"border-spacing",
		"border-style",
		"border-top",
		"border-top-color",
		"border-top-left-radius",
		"border-top-right-radius",
		"border-top-style",
		"border-top-width",
		"border-width",
		"bottom",
		"box-shadow",
		"box-sizing",
		"caption-side",
		"caret-color",
		"clear",
		"clip-path",
		"color",
		"column-gap",
		"columns",
		"contain",
		"content",
		"cursor",
		"display",
		"filter",
		"flex",
		"flex-basis",
		"flex-direction",
		"flex-flow",
		"flex-grow",
		"flex-shrink",
		"flex-wrap",
		"float",
		"font",
		"font-family",
		"font-feature-settings",
		"font-kerning",
		"font-size",
		"font-style",
		"font-variant",
		"font-weight",
		"gap",
		"grid",
		"grid-area",
		"grid-auto-columns",
		"grid-auto-flow",
		"grid-auto-rows",
		"grid-column",
		"grid-column-end",
		"grid-column-start",
		"grid-row",
		"grid-row-end",
		"grid-row-start",
		"grid-template",
		"grid-template-areas",
		"grid-template-columns",
		"grid-template-rows",
		"height",
		"hyphens",
		"image-rendering",
		"inset",
		"isolation",
		"justify-content",
		"justify-items",
		"justify-self",
		"left",
		"letter-spacing",
		"line-height",
		"list-style",
		"list-style-position",
		"list-style-type",
		"margin",
		"margin-bottom",
		"margin-left",
		"margin-right",
		"margin-top",
		"max-height",
		"max-width",
		"min-height",
		"min-width",
		"object-fit",
		"object-position",
		"opacity",
		"order",
		"outline",
		"outline-color",
		"outline-offset",
		"outline-style",
		"outline-width",
		"overflow",
		"overflow-x",
		"overflow-y",
		"padding",
		"padding-bottom",
		"padding-left",
		"padding-right",
		"padding-top",
		"pointer-events",
		"position",
		"right",
		"rotate",
		"scale",
		"scroll-behavior",
		"tab-size",
		"text-align",
		"text-decoration",
		"text-decoration-color",
		"text-decoration-style",
		"text-decoration-thickness",
		"text-indent",
		"text-overflow",
		"text-shadow",
		"text-transform",
		"top",
		"transform",
		"transform-origin",
		"transform-style",
		"transition",
		"transition-delay",
		"transition-duration",
		"transition-property",
		"transition-timing-function",
		"translate",
		"unicode-bidi",
		"user-select",
		"vertical-align",
		"visibility",
		"white-space",
		"width",
		"word-break",
		"word-spacing",
		"word-wrap",
		"z-index",

		"--*",
    ]

	keywords = [
		"media",
		"import",
		"supports",
		"keyframes",
		"font-face",
		"layer",
		"container",
		"page",
		"namespace",
		"charset",
		"property",
	]

	primitive_types = [
		":root",
		":host",
		":host-context",
	]

	builtin_types = []
    