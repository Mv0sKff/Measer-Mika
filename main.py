from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from kivy.lang import Builder
from kivy.config import Config
from kivy.utils import platform
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.properties import NumericProperty

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
    hinweis_label_text = StringProperty()
    schrittIndex = NumericProperty()

    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)

        self.addSchrittIndex()
        self.changeTippText()
        self.setWeiterButtonVisibility(False)

    def addSchrittIndex(self):
        self.schrittIndex += 1

    def returnSchrittIndex(self):
        self.schrittIndex -= 1

    def changeTippText(self):
        if self.schrittIndex == 1:
            self.hinweis_label_text = 'Halten Sie das Handy auf Kopfhöhe und\nzielen Sie mit dem Fadenkreutz auf den tiefsten\nPunkt des Objektes. Nehmen Sie dann ein Foto auf.'
        elif self.schrittIndex == 2:
            self.hinweis_label_text = 'Super, erstes Foto ist gemacht, wenn Sie\nden Vorgang wiederholen möchten, dann benutzen\nSie den Button links unten. Wenn alles\npasst, dann den Button rechts unten.'
        elif self.schrittIndex == 3:
            self.hinweis_label_text = 'Halten Sie das Handy wieder auf Kopfhöhe\nund zielen Sie mit dem Fadenkreutz auf den\nhöchsten Punkt des Objektes.'
        elif self.schrittIndex == 4:
            self.hinweis_label_text = 'Auch das ist geschaft, wenn Sie den Vorgang\nwiederholen möchten, dann benutzen Sie den\nButton links unten. Wenn alles passt,\ndann den Button rechts unten.'

    def setGoBackButtonVisibility(self, visible):
        if visible:
            self.ids.go_back_button.opacity = 100
            self.ids.go_back_button.disabled: False
        else:
            self.ids.go_back_button.opacity = 0
            self.ids.go_back_button.disabled: True

    def setWeiterButtonVisibility(self, visible):
        if visible:
            self.ids.weiter_button.opacity = 100
            self.ids.weiter_button.disabled: False
        else:
            self.ids.weiter_button.opacity = 0
            self.ids.weiter_button.disabled: True  

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