# Ohjelma joka muuttaa annetun koodin html muotoon jotta sen voi laittaa
# ItsLearning:ii
# 

import tkinter as tk

from styles.style_light import colors
from languages.language_csharp import Language_Csharp
from languages.language_python import Language_Python
from parser import Parser

language = Language_Csharp()

def select_python():
	language = Language_Python()
	label_selected["text"] = "python"
	
def select_csharp():
	language = Language_Csharp()
	label_selected["text"] = "csharp"

def convert():
	code = text_input.get("1.0", tk.END)
	code_lines = code.split("\n")
	text_output.delete("1.0", tk.END)

	parser = Parser(code_lines, colors, language)
	html_lines = parser.create_html()

	for line in html_lines:
		text_output.insert(tk.END, line)

# Create the window
window = tk.Tk()
frame_language = tk.Frame(master=window)
label_language = tk.Label(text="Choose language", master=frame_language)
button_python = tk.Button(text="Python", command=select_python, master=frame_language)
button_csharp = tk.Button(text="C sharp", command=select_csharp, master=frame_language)
label_selected = tk.Label(text=language, master=frame_language)
label_input = tk.Label(text="Paste code here")
text_input = tk.Text()

# TODO: style selection widgets
button_convert = tk.Button(text="Convert", command=convert)
label_output = tk.Label(text="Generated html")
text_output = tk.Text()
# TODO: button to copy output to clipboard

label_language.pack()
button_python.pack(side=tk.LEFT)
button_csharp.pack(side=tk.LEFT)
label_selected.pack(side=tk.LEFT)
frame_language.pack()

label_input.pack()
text_input.pack()
button_convert.pack()
label_output.pack()
text_output.pack()
window.mainloop()
