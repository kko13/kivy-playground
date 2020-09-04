import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def btn(self):
        print("Username: {}\nPassword: {}".format(self.username.text, self.password.text))
        # Clear input boxes
        self.username.text = ""
        self.password.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()