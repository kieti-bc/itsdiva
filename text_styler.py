# This file contains functions to apply a style to a Python text widget

import tkinter as tk
from token_types import Token, TokenType

# Way to iterate over enum
import inspect

def iter_enum(enumName, list):
	for member in enumName:  
		if inspect.isclass(member.value) and issubclass(member.value, enum.Enum):
			iter_enum(member.value)
		else:
			list.append(member.value)

	return list


class TextStyler:
	# Configure the tags
	def apply_style_to_text(self, text_widget:object, style:dict):
		text_widget["background"] = style["background"]
		text_widget["foreground"] = style["foreground"]
		classNames = []
		iter_enum(TokenType, classNames)
		for name in classNames:
			tag_name = name
			if tag_name in style:
				# NOTE does not take hex values, only names
				text_widget.tag_configure(tag_name, foreground  = style[tag_name])
		pass

	# inserts text to widget and applies the correct tag
	# based on the tokenType
	def insert_stylized_text(self, text_widget:object, style:dict, token:object):
		tagName = token.type.value # class name in style
		if tagName in style:
			text_widget.insert(tk.END, token.text, tagName)
		else:
			text_widget.insert(tk.END, token.text)
		
	def insert_new_line(self, text_widget:object):
		text_widget.insert(tk.END, '\n')
