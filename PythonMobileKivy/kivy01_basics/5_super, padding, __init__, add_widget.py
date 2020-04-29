
 
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
 
class Controller2(BoxLayout):
 
    def __init__(self, **kwargs):
        super(Controller2, self).__init__(**kwargs)
 
        self.padding = 100

        button = Button(text='button')
        self.add_widget(button)
 
class Controller2App(App):
    def build(self):
        return Controller2()
 
if __name__ == '__main__':
    Controller2App().run()
