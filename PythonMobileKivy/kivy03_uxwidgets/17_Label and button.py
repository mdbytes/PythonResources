from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''
BoxLayout:
    orientation:'vertical'
    size_hint_y:None
    height: sp(500)
    Label:
        text:'Hallo world'
    Button:
        text:'stuodent'

'''))
