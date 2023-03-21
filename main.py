from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.config import Config
from kivy.utils import platform

Config.set('graphics', 'resizable', True)

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    def __init__(self):
        # -1 is auto selection
        self.index = -1

    def returnCameraIndexes():
        index = 0
        arr = []
        while True:
            cap = cv2.VideoCapture(index)
            if not cap.read()[0]:
                break
            else:
                arr.append(index)
            cap.release()
            index += 1
        return arr

    def changeCameraIndex(self, *args):
        self.camera_index_button.text = "Hello"

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