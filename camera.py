from kivy.app import App
from kivy.lang import Builder
from kivy.core.camera import Camera

kv = """
BoxLayout:
	orientation: "vertical"
	Camera: 
		play: "False"
		id: camera
		resolution: (1920,1080)
	ToggleButton:
		text: "PLAY"
		size_hint_y: None
		height: "48dp"
		on_press: camera.play = not camera.play
"""
class NewApp(App):
	def build(self):
		return Builder.load_string(kv)

if __name__=="__main__":
	NewApp().run()
