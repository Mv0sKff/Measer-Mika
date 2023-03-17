from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MeasureMikaApp(App):
    pass

if __name__ == "__main__":
    MeasureMikaApp().run()