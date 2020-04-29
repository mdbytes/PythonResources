
 
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
 

 
class Controller2App(App):
    def build(self):
        return Label(text='[color=ff3333]Hello[/color][color=3333ff][b]World[/b][/color]',
		markup = True,
        font_size='60sp')
 		#Label(text='Hello [b]World[/b]', markup=True)
if __name__ == '__main__':
    Controller2App().run()
