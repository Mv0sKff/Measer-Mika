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
from plyer.facades import Gyroscope
from plyer.platforms.android import activity
from jnius import PythonJavaClass, java_method, autoclass, cast

Context = autoclass('android.content.Context')
Sensor = autoclass('android.hardware.Sensor')
SensorManager = autoclass('android.hardware.SensorManager')

Config.set('graphics', 'resizable', True)

hoeheInZentimeter = NumericProperty()
winkel1 = NumericProperty()
winkel2 = NumericProperty()

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
    
def instance():
    return AndroidGyroscope()

class SecondWindow(Screen):
    hinweis_label_text = StringProperty()
    schrittIndex = NumericProperty()
    gyroscopeInstance = instance()

    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__(**kwargs)

        self.addSchrittIndex()
        self.setWeiterButtonVisibility(False)

    def addSchrittIndex(self):
        self.schrittIndex += 1
        self.indexChanged()

    def returnSchrittIndex(self):
        self.schrittIndex -= 1
        self.indexChanged()

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

    def setCameraCaptureButtonVisibility(self, visible):
        if visible:
            self.ids.capture_button.opacity = 100
            self.ids.capture_button.disabled: False
        else:
            self.ids.capture_button.opacity = 0
            self.ids.capture_button.disabled: True 

    def indexChanged(self):
        if self.schrittIndex == 2:
            self.setGoBackButtonVisibility(False)
            self.setWeiterButtonVisibility(True)
            self.setCameraCaptureButtonVisibility(False)
            orientation1 = self.gyroscopeInstance._get_orientation()
        if self.schrittIndex == 3:
            self.setWeiterButtonVisibility(False)
            self.setCameraCaptureButtonVisibility(True)
        if self.schrittIndex == 4:
            self.setWeiterButtonVisibility(True)
            self.setCameraCaptureButtonVisibility(False)
        #if self.schrittIndex >= 5:
            # Hier muss dann der 3. Bildschirm aufgerufen werden
        self.changeTippText()
        

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


class GyroscopeSensorListener(PythonJavaClass):
    __javainterfaces__ = ['android/hardware/SensorEventListener']

    def __init__(self):
        super().__init__()
        self.SensorManager = cast(
            'android.hardware.SensorManager',
            activity.getSystemService(Context.SENSOR_SERVICE)
        )
        self.sensor = self.SensorManager.getDefaultSensor(
            Sensor.TYPE_GYROSCOPE
        )

        self.values = [None, None, None]

    def enable(self):
        self.SensorManager.registerListener(
            self, self.sensor,
            SensorManager.SENSOR_DELAY_NORMAL
        )

    def disable(self):
        self.SensorManager.unregisterListener(self, self.sensor)

    @java_method('(Landroid/hardware/SensorEvent;)V')
    def onSensorChanged(self, event):
        self.values = event.values[:3]

class GyroUncalibratedSensorListener(PythonJavaClass):
    __javainterfaces__ = ['android/hardware/SensorEventListener']

    def __init__(self):
        super().__init__()
        service = activity.getSystemService(Context.SENSOR_SERVICE)
        self.SensorManager = cast('android.hardware.SensorManager', service)

        self.sensor = self.SensorManager.getDefaultSensor(
            Sensor.TYPE_GYROSCOPE_UNCALIBRATED)
        self.values = [None, None, None, None, None, None]

    def enable(self):
        self.SensorManager.registerListener(
            self, self.sensor,
            SensorManager.SENSOR_DELAY_NORMAL
        )

    def disable(self):
        self.SensorManager.unregisterListener(self, self.sensor)

    @java_method('(Landroid/hardware/SensorEvent;)V')
    def onSensorChanged(self, event):
        self.values = event.values[:6]

class AndroidGyroscope(Gyroscope):
    def __init__(self):
        super().__init__()
        self.bState = False

    def _enable(self):
        if (not self.bState):
            self.listenerg = GyroscopeSensorListener()
            self.listenergu = GyroUncalibratedSensorListener()
            self.listenerg.enable()
            self.listenergu.enable()
            self.bState = True

    def _disable(self):
        if (self.bState):
            self.bState = False
            self.listenerg.disable()
            self.listenergu.disable()
            del self.listenerg
            del self.listenergu

    def _get_orientation(self):
        if (self.bState):
            return tuple(self.listenerg.values)
        else:
            return (None, None, None)

    def _get_rotation_uncalib(self):
        if (self.bState):
            return tuple(self.listenergu.values)
        else:
            return (None, None, None, None, None, None)

    def __del__(self):
        if self.bState:
            self._disable()
        super().__del__()


