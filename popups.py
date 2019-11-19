from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class NotificationPopup(Popup):
    def __init__(self, label, title, **kwargs):
        self.label = Label(text=label)
        self.button = Button(text="Ok", on_release=self.dismiss, size_hint=(0.28, 0.3))
        self.content = GridLayout(cols=1)
        self.content.add_widget(self.label)
        self.content.add_widget(self.button)
        super().__init__(title=title,
                         auto_dismiss=False,
                         size_hint=(0.3, 0.3),
                         content=self.content,
                         **kwargs)


class ChoosePopup(Popup):

    def __init__(self, label="", title="", **kwargs):
        self.answer = False
        self.label = Label(text=label)
        self.yes = Button(text="Yes", on_release=self.on_yes, size_hint=(0.28, 0.3))
        self.no = Button(text="No", on_release=self.on_no, size_hint=(0.28, 0.3))
        self.button_grid = GridLayout(cols=2, size_hint=(0.28, 0.3))
        self.button_grid.add_widget(self.yes)
        self.button_grid.add_widget(self.no)
        self.content = GridLayout(cols=1)
        self.content.add_widget(self.label)
        self.content.add_widget(self.button_grid)
        super().__init__(title=title,
                         content=self.content,
                         auto_dismiss=False,
                         size_hint=(0.3, 0.3),
                         **kwargs)

    def on_yes(self, instance):
        self.answer = True
        self.dismiss()

    def on_no(self, instance):
        self.answer = False
        self.dismiss()
