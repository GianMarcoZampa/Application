from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup


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
