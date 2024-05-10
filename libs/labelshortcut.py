from libs.utils import generate_color_by_text

class LabelShortcut:
	def __init__(self,items):
		self.items=items
		self.selection=None
		print("items")
		print(self.items)

	def onPress(self,item,key):
		if(key==48):
			index=9
		else:
			index= key-49
		text=self.items[index]
		item.setText(text)
		item.setBackground(generate_color_by_text(text))
