from enum import Enum, auto 

class ScannerState(Enum):
	"""If scanner is in some other state than default. This state persists when set in scanner"""
	DEFAULT = "default"
	MULTI_LINE_COMMENT = "multiline_comment" # Comment is spanning multiple lines
	HTML_TAG = "html_tag" # The scanner is inside a html tag
