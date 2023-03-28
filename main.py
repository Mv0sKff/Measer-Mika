from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from kivy.lang import Builder
from kivy.config import Config
from kivy.utils import platform
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.core.window import Window
import math
import os

Window.maximize()
if platform == "android":
    #from plyer import gyroscope
    from plyer import spatialorientation

Config.set('graphics', 'resizable', True)
hoeheInZentimeter = NumericProperty()

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
        
        hoeheInZentimeter = int(self.ids.input.text)
        return False

class SecondWindow(Screen):
    hinweis_label_text = StringProperty()
    schrittIndex = NumericProperty()

    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)

        self.addSchrittIndex()

    def addSchrittIndex(self):
        self.schrittIndex += 1
        self.indexChanged()
        print(self.schrittIndex, "(+1)")

    def returnSchrittIndex(self):
        self.schrittIndex -= 1
        self.indexChanged()
        print(self.schrittIndex, "(--)")

    def changeTippText(self):
        if self.schrittIndex == 1:
            self.hinweis_label_text = 'Halten Sie das Handy auf Kopfhöhe und\nzielen Sie mit dem Fadenkreuz auf den tiefsten\nPunkt des Objektes. Nehmen Sie dann ein Foto auf.'
        elif self.schrittIndex == 2:
            self.hinweis_label_text = 'Super, erstes Foto ist gemacht, wenn Sie\nden Vorgang wiederholen möchten, dann benutzen\nSie den Button links unten. Wenn alles\npasst, dann den Button rechts unten.'
        elif self.schrittIndex == 3:
            self.hinweis_label_text = 'Halten Sie das Handy wieder auf Kopfhöhe\nund zielen Sie mit dem Fadenkreuz auf den\nhöchsten Punkt des Objektes.'
        elif self.schrittIndex == 4:
            self.hinweis_label_text = 'Auch das ist geschafft, wenn Sie den Vorgang\nwiederholen möchten, dann benutzen Sie den\nButton links unten. Wenn alles passt,\ndann den Button rechts unten.'
        else:
            self.hinweis_label_text = ''

    def disableWidget(self, id: str, disable: bool):
        if disable:
            self.ids[id].disabled = True
            self.ids[id].opacity = 0
        else:
            self.ids[id].disabled = False
            self.ids[id].opacity = 100

    def indexChanged(self):
        if self.schrittIndex == 1:
            self.disableWidget('weiter_button', True)
            self.disableWidget('capture_button', False)
            self.ids['go_back_redo_image'].source = 'images/ReturnButton.png'
            self.ids['camera'].play = True
        elif self.schrittIndex == 2:
            self.disableWidget('weiter_button', False)
            self.disableWidget('capture_button', True)
            self.ids['go_back_redo_image'].source = 'images/RedoButton.png'
            self.ids['camera'].play = False
        elif self.schrittIndex == 3:
            self.disableWidget('weiter_button', True)
            self.disableWidget('capture_button', False)
        elif self.schrittIndex == 4:
            self.disableWidget('weiter_button', False)
            self.disableWidget('capture_button', True)
        elif self.schrittIndex == 5:
            self.disableWidget('weiter_button', True)
            self.disableWidget('capture_button', True)
            self.disableWidget('go_back_redo_image', True)
            pass
        self.changeTippText()

class ThirdWindow(Screen):
    def __init__(self, **kwargs):
        super(ThirdWindow, self).__init__(**kwargs)
        self.saveErgebnis()

    def saveErgebnis(self):
        dictionary = {
            "Höhe": 'entfernung',
            "Entfernung": 'höhe',
            }
        if platform == "android":
            from android.storage import primary_external_storage_path
            fname = os.path.join(primary_external_storage_path(),'/Download/ergebnisse.json')
            with open(fname, 'wb') as f:        
                f.write(dictionary)
            return fname
 

class FourthWindow(Screen):
    def __init__(self, **kwargs):
        super(FourthWindow, self).__init__(**kwargs)
        self.sensorEnabled = False

    def get_orientation(self, dt):
        try:
            val = spatialorientation.orientation
            pitchRaw = int(val[1] * 100)
            pitchAngle = int((val[1] + math.pi) * 100)

            self.ids.label1.text = "pitchRaw: " + str(pitchRaw)
            self.ids.label2.text = "pitchAngle: " + str(pitchAngle)
            self.ids.label3.text = "pitch: " + str(pitch) + "°"

            # b = distance
            b = int(150 * math.cos(pitchAngle))

            self.ids.distance.text = "distance: " + str(b) + " cm"

        except:
            print("error gyroscope.orientation")

    def pressed1(self):
        try:
            if not self.sensorEnabled:
                spatialorientation.enable_listener()
                Clock.schedule_interval(self.get_orientation, 1 / 20.)

                self.sensorEnabled = True
                self.ids.button1.text = "Stop"
            else:
                spatialorientation.disable_listener()
                Clock.unschedule(self.get_orientation)

                self.sensorEnabled = False
                self.ids.button1.text = "Start"
        except NotImplementedError:
            import traceback; traceback.print_exc()
            self.ids.status.text = "Gyroscope is not supported for your platform"

class WindowManager(ScreenManager):
    pass

class MeasureMikaApp(App):
    def build(self):
        self.icon = "images/icon.png"
        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([
                Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE
            ])
        
        app = ScreenManager()
        app.add_widget(MainWindow(name='main'))
        app.add_widget(SecondWindow(name='second'))
        app.add_widget(ThirdWindow(name='third'))
        app.add_widget(FourthWindow(name='fourth'))
        
        return app

if __name__ == "__main__":
    MeasureMikaApp().run()
