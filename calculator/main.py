from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class TombolAngka(Button):
    def __init__(self, kalkulator, **kwargs):
        super().__init__(**kwargs)
        self.kalkulator = kalkulator
        self.font_size = 28
    def on_press(self):
        self.kalkulator.tambah(self.text)
    
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layar = Label(text='0', font_size=40, size_hint=(1, 0.3))
        grid = GridLayout(cols=3, spacing=6)
        tombol_tombol = [
            '7', '8', '9', 
            '4', '5', '6', 
            '1', '2', '3', 
            '0', 
        ]
        for text in tombol_tombol:
            grid.add_widget(TombolAngka(kalkulator=self, text=text))

        layout = BoxLayout(orientation='vertical', padding=8, spacing=8)
        layout.add_widget(self.layar)
        layout.add_widget(grid)
        self.add_widget(layout)

    def tambah(self, karakter):
        if self.layar.text == '0':
            self.layar.text = karakter
        else:
            self.layar.text += karakter

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

app = MyApp()
app.run()