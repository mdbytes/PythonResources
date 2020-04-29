from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.base import runTouchApp

# buttons appear in vertical stack - horizontal would be side by side
Builder.load_string("""
<BoxLayout>:
    orientation: 'vertical'
    Button:
        text: 'B1'
    Button:
        text: 'B2'
    Button:
        text: 'B3'

""")

class MyListView(BoxLayout):
    pass

if __name__== '__main__':
    runTouchApp(MyListView())
