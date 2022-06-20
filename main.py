import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager
import string

class Grid1(GridLayout):
    na = 0
    nk = 0
    def __init__(self, **kwargs):
        super(Grid1, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 5

        self.add_widget(Label(text="Adults"))
        self.add_widget(Label(text="Kids"))

        self.ANum = Button(text="+1")
        self.ANum.bind(on_press=self.POA)
        self.add_widget(self.ANum)

        self.KNum = Button(text="+1")
        self.KNum.bind(on_press=self.POK)
        self.add_widget(self.KNum)

        self.ANum5 = Button(text="+5")
        self.ANum5.bind(on_press=self.PFA)
        self.add_widget(self.ANum5)

        self.KNum5 = Button(text="+5")
        self.KNum5.bind(on_press=self.PFK)
        self.add_widget(self.KNum5)

        self.ANumN = Button(text="-1")
        self.ANumN.bind(on_press=self.MOA)
        self.add_widget(self.ANumN)

        self.KNumN = Button(text="-1")
        self.KNumN.bind(on_press=self.MOK)
        self.add_widget(self.KNumN)


        self.add_widget(Label(text="CLEAR ALL"))
        #CLEAR button
        self.CLEAR = Button(text="CLEAR")
        self.CLEAR.bind(on_press=self.Clear)
        self.add_widget(self.CLEAR)

    def POA(self, instance):
        Grid1.na += 1
        stna = str(Grid1.na)
        self.ANum.text = stna

    def PFA(self, instance):
        Grid1.na += 5
        stna = str(Grid1.na)
        self.ANum.text = stna

    def POK (self, instance):
        Grid1.nk += 1
        stna = str(Grid1.nk)
        self.KNum.text = stna

    def PFK (self, instance):
        Grid1.nk += 5
        stna = str(Grid1.nk)
        self.KNum.text = stna

    def MOA (self, instance):
        Grid1.na -= 1
        stna = str(Grid1.na)
        self.ANum.text = stna

    def MOK (self, instance):
        Grid1.nk -= 1
        stna = str(Grid1.nk)
        self.KNum.text = stna

    def Clear (self, instance):
        Grid1.na = 0
        Grid1.nk = 0
        stna = str(Grid1.na)
        stnk = str(Grid1.nk)
        self.ANum.text = stna
        self.KNum.text = stnk


class ClickerApp(App):
    def build (self):
        return Grid1()

if __name__ == "__main__":
    ClickerApp().run()
