import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# Inherit GridLayout
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        # Call parent constructor
        super(MyGrid, self).__init__(**kwargs)
        # Set columns of grid
        self.cols = 2
        
        # Specify/add widgets
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

# Inherit kivy App class
class MyApp(App):
    # Build kivy App
    def build(self):
        return MyGrid()
        # return Label(text="Hello Kivy")

if __name__ == "__main__":
    MyApp().run()