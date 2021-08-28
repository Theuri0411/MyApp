import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Label)