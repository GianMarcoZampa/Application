from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from database import DataBase


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def __init__(self, database, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.db = database
        self.sm = screen_manager

    def sign_in(self):
        print(self.email.text, self.password.text)
        if self.db.validate(email=self.email.text, password=self.password.text):
            self.email.text = ""
            self.password.text = ""
            self.sm.current = "main"
        else:
            self.email.text = ""
            self.password.text = ""
            pop = InvalidLoginPopUp()
            pop.popup.open()

    def sign_up(self):
        self.email.text = ""
        self.password.text = ""
        self.sm.current = "register"


class RegisterWindow(Screen):
    email = ObjectProperty(None)
    nickname: ObjectProperty(None)
    password = ObjectProperty(None)
    repeated_password = ObjectProperty(None)

    def __init__(self, database, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.db = database
        self.sm = screen_manager

    def sign_up(self):
        if self.password.text == self.repeated_password.text:
            if self.db.add(self.email.text, self.nickname.text, self.password.text):
                self.email.text = ""
                self.nickname.text = ""
                self.password.text = ""
                self.repeated_password.text = ""
                self.sm.current = "login"
            else:
                self.email.text = ""
                self.nickname.text = ""
                self.password.text = ""
                self.repeated_password.text = ""
                pop = InvalidRegistrationPopUp(label_text="Email already registered")
                pop.popup.open()
        else:
            self.repeated_password.text = ""
            pop = InvalidRegistrationPopUp(label_text="Check password spelling")
            pop.popup.open()


class MainWindow(Screen):
    pass


class InvalidLoginPopUp:
    def __init__(self, **kwargs):
        self.label = Label(text="Invalid email or password")
        self.button = Button(text="OK", size_hint=(0.28, 0.3))
        self.grid = GridLayout(cols=1)
        self.grid.add_widget(self.label)
        self.grid.add_widget(self.button)
        self.popup = Popup(title="Invalid login",
                           auto_dismiss=False,
                           size_hint=(0.3, 0.3),
                           content=self.grid
                           )
        self.button.bind(on_release=self.popup.dismiss)


class InvalidRegistrationPopUp:
    def __init__(self, label_text, **kwargs):
        self.label = Label(text=label_text)
        self.button = Button(text="OK", size_hint=(0.28, 0.3))
        self.grid = GridLayout(cols=1)
        self.grid.add_widget(self.label)
        self.grid.add_widget(self.button)
        self.popup = Popup(title="Invalid Registration",
                           auto_dismiss=False,
                           size_hint=(0.3, 0.3),
                           content=self.grid
                           )
        self.button.bind(on_release=self.popup.dismiss)
