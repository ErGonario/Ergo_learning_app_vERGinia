from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.config import Config

Config.set('graphics', 'Resizable','0')
Config.set('graphics', 'width', '412')
Config.set('graphics', 'height', '732')

#Compilare ogni informazione per le risposte
#Scambiare bottone indietro con istruzioni per ogni domanda
#Link ergotutorials
#link Ergodocs


class HomePage(Screen):
    pass

class Presentation(Screen):
    pass 
class Q1(Screen):
    pass
class I1(Screen):
    pass
class Q2(Screen):
    pass
class I2(Screen):
    pass
class Q3(Screen):
    pass
class I3(Screen):
    pass
class Q4(Screen):
    pass
class I4(Screen):
    pass
class Q5(Screen):
    pass
class I5(Screen):
    pass
class Score (Screen):
    pass
class FinalPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

file=Builder.load_file('kivy.kv')

class ErgoLearningApp(App):
    def build(self):
        return file

ErgoLearningApp().run()