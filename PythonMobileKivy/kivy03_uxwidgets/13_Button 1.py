from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''

Label:
    Button:
        text:'Hello'
        font_size:30
        color:.9,.8,0,1
        size:100,100
        pos:50 , 300
    Button:
        text:'World'
        font_size:15
        color:.3,.8,0,1
        size:50,100
        pos:150 , 300
'''))
