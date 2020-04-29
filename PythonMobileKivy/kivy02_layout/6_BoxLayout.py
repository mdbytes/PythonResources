from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''

BoxLayout:
	orientation: 'vertical'
	spacing: 10
	padding: 50
	Label:
	    text: 'Box Layout'
	Button:
		text: 'B1'
	Button:
		text:'B2'


'''))
