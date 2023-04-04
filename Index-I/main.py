import json
import re
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.tab import MDTabsBase


kv = """
<Home>:
    name:'main'
        
    MDLabel:
        text: 'INDEX-I'
        # md_bg_color: "#3f38f5"
        halign: 'center'
        font_size: '80sp'
        font_name: 'CONSOLAB.TTF'
    MDIconButton:
        icon: "distribute-horizontal-center"
        icon_size: '34sp'
        md_bg_color: '#3f38f5'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press: 
            root.manager.current = 'currencies'
            root.manager.transition.direction = "left"
            
    MDLabel:
        text: "REMEMBER TO ALWAYS BE HUMBLE!!"
        halign: "center"
        pos_hint: {'center_y': 0.1}
        font_size: 18
        font_name: 'CONSOLAB.TTF'

<Currencies>:
    name:'currencies'
    MDScreen:
        MDTopAppBar:
            title: "INDEX-I"
            pos_hint: {"top": 1}    
            md_bg_color: "#060459"
            left_action_items: [["menu", lambda x: nav_drawer.set_state('open')]]
            right_action_items: 
                [
                ['arrow-left-bold', lambda x: app.set_screen('main')],
                ['calculator', lambda x: app.cal_screen('calc')],
                ]

        MDFloatingActionButton:
            icon: "android"
            opacity: 0.2
            md_bg_color: app.theme_cls.primary_color
            font_size: '94sp'
            pos_hint: {"center_x": .5, "center_y": .5}

        MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                MDTextButton:
                    text: "NASDAQ100"
                    font_name: 'CONSOLAB.TTF'
                    opacity: 0.5
                    custom_color: "white"
                    font_size: '34dp'
                    pos_hint: {"center_x": .5, "center_y": .85}
                MDTextField:
                    id:op
                    font_name: 'CONSOLAB.TTF'
                    hint_text: "Open"
                    mode: "line"
                    pos_hint: {"center_x": .5, "center_y": .75}
                    size_hint_x: 0.8
                MDTextField:
                    id: vol
                    font_name: 'CONSOLAB.TTF'
                    hint_text: "Volume"
                    mode: "line"
                    pos_hint: {"center_x": .5, "center_y": .65}
                    size_hint_x: 0.8
                MDTextField:
                    id:lo
                    font_name: 'CONSOLAB.TTF'
                    hint_text: "Low"
                    mode: "line"
                    pos_hint: {"center_x": .5, "center_y": .55}
                    size_hint_x: 0.8
                MDTextField:
                    id: hig
                    font_name: 'CONSOLAB.TTF'
                    hint_text: "High"
                    mode: "line"
                    pos_hint: {"center_x": .5, "center_y": .45}
                    size_hint_x: 0.8

                MDRaisedButton:
                    text: "SUBMIT"
                    font_name: 'CONSOLAB.TTF'
                    md_bg_color: '#3f38f5'
                    pos_hint: {"center_x": .5, "center_y": .35}
                    on_release:  
                        app.my_func()

                MDCard:
                    size_hint: None, None
                    size: "325dp", "170dp"
                    pos_hint: {"center_x": .5, "center_y": .18}
                    radius: (0, 0, 0, 0)
                    styles: "filled"

                    MDLabel:
                        text: ""
                        font_name: 'CONSOLAB.TTF'
                        id: put_txt_here
                        halign: 'center'
                        pos_hint: {"center_x": .5, "center_y": .5}
                

                        
            MDScreen:
                name: "scr 2"

                MDTextButton:
                    text: "US30"
                    font_name: 'CONSOLAB.TTF'
                    opacity: 0.5
                    custom_color: "white"
                    font_size: '34dp'
                    pos_hint: {"center_x": .5, "center_y": .85}
                MDTextField:
                    id: open_30
                    font_name: 'CONSOLAB.TTF'
                    hint_text: "Open"
                    mode: "line"
                    pos_hint: {"center_x": .5, "center_y": .75}
                    size_hint_x: 0.8
                MDTextField:
                    id: volume_30
                    font_name: 'CONSOLAB.TTF'
                    hint_text: "Volume"
                    mode: "line"
                    pos_hint: {"center_x": .5, "center_y": .65}
                    size_hint_x: 0.8
                MDTextField:
                    id: low_30
                    font_name: 'CONSOLAB.TTF'
                    hint_text: "Low"
                    mode: "line"
                    pos_hint: {"center_x": .5, "center_y": .55}
                    size_hint_x: 0.8
                MDTextField:
                    id: high_30
                    font_name: 'CONSOLAB.TTF'
                    hint_text: "High"
                    mode: "line"
                    pos_hint: {"center_x": .5, "center_y": .45}
                    size_hint_x: 0.8

                MDRaisedButton:
                    text: "SUBMIT"
                    font_name: 'CONSOLAB.TTF'
                    md_bg_color: '#d91e1e'
                    pos_hint: {"center_x": .5, "center_y": .35}
                    on_release:  
                        app.my_us30()

                MDCard:
                    size_hint: None, None
                    size: "325dp", "170dp"
                    pos_hint: {"center_x": .5, "center_y": .18}
                    radius: (0, 0, 0, 0)
                    styles: "filled"
                    MDLabel:
                        text: ""
                        font_name: 'CONSOLAB.TTF'
                        id: put_us30
                        halign: 'center'
                        pos_hint: {"center_x": .5, "center_y": .5}
    
            MDScreen:
                name: "scr 3"

                MDTextButton:
                    text: "GER30"
                    font_name: 'CONSOLAB.TTF'
                    opacity: 0.5
                    custom_color: "white"
                    font_size: '34dp'
                    pos_hint: {"center_x": .5, "center_y": .85}
                MDTextField:
                    id:open_40
                    font_name: 'CONSOLAB.TTF'
                    hint_text: "Open"
                    mode: "line"
                    pos_hint: {"center_x": .5, "center_y": .75}
                    size_hint_x: 0.8
                MDTextField:
                    id: volume_40
                    font_name: 'CONSOLAB.TTF'
                    hint_text: "Volume"
                    mode: "line"
                    pos_hint: {"center_x": .5, "center_y": .65}
                    size_hint_x: 0.8
                MDTextField:
                    id:low_40
                    font_name: 'CONSOLAB.TTF'
                    hint_text: "Low"
                    mode: "line"
                    pos_hint: {"center_x": .5, "center_y": .55}
                    size_hint_x: 0.8
                MDTextField:
                    id: high_40
                    font_name: 'CONSOLAB.TTF'
                    hint_text: "High"
                    mode: "line"
                    pos_hint: {"center_x": .5, "center_y": .45}
                    size_hint_x: 0.8

                MDRaisedButton:
                    text: "SUBMIT"
                    font_name: 'CONSOLAB.TTF'
                    md_bg_color: '#1c5e30'
                    pos_hint: {"center_x": .5, "center_y": .35}
                    on_release:  
                        app.my_ger30()

                MDCard:
                    size_hint: None, None
                    size: "325dp", "170dp"
                    pos_hint: {"center_x": .5, "center_y": .18}
                    radius: (0, 0, 0, 0)
                    styles: "filled"
                    MDLabel:
                        text: ""
                        font_name: 'CONSOLAB.TTF'
                        id: put_ger30
                        halign: 'center'
                        pos_hint: {"center_x": .5, "center_y": .5}
                        
            MDScreen:
                name: "scr 4"
                MDCard:
                    orientation: "vertical"
                    padding: "8dp"
                    size_hint: None, None
                    size: "380dp", "115dp"
                    pos_hint: {"center_x": .5, "center_y": .81}
                    line_color: 'black'
            
                    MDLabel:
                        text: "NAS100 Information"
                        font_name: 'CONSOLAB.TTF'
                        theme_text_color: "Secondary"
                        size_hint_y: None
                        height: self.texture_size[1]
                                        
                    MDSeparator:
                        height: "1dp"
            
                    MDLabel:
                        text: ""
                        id: nas100_info
                        halign: 'center'
                        font_name: 'CONSOLAB.TTF'
                MDRaisedButton:
                    text: "GET"
                    font_name: 'CONSOLAB.TTF'
                    pos_hint: {"center_x": .5, "center_y": .68}
                    # md_bg_color: "black"
                    size_hint_x: 0.5
                    on_release:  
                        app.nasdaq()
                    
                MDCard:
                    orientation: "vertical"
                    padding: "8dp"
                    size_hint: None, None
                    size: "380dp", "115dp"
                    pos_hint: {"center_x": .5, "center_y": .55}
                    line_color: 'black'
            
                    MDLabel:
                        text: "US30 Information"
                        font_name: 'CONSOLAB.TTF'
                        theme_text_color: "Secondary"
                        size_hint_y: None
                        height: self.texture_size[1]
                                        
                    MDSeparator:
                        height: "1dp"
            
                    MDLabel:
                        text: ""
                        id: dowjones_info
                        halign: 'center'
                        font_name: 'CONSOLAB.TTF'
                MDRaisedButton:
                    text: "GET"
                    font_name: 'CONSOLAB.TTF'
                    pos_hint: {"center_x": .5, "center_y": .42}
                    # md_bg_color: "black"
                    size_hint_x: 0.5
                    on_release:
                        app.dowjones()
                    
                MDCard:
                    orientation: "vertical"
                    padding: "8dp"
                    size_hint: None, None
                    size: "380dp", "115dp"
                    pos_hint: {"center_x": .5, "center_y": .28}
                    line_color: 'black'
            
                    MDLabel:
                        text: "GER30 Information"
                        font_name: 'CONSOLAB.TTF'
                        theme_text_color: "Secondary"
                        size_hint_y: None
                        height: self.texture_size[1]
                                        
                    MDSeparator:
                        height: "1dp"
            
                    MDLabel:
                        text: ""
                        id: german40_info
                        halign: 'center'
                        font_name: 'CONSOLAB.TTF'
                MDRaisedButton:
                    text: "GET"
                    font_name: 'CONSOLAB.TTF'
                    pos_hint: {"center_x": .5, "center_y": .15}
                    # md_bg_color: "black"
                    size_hint_x: 0.5
                    on_release:
                        app.german40()
                    
                



        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 0, 0, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
<Tab>:
    MDLabel:
        id: label
        halign: "center"

<ContentNavigationDrawer>

    MDList:
        MDNavigationDrawerHeader:
            title: "Main Menu"
            font_name: 'CONSOLAB.TTF'

        OneLineListItem:
            text: "NAS100"
            font_name: 'CONSOLAB.TTF'
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 1"
                root.screen_manager.transition.direction = "down"

        OneLineListItem:
            text: "US30"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"
                
        OneLineListItem:
            text: "GER30"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 3"
        OneLineListItem:
            text: 'PRICE INFO'
            on_press:
                root.nav_drawer.set_state('close')
                root.screen_manager.current = 'scr 4'
                
<PipScreen>:
    name: 'calc'
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "Pip Calculator"
            md_bg_color: '#191f59'
            pos_hint: {'top': 1}
        MDTextField:
            id: input_dt
            halign: "right"
            valign: "bottom"
            font_size: 32
            mode: "line"
            pos_hint: {"center_x": .5, "center_y": .70}
            size_hint: 1, 0.4
            
        MDGridLayout:
            cols: 4
            rows: 5
            padding: 15
            size: root.width, root.height
            MDFlatButton:
                id: C
                text: "%"
                font_size: 30
                size: 500, 200
                # md_bg_color: 1, 0, 0, 1
                size_hint: 1, 1
                on_press:
                    root.signs('%')
                
            MDFlatButton:
                id: C
                text: "C"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.clear()
                
            MDFlatButton:
                id: C
                text: u"\u00AB"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                # md_bg_color: 214/255, 43/255, 43/255
                on_press:
                    root.remove_last()
            
            MDFlatButton:
                id: C
                text: "/"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                md_bg_color: '#191f59'
                on_press:
                    root.signs('/')
                md_bg_radius: 0
                
            MDFlatButton:
                id: C
                text: "7"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(7)
            
            MDFlatButton:
                id: C
                text: "8"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(8)
                
            MDFlatButton:
                id: C
                text: "9"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(9)
            
            MDFlatButton:
                id: C
                text: "x"
                md_bg_color: '#191f59'
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                md_bg_radius: -1
                on_press:
                    root.signs('*')
                            
            MDFlatButton:
                id: C
                text: "4"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(4)
            
            MDFlatButton:
                id: C
                text: "5"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(5)
            MDFlatButton:
                text: "6"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(6)
            
            MDFlatButton:
                id: C
                text: "-"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                md_bg_color: '#191f59'
                md_bg_radius: 0
                on_press:
                    root.signs('-')
                
            MDFlatButton:
                text: "1"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(1)
            
            MDFlatButton:
                id: C
                text: "2"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(2)
            MDFlatButton:
                id: C
                text: "3"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(3)
            
            MDFlatButton:
                id: C
                text: "+"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                md_bg_color: '#191f59'
                on_press:
                    root.signs('+')
                
            MDFlatButton:
                id: C
                text: "+/-"
                font_size: 30
                md_bg_color: '#7f8780'
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.pos_neg()
            
            MDFlatButton:
                id: C
                text: "0"
                font_size: 30
                size: 200, 200
                size_hint: 1, 1
                on_press: 
                    root.bt_values(0)
            MDFlatButton:
                id: C
                text: "."
                font_size: 30
                size: 200, 200
                md_bg_color: '#7f8780'
                size_hint: 1, 1
                on_press:
                    root.dot()
            
            MDFlatButton:
                id: C
                text: "="
                font_size: 30
                md_bg_color: '#257a30'
                size: 200, 200
                size_hint: 1, 1
                on_press:
                    root.results()
                
                
            
        MDIconButton:
            icon: "keyboard-backspace"
            icon_size: "40"
            pos_hint: {"center_x": .1, "center_y": .1}
            on_press:
                root.manager.current = 'currencies'
                root.manager.transition.direction = "right"

"""


class Home(Screen):
    pass

class Tab(MDFloatLayout, MDTabsBase):
    pass

class Currencies(Screen):
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <main.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''
    # def symbols(self):
        # self.manager.get_screen('currencies').ids.text.text = f'Hello Teddy'
        # print("Hello Thabang")


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class PipScreen(Screen):
    def clear(self):
        self.ids.input_dt.text = '0'

    def bt_values(self, number):
        prev_number = self.ids.input_dt.text
        if 'Input Error Buddy' in prev_number:
            prev_number = ''
        if prev_number == '0':
            self.ids.input_dt.text = ''
            self.ids.input_dt.text = f'{number}'
        else:
            self.ids.input_dt.text = f'{prev_number}{number}'

    def signs(self, sing):
        prev_number = self.ids.input_dt.text
        self.ids.input_dt.text = f'{prev_number}{sing}'

    def remove_last(self):
        prev_number = self.ids.input_dt.text
        prev_number = prev_number[:-1]
        self.ids.input_dt.text = prev_number

    def results(self):
        prev_number = self.ids.input_dt.text
        try:
            result = eval(prev_number)
            self.ids.input_dt.text = str(result)
        except:
            self.ids.input_dt.text = 'Input Error Buddy'

    def pos_neg(self):
        prev_number = self.ids.input_dt.text
        if '-' in prev_number:
            self.ids.input_dt.text = f'{prev_number.replace("-", "")}'
        else:
            self.ids.input_dt.text = f'-{prev_number}'

    def dot(self):
        prev_number = self.ids.input_dt.text
        num_list = re.split("[+/*%-]", prev_number)
        if (
                "+" in prev_number or "-" in prev_number or "/" in prev_number or "*" in prev_number or "%" in prev_number) and "." not in \
                num_list[-1]:
            prev_number = f"{prev_number}."
            self.ids.input_dt.text = prev_number

        elif "." in prev_number:
            pass
        else:
            prev_number = f"{prev_number}."
            self.ids.input_dt.text = prev_number


class INDEXI(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.icon = "fx.png"
        # self.theme_cls.material_style = "M3"
        Builder.load_string(kv)

        sm = MDScreenManager()
        sm.add_widget(Home(name='main'))
        sm.add_widget(Currencies(name='currencies'))
        sm.add_widget(PipScreen(name='calc'))
        return sm

    def my_func(self):
        open = self.root.get_screen("currencies").ids.op.text
        volume = self.root.get_screen("currencies").ids.vol.text
        high = self.root.get_screen("currencies").ids.hig.text
        low = self.root.get_screen("currencies").ids.lo.text
        link = f'https://trademavericks-api.herokuapp.com/nas100'
        data = {"open": open, "volume": volume, "low": low, "high": high}
        headers = {'Content-Type': 'application/json'}
        self.request = UrlRequest(url=link, req_headers=headers, on_success=self.func, method='POST',
                                  req_body=json.dumps(data))

    def func(self, *args):
        self.data = self.request.result
        ans = self.data
        print("Horray")
        self.root.get_screen("currencies").ids.put_txt_here.text = ans["prediction"]

    def my_us30(self):
        open = self.root.get_screen("currencies").ids.open_30.text
        volume = self.root.get_screen("currencies").ids.volume_30.text
        high = self.root.get_screen("currencies").ids.high_30.text
        low = self.root.get_screen("currencies").ids.low_30.text
        link = f'https://trademavericks-api.herokuapp.com/us30'
        data = {"open": open, "volume": volume, "low": low, "high": high}
        headers = {'Content-Type': 'application/json'}
        self.request = UrlRequest(url=link, req_headers=headers, on_success=self.us30, method='POST',
                                  req_body=json.dumps(data))

    def us30(self, *args):
        self.data = self.request.result
        ans = self.data
        print("Horray")
        self.root.get_screen('currencies').ids.put_us30.text = ans["prediction"]

    def my_ger30(self):
        open = self.root.get_screen("currencies").ids.open_40.text
        volume = self.root.get_screen("currencies").ids.volume_40.text
        high = self.root.get_screen("currencies").ids.high_40.text
        low = self.root.get_screen("currencies").ids.low_40.text
        link = f'https://trademavericks-api.herokuapp.com/ger30'
        data = {"open": open, "volume": volume, "low": low, "high": high}
        headers = {'Content-Type': 'application/json'}
        self.request = UrlRequest(url=link, req_headers=headers, on_success=self.ger30, method='POST',
                                  req_body=json.dumps(data))

    def ger30(self, *args):
        self.data = self.request.result
        ans = self.data
        print("Workline")
        self.root.get_screen('currencies').ids.put_ger30.text = ans["prediction"]

    def set_screen(self, currencies):
        self.root.current = currencies

    def cal_screen(self, calc):
        self.root.current = calc

    def nasdaq(self):
        link = f'https://trademavericks-api.herokuapp.com/nasdaq'
        headers = {'Content-Type': 'application/json'}
        self.request = UrlRequest(url=link, req_headers=headers, on_success=self.nas, method='GET')

    def nas(self, request, data):
        ans = data
        print("Workline")
        self.root.get_screen('currencies').ids.nas100_info.text = ans

    def dowjones(self):
        link = f'https://trademavericks-api.herokuapp.com/dowjones'
        headers = {'Content-Type': 'application/json'}
        self.request = UrlRequest(url=link, req_headers=headers, on_success=self.dowj, method='GET')

    def dowj(self, request, data):
        ans = data
        print("Workline")
        self.root.get_screen('currencies').ids.dowjones_info.text = ans

    def german40(self):
        link = f'https://trademavericks-api.herokuapp.com/german40'
        headers = {'Content-Type': 'application/json'}
        self.request = UrlRequest(url=link, req_headers=headers, on_success=self.ger, method='GET')

    def ger(self, request, data):
        ans = data
        print("Workline")
        self.root.get_screen('currencies').ids.german40_info.text = ans


INDEXI().run()