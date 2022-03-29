import sys
import os
controller_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(controller_directory)
sys.path.append(parent_directory)

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from Helpers import login_helper as lh
from Model.player import Player
from Helpers import dummy_players as dp
from kivy.graphics import Rectangle, Color
from kivy.factory import Factory
from kivy.uix.dropdown import DropDown
import re
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.boxlayout import MDBoxLayout
from datetime import datetime
from Model import rpg_database as db

db.drop_all_tables()
db.create_all_tables()


Window.size = (400,800)
player1 = dp.create_test_user1()
player2 = dp.create_test_user2()


class Login(Screen):
    pass

class Home(Screen):
    pass

class ForgotPassword(Screen):
    pass

class PassCodeSubmission(Screen):
    pass

class NewAccount(Screen):
    pass

class NewTask(Screen):
    pass

class DialogBox(MDBoxLayout):
    def __init__(self, **kwargs):
        #super().__init__(**kwargs)
        self.ids.date_text.text = str(datetime.now().strftime('%A %d % B % Y'))

    def show_calendar(self):
        #super().__init__(**kwargs)
        calendar = MDDatePicker()
        calendar.bind(on_save = self.on_save)
        calendar.open()

    def on_save(self, instance, value, date_range):
        date = value.strftime('%A %d %B %Y')
        self.ids.date_text.text = str(date)
#class DifficultyDropDown(BoxLayout):
#    pass

sm = ScreenManager(transition = NoTransition())
sm.add_widget(Login(name='login'))
sm.add_widget(Home(name='home'))

class MainApp(MDApp):
    def build(self):
        self.sm = ScreenManager(transition = NoTransition())
        self.sm.add_widget(Login(name='login'))
        self.sm.add_widget(Home(name='home'))
        self.sm.add_widget(ForgotPassword(name = 'forgotpassword'))
        self.sm.add_widget(PassCodeSubmission(name = 'passcodesubmission'))
        self.sm.add_widget(NewAccount(name = 'newaccount'))
        self.sm.add_widget(NewTask(name = 'newtask'))
        return self.sm

    def to_home(self):
        self.sm.current = 'home'

    def to_new_account(self):
        self.sm.current = 'newaccount'

    def to_login(self):
        self.sm.current = 'login'

    def to_forgotpassword(self):
        self.sm.current = 'forgotpassword'

    def to_new_task(self):
        self.sm.current = 'newtask'

    def create_new_user(self, username, email, password):
        print("create new user")
        if self.is_valid_account(username, email, password):
            new_player = Player(email, username, password)
            self.player = new_player
            self.sm.current = "home"
        else:
            print("Did not make an account.")

    def authenticate_login(self, email, password):
        pass

    def password_error_message(self):
        warning = Label(text = '[color=ff3333]Wrong password.[/color]', markup = True, pos = (270, 270), size = (50, 50), size_hint = (None, None)  )
        self.sm.current_screen._widget(warning)

    def forgotpassword(self):
        self.sm.current = 'forgotpassword'

    def passcodesubmission(self, email):
        self.player = lh.get_registered_player_via_email(email, players)
        if self.player != 0:
            print("trying to send passcode")
            self.sm.current = 'passcodesubmission'
            self.correct_passcode = lh.email_passcode(email)
            print(self.correct_passcode)

    def validate_passcode(self,user_passcode):
        if str(user_passcode) == str(self.correct_passcode):
            self.sm.current = 'home'
            Factory.ChangePasswordPopup().open()

        else:
            warning = Label(text = '[color=ff3333]Wrong passcode.[/color]', markup = True, pos = (270, 370), size = (50, 50), size_hint = (None, None))
            self.sm.current_screen._widget(warning)

    def save_newpassword(self, newpassword):
        print("old password:")
        print(self.player.player_account.password)
        self.player.player_account.password = newpassword
        print("New password")
        print(self.player.player_account.password)

    def open_calendar(self):
        DialogBox().show_calendar()

if __name__ == "__main__":
    MainApp().run()
