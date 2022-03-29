import unittest
from menu import CommandMenu
from player import Player, CustomException, Account, Backpack, Task
import datetime

class TestMenu(unittest.TestCase):
    def test_user_logged_in_at_welcome_menu(self):
        player1 = Player("bob", "123abc!")
        menu = CommandMenu([player1])
        menu.current_player = player1
        menu.welcome_menu(True)
        self.assertTrue(player1.player_account.isloggedin, "player should be logged in")

if __name__ == "__main__":
    unittest.main()
