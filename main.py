#siehe https://www.youtube.com/watch?v=mEAjGChhwcs
# https://sounds-mp3.com/

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader

class MyGridLayout(GridLayout):
    def playSound(self,src):
        sounds = {'Hund':'sounds/dog_bark_01.mp3',
                  'Vogel':'sounds/birds_cardinal.mp3',
                  'Katze':'sounds/cat_meow_04.mp3',
                  'Kuh':'sounds/cows_two_cows_mooing.mp3',
                  'Esel':'sounds/donkey_braying.mp3',
                  'Schwein':'sounds/pig_grunt.mp3',
                  'Schaf':'sounds/sheep_bleat_001.mp3'
                  }
        
        b=SoundLoader.load(filename=sounds[src])
        b.play()
        

class MultimediaApp(App):
    def build(self):
        self.title = 'Multimedia App'
        return MyGridLayout()

if __name__ == "__main__":
    MultimediaApp().run()