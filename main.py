import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

kv = Builder.load_file("my.kv")


class Widgets(Widget):
    pass


class DrawApp(App):
    def build(self):
        return kv
