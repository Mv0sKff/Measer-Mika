from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from kivy.lang import Builder
from kivy.config import Config
from kivy.utils import platform
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Config.set('graphics', 'resizable', True)

class MainWindow(Screen):
    def checkData(self):
        popup = Popup(title='Hinweis',
            size_hint=(None, None), size=(350, 100))    

        if self.ids.input.text == '':
            popup.content = Label(text='Bitte geben Sie zuerst Ihre Größe in cm an!')
            popup.open()
            return True
        if not self.ids.input.text.isdecimal():
            popup.content = Label(text='Bitte geben Sie einen Numerischen Wert an!')
            popup.open()
            return True
        return False

class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)

        # -1 is auto selection
        self.index = -1

    def changeCameraIndex(self):
        self.ids.camera_index_button.text = "Index 1"
        self.ids.camera.index = 1

class WindowManager(ScreenManager):
    pass

class MeasureMikaApp(App):
    def build(self):
        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([
                Permission.CAMERA
            ])
        
        app = ScreenManager()
        app.add_widget(MainWindow(name='main'))
        app.add_widget(SecondWindow(name='second'))
        
        return app

if __name__ == "__main__":
    MeasureMikaApp().run()