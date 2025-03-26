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
from languages.language_sql import Language_SQL
from diva_parser import Parser
from text_styler import TextStyler, get_default_font

# Try to load pyclip, which gives the ability to copy
# output directly to windows clipboard.
pyclip_available = False

try:
	import pyclip
	pyclip_available = True
except (ImportError):
	pass

class ItsDivaGUI:

	def __init__(self, window):
		window.title("ItsDiva")

		self.languages = [
			Language_Python(),
			Language_Csharp(),
			Language_Javascript(),
			Language_Html(),
			Language_SQL()
			]
		language_names = []
		for l in self.languages:
			language_names.append(l.name)

		# Left and right
		frame_top = tk.Frame(master=window)
		frame_bottom = tk.Frame(master=window)

		# Language and Style
		self.language_name = tk.StringVar(value=language_names[0])
		frame_language = tk.Frame(master=frame_top)
		label_language = tk.Label(text="Choose language", master=frame_language)
		self.dropdown_language = ttk.Combobox(master=frame_language, textvariable=self.language_name)
		self.dropdown_language["values"] = language_names
		self.dropdown_language.state(["readonly"])
		self.dropdown_language.bind("<<ComboboxSelected>>", self.handle_language_select)

		# Style selection
		self.styles = []
		self.read_style_files()
		self.style_names = []
		for s in self.styles:
			self.style_names.append(s["name"])

		initial_style = "Light"
		if initial_style not in self.style_names:
			initial_style = self.style_names[0]

		self.style_name = tk.StringVar(value=initial_style)
		label_style = tk.Label(text="Choose style", master=frame_language)
		button_style = tk.Button(text="Reload styles", master=frame_language, command=self.reload_styles)
		self.dropdown_style = ttk.Combobox(master=frame_language, textvariable=self.style_name)
		self.dropdown_style["values"] = self.style_names
		self.dropdown_style.state(["readonly"])
		self.dropdown_style.bind("<<ComboboxSelected>>", self.handle_style_select)


		# Line numbers, text size and tab width
		self.use_line_numbers = tk.BooleanVar(value=False)
		self.first_line_number = tk.StringVar(value="1")
		frame_line_numbers = tk.Frame(master=frame_top)
		check_line_numbers = ttk.Checkbutton(master=frame_line_numbers, text="Line numbers", onvalue=True, offvalue=False, variable=self.use_line_numbers)
		label_first_line = tk.Label(master=frame_line_numbers, text="Start from:")
		entry_first_line = tk.Entry(master=frame_line_numbers, textvariable=self.first_line_number)

		self.tab_width = tk.IntVar(value = 2)
		label_tab_width = tk.Label(master= frame_line_numbers, text="Tab width")
		entry_tab_width = tk.Spinbox(master=frame_line_numbers, textvariable=self.tab_width, from_=1, to=8, increment=1)

		# Other settings
		label_text_size = tk.Label(master=frame_line_numbers, text="Text size in em")
		self.text_size = tk.DoubleVar(value=1.0)
		spinner_text_size = ttk.Spinbox(master=frame_line_numbers, textvariable=self.text_size, from_=1.0, to=3.0, increment=0.1)

		# User types
		frame_user_types = tk.Frame(master=frame_top)
		self.user_types = tk.StringVar(value="")
		label_user_types = tk.Label(master=frame_user_types, text="Space separated list of user types")
		self.user_types_input = tk.Entry(master=frame_user_types, textvariable=self.user_types);

		# Input text area
		label_input = tk.Label(master=frame_bottom, text="Paste code here")
		self.text_input = tk.Text(master=frame_bottom, height=12, wrap='word')
		self.text_input["font"] = get_default_font()

		button_convert = tk.Button(master=frame_bottom, text="Convert", command=self.convert, background="Coral")
		label_output = tk.Label(master=frame_bottom, text="Generated html")
		self.text_output = tk.Text(master=frame_bottom, height=12, wrap='word')

		self.label_pyclip = tk.Label(master=frame_bottom, text="Install module pyclip to be able to copy directly to clipboard")

		if pyclip_available:
			self.text_input["height"] = 24
			button_convert["text"] = "Convert and copy to clipboard"
			self.label_pyclip["text"] = ""

		# Layout
		label_language.pack(side=tk.LEFT, expand=True)
		self.dropdown_language.pack(side=tk.LEFT, expand=True)

		label_style.pack(side=tk.LEFT)
		self.dropdown_style.pack(side=tk.LEFT)
		button_style.pack(side=tk.LEFT)
		frame_language.pack(expand=True, fill=tk.X)

		check_line_numbers.pack(side=tk.LEFT)
		label_first_line.pack(side=tk.LEFT)
		entry_first_line.pack(side=tk.LEFT)

		label_text_size.pack(side=tk.LEFT)
		spinner_text_size.pack(side=tk.LEFT)

		label_tab_width.pack(side=tk.LEFT)
		entry_tab_width.pack(side=tk.LEFT)
		frame_line_numbers.pack(expand=True, fill=tk.X)

		label_user_types.pack(side=tk.LEFT)
		self.user_types_input.pack(side=tk.LEFT, expand=True, fill=tk.X)

		frame_user_types.pack(expand=True, fill=tk.X)

		frame_top.pack()


		# Input and output

		label_input.pack()
		self.text_input.pack()
		button_convert.pack()

		frame_bottom.pack()


		if pyclip_available == False:
			label_output.pack()
			self.text_output.pack()

		self.label_pyclip.pack()

	def reload_styles(self):
		self.read_style_files()

	def handle_language_select(self, event):
		self.dropdown_language.selection_clear()

	def handle_style_select(self, event):
		self.dropdown_style.select_clear()

	def get_language(self):
		for language in self.languages:
			if language.name == self.language_name.get():
				return language

	def get_style(self):
		for style in self.styles:
			if style["name"] == self.style_name.get():
				return style 

	def convert(self):
		code = self.text_input.get("1.0", tk.END)
		code_lines = code.split("\n")
		self.text_output.delete("1.0", tk.END)

		# Get the user types
		user_types = self.user_types_input.get().split(' ')
		# Trim 
		for utype in user_types:
			utype = utype.strip()

		language = self.get_language()
		style = self.get_style()
		


		first_line_number = 1
		try:
			first = int(self.first_line_number.get())
			first_line_number = max(0, first)
		except ValueError:
			pass
		except tk.TclError:
			pass

		text_size = 1.0
		try:
			text_size = float(self.text_size.get())
		except ValueError:
			pass
		except tk.TclError:
			pass

		tab_width_int = 2
		try:
			tab_width_int = int(self.tab_width.get())
		except ValueError:
			pass
		except tk.TclError:
			pass

		parser = Parser(code_lines, style, language, user_types, self.use_line_numbers.get(), first_line_number, text_size, tab_width_int)

		html_lines = parser.create_html()

		# Apply style to text area
		styler = TextStyler()
		styler.apply_style_to_text(self.text_input, style)
		styler.apply_text_size(self.text_input, text_size)
		self.text_input.delete("1.0", tk.END)
		parser.print_to_text_widget(styler, self.text_input)

		if pyclip_available:
			full_output = ""
			for line in html_lines:
				full_output += line
			pyclip.copy(full_output)
			self.label_pyclip["text"] = "Copied to clipboard"
		else:
			for line in html_lines:
				self.text_output.insert(tk.END, line)


	def read_style_json(self, filename) -> dict:
		style_dic = {}
		with open(filename, encoding="utf-8") as f:
			read_data = f.read()
			style_dic = json.loads(read_data)

		return style_dic

	def read_style_files(self):
		self.styles = []
		try:
			os.chdir('styles')
			style_files = glob.glob("*.json")
			for f in style_files:
				self.styles.append(self.read_style_json(f))
			os.chdir('..')
		except FileNotFoundError:
			pass

def run_tkinter_window():
	# Create the window
	window = tk.Tk()
	ItsDivaGUI(window)
	window.mainloop()
