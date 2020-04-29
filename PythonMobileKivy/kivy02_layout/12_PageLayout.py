from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''
PageLayout:
    Button:
        text:'pag1'
    Button:
        text:'pag2'
    Button:
        text:'pag3'

'''))
