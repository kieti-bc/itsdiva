# Ohjelma joka muuttaa annetun koodin html muotoon jotta sen voi laittaa
# ItsLearning:ii
# 

import tkinter as tk
import tkinter.ttk as ttk

import json
import os
# File wildcards
import glob

from languages.language_csharp import Language_Csharp
from languages.language_python import Language_Python
from parser import Parser

python = Language_Python()
csharp = Language_Csharp()


def handle_language_select(event):
	dropdown_language.selection_clear()

def handle_style_select(event):
	dropdown_style.select_clear()

def get_language(name):
	match name:
		case python.name:
			return python
		case csharp.name:
			return csharp

def get_style(name):
	for style in styles:
		if style["name"] == name:
			return style 

def convert():
	code = text_input.get("1.0", tk.END)
	code_lines = code.split("\n")
	text_output.delete("1.0", tk.END)

	user_types = []

	language = get_language(dropdown_language.get())
	style = get_style(dropdown_style.get())

	parser = Parser(code_lines, style, language, user_types)
	html_lines = parser.create_html()

	for line in html_lines:
		text_output.insert(tk.END, line)


def read_style_json(filename) -> dict:
	style_dic = {}
	with open(filename, encoding="utf-8") as f:
		read_data = f.read()
		style_dic = json.loads(read_data)

	return style_dic

def read_style_files():
	styles = []
	os.chdir('styles')
	style_files = glob.glob("*.json")
	for f in style_files:
		styles.append(read_style_json(f))
	return styles

styles = read_style_files()

# Widgets
window = tk.Tk()
frame_language = tk.Frame(master=window)

label_language = tk.Label(text="Choose language", master=frame_language)

dropdown_language = ttk.Combobox(master=frame_language)
dropdown_language["values"] = (csharp.name, python.name)
dropdown_language.set(csharp.name)
dropdown_language.state(["readonly"])
dropdown_language.bind("<<ComboboxSelected>>", handle_language_select)

frame_style = tk.Frame(master=window)
label_style = tk.Label(text="Choose style", master=frame_style)
dropdown_style = ttk.Combobox(master=frame_style)

# Read styles from styles/ folder
style_names = []
for s in styles:
	style_names.append(s["name"])

dropdown_style["values"] = style_names
dropdown_style.set(style_names[0])
dropdown_style.state(["readonly"])
dropdown_style.bind("<<ComboboxSelected>>", handle_style_select)

label_input = tk.Label(text="Paste code here")
text_input = tk.Text(height=12, wrap='word')

# TODO: style selection widgets
button_convert = tk.Button(text="Convert", command=convert)
label_output = tk.Label(text="Generated html")
text_output = tk.Text(height=12, wrap='word')
# TODO: button to copy output to clipboard

def run_tkinter_window():
	# Create the window
	label_language.pack(side=tk.LEFT)
	dropdown_language.pack(side=tk.RIGHT)
	frame_language.pack()

	label_style.pack(side=tk.LEFT)
	dropdown_style.pack(side=tk.RIGHT)
	frame_style.pack()

	label_input.pack()
	text_input.pack()
	button_convert.pack()
	label_output.pack()
	text_output.pack()

	window.mainloop()
