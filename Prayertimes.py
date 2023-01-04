import kivy
import aladhan
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.behaviors import TouchRippleBehavior
from kivy.uix.button import Button
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty


kv = """
Screen:
    in_class: text
    MDLabel:
        text: 'Prayer Times'
        text_color: (0,0.5,0.5)
        font_style: 'H2'
        pos_hint:{'center_x': 0.6,'center_y':0.91}
        theme_text_color: 'Custom'
    MDLabel:
        text:''
        id:city
        text_color: (0,0.5,0.5)
        font_style: 'H2'
        pos_hint:{'center_x': 0.6,'center_y':0.8}
        theme_text_color: 'Custom'


    MDLabel:
        text:''
        id : Fajr
        text_color: (0,0.5,0.5)
        font_style: 'H6'
        pos_hint:{'center_x': 0.5,'center_y':0.6}
        theme_text_color: 'Custom'

    MDLabel:
        text:''
        id : dhuhr
        text_color: (0,0.5,0.5)
        font_style: 'H6'
        pos_hint:{'center_x': 0.5,'center_y':0.48}
        theme_text_color: 'Custom'

    MDLabel:
        text: ''
        id : asr
        text_color: (0,0.5,0.5)
        font_style: 'H6'
        pos_hint:{'center_x': 0.5,'center_y':0.38}
        theme_text_color: 'Custom'

    MDLabel:
        text: ''
        id : maghrib
        text_color: (0,0.5,0.5)
        font_style: 'H6'
        pos_hint:{'center_x': 0.5,'center_y':0.28}
        theme_text_color: 'Custom'

    MDLabel:
        text: ''
        id : isha
        text_color: (0,0.5,0.5)
        font_style: 'H6'
        pos_hint:{'center_x': 0.5,'center_y':0.18}
        theme_text_color: 'Custom'

    
        

    MDTopAppBar:
        title : " "
        id : next

    MDTextField:
        id: text
        hint_text : 'Enter your City'
        pos_hint: {'center_x':0.48,'center_y':0.7}
        size_hint_x:None
        width:300
        required: True
    MDRaisedButton:
        text: 'Enter'
        pos_hint: {'center_x': 0.8, 'center_y':0.7}
        on_press:
            app.prayer()

"""


class Prayertime(MDApp):
    Window.size = (500,750)
    in_class = ObjectProperty(None)

    def build(self):
      return Builder.load_string(kv)
    
    def prayer(self):
        user = aladhan.Client()
        prayer_times = user.get_timings_by_address(f"{self.root.in_class.text}")
        next_prayer = user.get_next_prayer_by_address(address=f"{self.root.in_class.text}")
        prayer_list = list(prayer_times)
        flabel = self.root.ids.Fajr
        flabel.text = f"{prayer_list[1]}"
        dlabel = self.root.ids.dhuhr
        dlabel.text = f"{prayer_list[3]}"
        alabel = self.root.ids.asr
        alabel.text = f"{prayer_list[4]}"
        mlabel = self.root.ids.maghrib
        mlabel.text = f"{prayer_list[6]}"
        ilabel = self.root.ids.isha
        ilabel.text = f"{prayer_list[7]}"
        clabel = self.root.ids.city
        clabel.text = f"In {self.root.in_class.text}"
        nlabel = self.root.ids.next
        nlabel.title = f"Next Prayer:{next_prayer},Remaining:{next_prayer.remaining}"
    




Prayertime().run()
