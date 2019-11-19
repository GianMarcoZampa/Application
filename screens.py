from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from widgets import BackgroundWidget, DrawWidget

from popups import NotificationPopup, ChoosePopup


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
            pop = NotificationPopup(label="Invalid email or password", title="Invalid login")
            pop.open()

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
                pop = NotificationPopup(label="Email already registered", title="Invalid Registration")
                pop.open()
        else:
            self.repeated_password.text = ""
            pop = NotificationPopup(label="Check password spelling", title="Invalid Registration")
            pop.open()

    def sign_in(self):
        self.email.text = ""
        self.password.text = ""
        self.repeated_password.text = ""
        self.nickname.text = ""
        self.sm.current = "login"


class MainWindow(Screen):
    current_user = ObjectProperty(None)
    r = ObjectProperty(None)
    g = ObjectProperty(None)
    b = ObjectProperty(None)
    a = ObjectProperty(None)
    brush_size = ObjectProperty(None)
    draw = ObjectProperty(None)

    def __init__(self, database, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.db = database
        self.sm = screen_manager

    def set_current_user(self):
        print(self.db.current_user)
        self.current_user.text = "Welcome, " + self.db.get(self.db.current_user)[0] + "!"

    def wait_logout(self):
        pop = ChoosePopup(label="Do you really want to logout?", title="Logout", on_dismiss=self.logout)
        pop.open()

    def logout(self, instance):
        if instance.answer:
            self.r.text = "0"
            self.g.text = "0"
            self.b.text = "0"
            self.a.text = "1"
            self.brush_size.text = "10"
            self.sm.current = "login"

    def change_color(self):
        self.draw.change_color(self.r.text, self.g.text, self.b.text, self.a.text)

    def change_size(self):
        self.draw.change_size(self.brush_size.text)
