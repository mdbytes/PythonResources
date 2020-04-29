from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

# default orientation is horizontal
runTouchApp(Builder.load_string('''

FloatLayout:
    Button:
        text: 'F1'
        size_hint: (0.25 , 0.25)
        
        pos:(20, 20)
        pos_hint:{'x':.1, 'y':.2}
    
    Button:
        text: 'F2'
        size_hint: (0.25 , 0.25)
        
        pos:(60, 20)
        pos_hint:{'x':.6, 'y':.2}
'''))

