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
            self.hinweis_label_text = 'Halten Sie das Handy auf Kopfhöhe und\nzielen Sie mit dem Fadenkreutz auf den tiefsten\nPunkt des Objektes. Nehmen Sie dann ein Foto auf.'
        elif self.schrittIndex == 2:
            self.hinweis_label_text = 'Super, erstes Foto ist gemacht, wenn Sie\nden Vorgang wiederholen möchten, dann benutzen\nSie den Button links unten. Wenn alles\npasst, dann den Button rechts unten.'
        elif self.schrittIndex == 3:
            self.hinweis_label_text = 'Halten Sie das Handy wieder auf Kopfhöhe\nund zielen Sie mit dem Fadenkreutz auf den\nhöchsten Punkt des Objektes.'
        elif self.schrittIndex == 4:
            self.hinweis_label_text = 'Auch das ist geschaft, wenn Sie den Vorgang\nwiederholen möchten, dann benutzen Sie den\nButton links unten. Wenn alles passt,\ndann den Button rechts unten.'
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
        match self.schrittIndex:
            case 1:
                self.disableWidget('go_back_button', False)
                self.disableWidget('weiter_button', True)
                self.disableWidget('capture_button', False)
                self.createRedoButton(False)
                self.ids['camera'].play = True
                return
            case 2:
                self.disableWidget('go_back_button', True)
                self.disableWidget('weiter_button', False)
                self.disableWidget('capture_button', True)
                self.createRedoButton(True)
                self.ids['camera'].play = False
                return
            case 3:
                self.disableWidget('weiter_button', True)
                self.disableWidget('capture_button', False)
                return
            case 4:
                self.disableWidget('weiter_button', False)
                self.disableWidget('capture_button', True)
                return
            case 5:
                # Hier muss dann der 3. Bildschirm aufgerufen werden
                return
        self.changeTippText()
    
    def createRedoButton(self, create: bool = True):
        if create:
            print("create redoButton")
            newWidget = Builder.load_string('''
Button:
	id: redo_button
	size_hint: (None, None)
	pos_hint: {"center_x":0.2, "center_y":0.1}
    on_release:
        app.root.children[0].returnSchrittIndex()
	background_color: 0, 0, 0, 0
	Image:
		id: redo_image
		source: 'images/RedoButton.png'
		center_x: self.parent.center_x
		center_y: self.parent.center_y
''')
            self.add_widget(newWidget)
        else:
            # does not work
            print("try remove redoButton")
            if 'redo_button' in self.ids:
                print("remove redoButton")
                self.remove_widget('redo_button')

class ThirdWindow(Screen):
    pass

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
        app.add_widget(ThirdWindow(name='third'))
        
        return app

if __name__ == "__main__":
    MeasureMikaApp().run()


