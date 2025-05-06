# This file contains functions to apply a style to a Python text widget

import tkinter as tk
from token_types import Token, TokenType
from tkinter.font import Font

# Way to iterate over enum
import inspect

def get_default_font():
	default = tk.font.nametofont("TkFixedFont")
	default.config(size = 12)
	return default

def get_fancy_font(bold: bool, italic: bool):
	fancy = Font(font="TkFixedFont")
	if (bold):
		fancy.config(weight="bold")
	if (italic):
		fancy.config(slant="italic")
	return fancy

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
				# Find out if this tag defines only a color or more complex style
				value = style[tag_name]
				text_color = "black"
				bg_color = "white"
				styledFont = get_default_font()
				# TkFixedFont
				# font . weight : bold 
				# font . slant : italic
				if type(value) == str:
					text_color = value	
					bg_color = style["background"]
				elif type(value) == dict:
					text_color = value["color"]
					if "switch_colors" in value and value["switch_colors"] == "True":
						bg_color = value["color"]
						text_color = style["foreground"]
					else:
						text_color = value["color"]
						bg_color = style["background"]
					
					bold = "weight" in value and value["weight"] == "bold"
					slanted = "style" in value and value["style"] == "italic"
					styledFont = get_fancy_font(bold, slanted)
				
				text_widget.tag_configure(tag_name, background = bg_color)
				text_widget.tag_configure(tag_name, foreground = text_color)
				text_widget.tag_configure(tag_name, font = styledFont)

	def apply_text_size(self, text_widget:object, em_size:float):
		myFont = get_default_font()
		myFont.config(size = int(12.0 * em_size))
		text_widget["font"] = myFont

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
