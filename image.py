from kivy.app import App
from kivy.core.image import Image
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget 

Builder.load_string('''
<FaaduLayout>:
	orientation: "vertical"
	Image:
		pos:root.width-butt.height, root.height-butt.height
		source: "abc.png"
	BoxLayout:
		orientation: "horizontal"
		Button:
			text: "PREVIOUS"
			size_hint: (None, None)
			size_hint_x: .33
			size_hint_y: .33
			id: butt_prev
		Button:
			text: "CLOSE IT"
			size_hint: (None, None)
			size_hint_x: .33
			size_hint_y: .33 
			id: butt
			on_release: App.on_stop()
		Button:
			text: "NEXT"
			size_hint: (None, None)
			size_hint_x: .33
			size_hint_y: .33
			id: butt_next
	''')

class FaaduLayout(BoxLayout):
	pass

class NewestApp(App):
	def build(self):
		return FaaduLayout()

if __name__ == "__main__":
	NewestApp().run()