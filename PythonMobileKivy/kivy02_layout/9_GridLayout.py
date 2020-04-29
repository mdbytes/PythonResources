from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
GridLayout:
    cols:2
    rows:2
    size_hint_x:1
    size_hint_y:1
    
    Button:
        text:'hello'
        width:.5
    Button:
        text:'world'
        width:.5
    Button:
        text:'hello'
        width:.5
    Button:
        text:'world'
        width:.5




'''))


