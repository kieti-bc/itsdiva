from enum import Enum, auto 

# If scanner is in some other state than
# default.
# This state persists and is given
# to scanners until it is changed
class ScannerState(Enum):
	DEFAULT = "default"
	MULTI_LINE_COMMENT = "multiline_comment" # Comment is spanning multiple lines
	HTML_TAG = "html_tag" # The scanner is inside a html tag
