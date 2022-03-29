"""Defines player class and interaction between Player,
Account, Backpack, and Task"""

import datetime
from Model import rpg_database as db

class Player:
    def __init__(self, email, username, password):
        self.player_account = Account(email, username, password)
        self.tasklist = []
        self.coins = 0
        self.level = 0
        self.backpack = Backpack()
        self.experience = 0
        self.strength = 0
        self.perception = 0
        self.intelligence = 0
        self.charisma = 0
        db.add_new_player(email, username, password)
        
    def add_to_experience(self, task):
        self.experience += int(task.taskvalue)
        if self.experience >= 15:
            self.experience = self.experience - 15
            self.level_up_player()

    def add_to_tasklist(self, newtask):
        self.tasklist.append(newtask)

    def subtract_from_tasklist(self, deleted_task):
        self.tasklist.remove(deleted_task)

    def add_coins(self, num_of_coins):
        self.coins += num_of_coins

    def subtract_coins(self, num_of_coins):
        if self.coins - num_of_coins < 0:
            raise CustomException("Not Enough Money")
        else:
            self.coins -= num_of_coins

    def level_up_player(self):
        self.level += 1


class CustomException:
        def __init__(self, *args):
            if args:
                self.message = args[0]
            else:
                self.message = None

        def __str__(self):
            if self.message:
                return "Error raised: {0}".format(self.message)
            else:
                return "Custom Exception Raised"

class Account:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
        self.isloggedin = False

    def login(self):
        self.isloggedin = True

    def logout(self):
        self.isloggedin = False


class Backpack():

    def __init__(self):
        self.items = {}

    def get_backpack_items(self):
        return self.items

    def display_item(self, key):
        print(self.items[key])

    def display_backpack_items(self):
        i = 1
        for key, value in self.items.items():
            print(str(i) + " - " + str(key) + ": " + str(value))
            i += 1

    def add_items(self, item, num_items):
        if item in self.items.keys():
            self.items[item] +=  num_items
        else:
            self.items[item] = num_items

    def delete_all_item_copies(self, item):
        if item in self.items.keys():
            del self.items[item]
        else:
            raise CustomException("item is not in backpack")

    def decrement_item(self, item):
        if item in self.items.keys():
            self.items[item] -= 1
        else:
            raise CustomException("item not in backpack")
        if self.items[item] == 0:
            self.delete_all_item_copies(item)

    def use_item(self, item):
        self.decrement_item(item)
        return item

    def make_list_of_items(self):
        backpack_list = []
        for key in self.items.items():
            backpack_list.append(key)
        return backpack_list

class Task:

    def __init__(self, description, duedate = datetime.date.today(), taskvalue = 1, is_repeatable = False):
        self.description = description
        self.duedate = duedate
        self.taskvalue = 1
        self.is_repeatable  = is_repeatable

    def edit_task_detail(self, description):
        self.description = description

    def edit_task_duedate(self, duedate):
        self.duedate = duedate

    def edit_task_value(self, taskvalue):
        self.taskvalue = taskvalue

    def make_task_repeatible(self):
        self.isrepeatable = True

    def display_task(self):
        return [self.description, self.duedate, self.taskvalue, self.isrepeatable]
