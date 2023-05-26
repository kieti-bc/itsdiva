# Ohjelma joka muuttaa annetun koodin html muotoon jotta sen voi laittaa
# ItsLearning:ii
# 

import tkinter as tk

from styles.style_light import Style_Light
from styles.style_dark import Style_Dark
from languages.language_csharp import Language_Csharp
from languages.language_python import Language_Python
from parser import Parser

python = Language_Python()
csharp = Language_Csharp()

def select_python():
	label_selected_language["text"] = python.name
	
def select_csharp():
	label_selected_language["text"] = csharp.name

def select_style_light():
	label_selected_style["text"] = "Light"

def select_style_dark():
	label_selected_style["text"] = "Dark"

def get_language(name):
	match name:
		case python.name:
			return python
		case csharp.name:
			return csharp

def get_style(name):
	match name:
		case "Light":
			return Style_Light()
		case "Dark":
			return Style_Dark()

def convert():
	code = text_input.get("1.0", tk.END)
	code_lines = code.split("\n")
	text_output.delete("1.0", tk.END)

	user_types = []

	language = get_language(label_selected_language["text"])
	style = get_style(label_selected_style["text"])

	parser = Parser(code_lines, style.colors, language, user_types)
	html_lines = parser.create_html()

	for line in html_lines:
		text_output.insert(tk.END, line)

# Widgets
window = tk.Tk()
frame_language = tk.Frame(master=window)
label_language = tk.Label(text="Choose language", master=frame_language)
button_python = tk.Button(text="Python", command=select_python, master=frame_language)
button_csharp = tk.Button(text="C sharp", command=select_csharp, master=frame_language)
label_selected_language = tk.Label(text="csharp", master=frame_language)
frame_style = tk.Frame(master=window)
button_style_light = tk.Button(text="Light", command=select_style_light, master=frame_style)
button_style_dark = tk.Button(text="Dark", command=select_style_dark, master=frame_style)
label_selected_style = tk.Label(text="Light", master=frame_style)
label_input = tk.Label(text="Paste code here")
text_input = tk.Text()

# TODO: style selection widgets
button_convert = tk.Button(text="Convert", command=convert)
label_output = tk.Label(text="Generated html")
text_output = tk.Text()
# TODO: button to copy output to clipboard

def run_tkinter_window():
	# Create the window
	label_language.pack()
	button_python.pack(side=tk.LEFT)
	button_csharp.pack(side=tk.LEFT)
	label_selected_language.pack(side=tk.RIGHT)
	frame_language.pack()

	button_style_light.pack(side=tk.LEFT)
	button_style_dark.pack(side=tk.LEFT)
	label_selected_style.pack(side=tk.RIGHT)
	frame_style.pack()

	label_input.pack()
	text_input.pack()
	button_convert.pack()
	label_output.pack()
	text_output.pack()

	window.mainloop()
