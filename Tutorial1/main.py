import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Inherit GridLayout
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        # Outer grid columns
        self.cols = 1

        # Declare inner grid and columns
        self.inner_grid = GridLayout()
        self.inner_grid.cols = 2
        # Add Username Label & Input widgets to inner grid
        self.inner_grid.add_widget(Label(text="Username: "))
        self.username = TextInput(multiline=False)
        self.inner_grid.add_widget(self.username)
        # Add Password Label & Input widgets to inner grid
        self.inner_grid.add_widget(Label(text="Password: "))
        self.password = TextInput(multiline=False, password=True)
        self.inner_grid.add_widget(self.password)

        # Add inner grid widget to outer grid
        self.add_widget(self.inner_grid)

        # Create submit button widget
        self.submit = Button(text="Submit", font_size=40)
        # Bind button press to pressed method
        self.submit.bind(on_press=self.pressed)
        # Add submit button widget to outer grid
        self.add_widget(self.submit)

    # Button action method
    def pressed(self, instance):
        # Capture text from input boxes
        username = self.username.text
        password = self.password.text
        # Clear input boxes
        self.username.text = ""
        self.password.text = ""

        print("Username: {}\nPassword: {}".format(username, password))


# Inherit kivy App class
class MyApp(App):
    # Build kivy App
    def build(self):
        return MyGrid()
        # return Label(text="Hello Kivy")

if __name__ == "__main__":
    MyApp().run()