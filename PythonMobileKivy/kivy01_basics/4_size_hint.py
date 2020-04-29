
from kivy.lang import Builder
from kivy.base import runTouchApp


runTouchApp(Builder.load_string("""
FloatLayout:
    Button:
        text: 'B1'
        size_hint_x: .3
        size_hint_y: .1
        pos_hint: {'right': 1 , 'down': 1}



"""))
