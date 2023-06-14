from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label





from kivy.core.window import Window
Window.clearcolor = (21/255, 19/255, 60/255, 1)

"""Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1000')"""

class RPSLS(App):
    pass



class BoxLayoutExample(BoxLayout):
    txtInput = StringProperty()

    def onTextValidate(self, widget):
        self.txtInput = widget.text

    def onButtonAClick(self):
        import play
        play.run(self.txtInput)
        pass
    pass


RPSLS().run()






