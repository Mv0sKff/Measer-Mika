from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.config import Config
from kivy.utils import platform
import cv2

Config.set('graphics', 'resizable', True)

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)

        # -1 is auto selection
        self.index = -1

    def changeCameraIndex(self):
        self.ids.camera_index_button.text = "Hello"
        self.ids.camera.index = 1
        #self.text = "Hello"

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