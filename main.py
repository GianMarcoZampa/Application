import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

from database import DataBase

kv = Builder.load_file("draw.kv")
sm = ScreenManager()
db = DataBase("user.txt")


class DrawApp(App):
    def build(self):
        return kv
