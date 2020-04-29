from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button
 
class Controller2(FloatLayout):
 
    def __init__(self, **kwargs):
        super(Controller2, self).__init__(**kwargs)
  
        b = Button(text='Button 1', font_size=20, pos_hint= {'x': .5, 'y':.6 }, size_hint=(.2,.2) )
        self.add_widget(b)
        b = Button(text='Button 2', font_size=20, pos_hint= {'x': .2, 'y':.3 }, size_hint=(.3,.3) )
        self.add_widget(b)
        b = Button(text='Button 3', font_size=10, pos_hint= {'x': .7, 'y':.8 }, size_hint=(.1,.1) )
        self.add_widget(b)

class Controller2App(App):
    def build(self):
        return Controller2()
 
if __name__ == '__main__':
    Controller2App().run()
