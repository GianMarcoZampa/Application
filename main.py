
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from database import DataBase
from screens import LoginWindow, RegisterWindow, MainWindow

kv = Builder.load_file("draw.kv")
sm = ScreenManager()
db = DataBase("user.csv")

screens = [LoginWindow(name="login", database=db, screen_manager=sm),
           RegisterWindow(name="register", database=db, screen_manager=sm),
           MainWindow(name="main", database=db, screen_manager=sm)]
for screen in screens:
    sm.add_widget(screen)
sm.current = "login"


class DrawApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    DrawApp().run()
