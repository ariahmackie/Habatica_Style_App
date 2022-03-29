import unittest
from player import Player
from player import CustomException
from player import Account
from player import Backpack
from player import Task
import datetime

class TestPlayer(unittest.TestCase):
    def test_init(self):
        username = "Bob"
        password = 123
        hero = Player(username, password)
        self.assertEqual(hero.coins, 0, "expected 0")
        self.assertEqual(hero.level, 0, "expected 0")

    def test_add_to_tasklist(self):
        username = "Bob"
        password = 123
        hero = Player(username, password)
        hero.add_to_tasklist("task")
        self.assertEqual(len(hero.tasklist), 1, "expected task list to now have 1 item")
        self.assertEqual(hero.tasklist[0].description, "task", "task added")

    def test_subtract_from_tasklist(self):
        username = "Bob"
        password = 123
        hero = Player(username, password)
        hero.tasklist = ["item1", "item2", "item3", "item4"]
        hero.subtract_from_tasklist("item1")
        self.assertEqual(len(hero.tasklist), 3, "list length that was 4 should now be 3")

    def test_add_coins(self):
        username = "Bob"
        password = 123
        hero = Player(username, password)
        hero.add_coins(100)
        self.assertEqual(hero.coins, 100, "should have 100 coins" )

    def test_subtract_coins(self):
        username = "Bob"
        password = 123
        hero = Player(username, password)
        hero.add_coins(100)
        hero.subtract_coins(2)
        self.assertEqual(hero.coins, 98, "should have 98 coins")

    def test_level_up_player(self):
        username = "Bob"
        password = 123
        hero = Player(username, password)
        hero.level_up_player()
        self.assertEqual(hero.level, 1, "should be level 1")

class TestAccount(unittest.TestCase):
    def test_init_account(self):
        newaccount = Account("Bob", 123)
        self.assertEqual(newaccount.username, "Bob", "username should be bob")
        self.assertEqual(newaccount.password, 123, "password should be 123")


    def test_login(self):
        newaccount = Account("Bob", 123)
        newaccount.isloggedin = False
        newaccount.login()
        self.assertTrue(newaccount.isloggedin, "is logged in")

    def test_logout(self):
        newaccount = Account("Bob", 123)
        newaccount.logout()
        self.assertFalse(newaccount.isloggedin, "is logged out")

class TestBackpack(unittest.TestCase):

    def test_init_backpack(self):
        backpack = Backpack()
        self.assertEqual(backpack.items, {}, "should create empty dictionary")

    def test_open_backpack(self):
        backpack = Backpack()
        self.assertEqual(backpack.open_backpack() ,{}, "should return dictionary")

    def test_add_items(self):
        backpack = Backpack()
        backpack.add_items("ruby", 10)
        self.assertEqual(backpack.open_backpack(), {"ruby": 10}, "ten rubies expected in backpack")
        backpack.add_items("hat", 1)
        self.assertEqual(backpack.items["hat"], 1, "should have one hat")
        backpack.add_items("ruby", 5)
        self.assertEqual(backpack.items["ruby"], 15, "15 rubies expected")

    def test_delete_all_item_copies(self):
        backpack = Backpack()
        backpack.items = {"ruby": 10}
        backpack.delete_all_item_copies("ruby")
        self.assertFalse( "ruby" in backpack.items.keys(), "all rubies should be gone")

    def test_decrement_item(self):
        backpack = Backpack()
        backpack.items = {"ruby": 10, "tree": 1}
        backpack.decrement_item("ruby")
        self.assertEqual(backpack.items["ruby"], 9, "should have one less rubies")
        backpack.decrement_item("tree")
        self.assertFalse( "tree" in backpack.items, "because tree went to zero there should be none")

    def test_use_item(self):
        backpack = Backpack()
        backpack.items = {"tree": 1}
        stored_value = backpack.use_item("tree")
        self.assertFalse("tree" in backpack.items , "trees be all used up")
        self.assertEqual(stored_value, "tree")

class TestTask(unittest.TestCase):

    def test_task_init(self):
        newtask = Task("make your bed")
        self.assertEqual(newtask.description, "make your bed", "item description set")

    def test_edit_task_detail(self):
        newtask = Task("make your bed")
        newtask.edit_task_detail("clean your room")
        self.assertEqual(newtask.description, "clean your room", "task description should be changed")

    def test_edit_task_duedate(self):
        newtask = Task("make your bed")
        date = datetime.datetime(2021, 10, 21)
        newtask.edit_task_duedate(date)
        self.assertEqual(newtask.duedate, date, "date should be updated")

    def test_edit_task_value(self):
        newtask = Task("make your bed")
        newtask.edit_task_value(2)
        self.assertEqual(newtask.taskvalue, 2, "score should be 2")

    def test_make_task_repeatable(self):
        newtask = Task("make your bed")
        self.assertFalse(newtask.isrepeatable, "not repeatable before made repeatable" )
        newtask.make_task_repeatible()
        self.assertTrue(newtask.isrepeatable, "tasks should be repeatable now")

    def test_display_task(self):
        newtask = Task("make your bed")
        self.assertEqual(newtask.display_task(), ["make your bed", datetime.date.today(), 1, False])


if __name__ == "__main__":
    unittest.main()
