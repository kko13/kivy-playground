import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Inherit GridLayout
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        # Call parent constructor
        super(MyGrid, self).__init__(**kwargs)
        # Set columns of grid
        self.cols = 2
        
        # Label and InputBox widgets for Username
        self.add_widget(Label(text="Username: "))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        # Label and InputBox widgets for Password
        self.add_widget(Label(text="Password: "))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        # Button widget for submit
        self.submit = Button(text="Submit", font_size=40)
        self.add_widget(self.submit)

# Inherit kivy App class
class MyApp(App):
    # Build kivy App
    def build(self):
        return MyGrid()
        # return Label(text="Hello Kivy")

if __name__ == "__main__":
    MyApp().run()