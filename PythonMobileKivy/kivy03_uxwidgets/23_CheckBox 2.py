from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''
GridLayout:
	cols:2
	CheckBox:
		active:False
	Label:
		text:'CheckBox 1'
	CheckBox:
		active:True
	Label:
		text:'CheckBox 2'

	CheckBox:
		group:"Radio Button"
		active:True
	Label:
		text:'Radio Button'



'''))

