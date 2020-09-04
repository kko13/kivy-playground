from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Login screen
class MainWindow(Screen):
    pass

# Landing screen
class SecondWindow(Screen):
    pass

# Screen manager
class WindowManager(ScreenManager):
    pass

# Build from whatever kv file specified
kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
