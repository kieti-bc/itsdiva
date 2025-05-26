# Returns a complex style definition
# style can be just the color name as string or a dictionary
# if tag is empty or invalid, will use styles foreground color only
class tag_style:
	def __init__(self, style:dict, tag:str):
		params = ""
		if tag in style:
			params = style[tag]
		else:
			params = style["foreground"]

		if type(params) == str:
			self.text_color = params
			self.bg_color = style["background"]
			self.bold = False
			self.slanted = False
			self.switch_colors = False
		elif type(params) == dict:
			self.text_color = params["color"]
			if "switch_colors" in params and params["switch_colors"] == "True":
				self.switch_colors = True
				self.text_color = style["foreground"]
				self.bg_color = params["color"]
			else:
				self.switch_colors = False
				self.text_color = params["color"]
				self.bg_color = style["background"]
		
			self.bold = "weight" in params and params["weight"] == "bold"
			self.slanted = "style" in params and params["style"] == "italic"
