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
from languages.language_javascript import Language_Javascript
from languages.language_html import Language_Html
from parser import Parser

# Try to load pyclip, which gives the ability to copy
# output directly to windows clipboard.

pyclip_available = False

try:
	import pyclip
	pyclip_available = True
except (ImportError):
	pass

languages = [
	Language_Python(),
	Language_Csharp(),
	Language_Javascript(),
	Language_Html()
	]


def handle_language_select(event):
	dropdown_language.selection_clear()

def handle_style_select(event):
	dropdown_style.select_clear()

def get_language(name):
	for language in languages:
		if language.name == name:
			return language

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

	if pyclip_available:
		full_output = ""
		for line in html_lines:
			full_output += line
		pyclip.copy(full_output)
		label_pyclip["text"] = "Copied to clipboard"
	else:
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
window.title("ItsDiva")
frame_language = tk.Frame(master=window)

label_language = tk.Label(text="Choose language", master=frame_language)

dropdown_language = ttk.Combobox(master=frame_language)
language_names = []
for l in languages:
	language_names.append(l.name)

dropdown_language["values"] = language_names
dropdown_language.set(language_names[0])
dropdown_language.state(["readonly"])
dropdown_language.bind("<<ComboboxSelected>>", handle_language_select)

frame_style = tk.Frame(master=window)
label_style = tk.Label(text="Choose style", master=frame_style)
button_style = tk.Button(text="Reload styles", master=frame_style)
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
button_convert = tk.Button(text="Convert", command=convert, background="Coral")
label_output = tk.Label(text="Generated html")
text_output = tk.Text(height=12, wrap='word')


label_pyclip = tk.Label(text="Install module pyclip to be able to copy directly to clipboard")

# TODO: button to copy output to clipboard
if pyclip_available:
	text_input["height"] = 24
	button_convert["text"] = "Convert and copy to clipboard"
	label_pyclip["text"] = ""

def run_tkinter_window():
	# Create the window
	label_language.pack(side=tk.LEFT)
	dropdown_language.pack(side=tk.RIGHT)
	frame_language.pack()

	label_style.pack(side=tk.LEFT)
	dropdown_style.pack(side=tk.LEFT)
	button_style.pack(side=tk.RIGHT)
	frame_style.pack()

	label_input.pack()
	text_input.pack()
	button_convert.pack()

	if pyclip_available == False:
		label_output.pack()
		text_output.pack()

	label_pyclip.pack()

	window.mainloop()
