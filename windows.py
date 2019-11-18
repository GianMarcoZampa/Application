from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from widgets import BackgroundWidget

from popups import InvalidRegistrationPopUp, InvalidLoginPopUp


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

    def sign_in(self):
        self.email.text = ""
        self.password.text = ""
        self.repeated_password.text = ""
        self.nickname.text = ""
        self.sm.current = "login"


class MainWindow(Screen):
    current_user = ObjectProperty(None)

    def __init__(self, database, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.db = database
        self.sm = screen_manager

    def set_current_user(self):
        self.current_user.text = self.db.get(self.db.current_user)[1]


