from kivy.app import App
from kivy.lang import Builder


kv = """
AnchorLayout:
	canvas:
		Color:
			rgb:1,1,3
		Rectangle:
			pos:self.pos
			size:self.size
	AsyncImage:
		size_hint:None, None
		size: dp(500), dp(500)
		source:'https://bdo-tech.com/wp-content/uploads/2018/01/new_logo_cropped_transparent_v1.png'
		anim_delay: 0.3
"""


class TestApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    TestApp().run()
