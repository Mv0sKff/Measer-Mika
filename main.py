#siehe https://www.youtube.com/watch?v=mEAjGChhwcs
# https://sounds-mp3.com/

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader

class MyGridLayout(GridLayout):
    pass
        

class MultimediaApp(App):
    def build(self):
        self.title = 'Multimedia App'
        return MyGridLayout()

if __name__ == "__main__":
    MultimediaApp().run()