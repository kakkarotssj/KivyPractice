from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_string("""
<WorkLayouts>:
	rows: 2
	cols: 3
	FloatLayout:
		Button:
			text: "F1"
			font_size: 32
			size_hint: .2,.2
			pos: 0,0
	RelativeLayout:
		Button:
			text: "R1"
			size_hint: .2,.2
			pos_hint: {"x":0,"y":0}
			font_size: 32
	GridLayout:
		rows: 2
		cols: 2
		spacing: 10
		Button:	
			text: "G1"
			size_hint: .2,.5
			font_size: 32
		Button:
			text: "G2"
			size_hint: .8,.5
			font_size: 32
		Button:
			text: "G3"
			size_hint: .2,.5
			font_size: 32
	AnchorLayout:
		anchor_x: "right"
		anchor_y: "top"
		Button:
			text: "A1"
			size_hint: .5,.5
			font_size: 32
		Button:
			text: "A2"
			size_hint: .2,.2
			font_size: 32
	BoxLayout:
		orientation: "horizontal"
		Button:
			size_hint:.25,1
			text: "B1"
			font_size: 32
		Button:
			size_hint: .5,.25
			pos_hint: {"x":.25,"y":.4}
			text: "B2"
			font_size: 32
		Button:
			size_hint: .25,1
			text: "B3"
			font_size: 32
	StackLayout:
		orientation: "rl-tb"
		padding: 10
		Button:
			text: "S1"
			size_hint: .7,.25
			font_size: 32
		Button:
			text: "S2"
			size_hint: .2,.4
			font_size: 32
		Button:
			text: "S3"
			size_hint: .2,.2
			font_size: 32
		Button:
			text: "S4"
			size_hint: .4,.4
			font_size: 32
	""")

class WorkLayouts(GridLayout):
	pass

class NewApp(App):
	def build(self):
		return WorkLayouts()

if __name__ == "__main__":
	NewApp().run()