from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''

StackLayout:
    Label:
        text:'S1'
'''))
