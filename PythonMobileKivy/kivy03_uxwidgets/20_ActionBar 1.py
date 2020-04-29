from kivy.base import runTouchApp
from kivy.lang import Builder
runTouchApp(Builder.load_string('''
ActionBar:
    pos_hint:{'top': 1}

    ActionView:
        ActionPrevious:
            title:'Action Bar'
            with_previous:False

        ActionButton:
            text:'Bt1'
        ActionButton:
            text:'Bt1'
        ActionButton:
            text:'Bt1'
        ActionButton:
            text:'Bt1'
















'''))

