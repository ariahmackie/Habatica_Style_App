"""Defines player class and interaction between Player,
Account, Backpack, and Task"""
import sys
import os
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

import datetime
from Model import rpg_database as db
from Helpers import login_helper as lh

class Player:
    def __init__(self, email, username, password):
        if self.is_existing_player(email, username):
            player = lh.get_registered_player_via_email(email)
            self.set_up_existing_player(player)
        else:
            self.set_up_new_player(email, username, password)

    def is_existing_player(self, email, username):
        player_with_email = lh.get_registered_player_via_email(email)
        player_with_username = lh.get_registered_player_via_username(username)
        if player_with_email is not None and player_with_username is not None:
            if player_with_email == player_with_username:
                return True
        return False

    def set_up_existing_player(self, player_tuple):
        print("setting up existing player")
        # player_tuple (email, username, password, isloggedin, level, coins, experience, health, strength, perception, intelligence, charisma)
        self.email = player[0]
        self.username = player[1]
        self.password = player[2]
        self.isloggedin = 1
        self.level = player[4]
        self.coins = player[5]
        self.experience = player[6]
        self.health = player[7]
        self.strength = player[8]
        self.perception = player[9]
        self.intelligence = player[10]
        self.charisma = player[11]
        self.player_id = self.__get_player_id__()

    def set_up_new_player(self, email, username, password):
        print("setting up new player")
        self.email = email
        self.username = username
        self.password = password
        self.isloggedin = 1
        self.level = 0
        self.coins = 0
        self.experience = 0
        self.health = 100
        self.strength = 0
        self.perception = 0
        self.intelligence = 0
        self.charisma = 0
        player_tuple = (self.email, self.username, self.password, self.isloggedin, self.level, self.coins, self.experience, self.health, self.strength, self.perception, self.intelligence, self.charisma)
        db.add_new_player(player_tuple)
        self.player_id = self.__get_player_id__()
        self.backpack = Backpack()

    def __get_player_id__(self):
        player_tuple = lh.get_registered_player_via_email(self.email)
        player_id = player_tuple[0]
        return player_id

    def add_to_experience(self, task):
        self.experience += int(task.taskvalue)
        if self.experience >= 15:
            self.experience = self.experience - 15
            self.level_up_player()

    def add_task(self, description, duedate = datetime.date.today(), taskvalue = 1, is_repeatable = False):
        self.tasklist.append(newtask)

    def delete_task(self, deleted_task):
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
        self.is_repeatable = True

    def display_task(self):
        return [self.description, self.duedate, self.taskvalue, self.is_repeatable]
