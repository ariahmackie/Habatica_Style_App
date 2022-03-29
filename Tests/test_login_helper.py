import sys
import os
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)


import unittest
from Helpers import login_helper as lh
import Model.rpg_database as db
from Model.player import Player

class TestLoginHelper(unittest.TestCase):
        def setUp(self):
            db.drop_all_tables()
            self.set_up_existing_players()

        def set_up_existing_players(self):
            db.create_player_table()
            player1 = Player("adam@gmail.com", "adam", "abc123")
            player2 = Player("sam@gmail.com", "sam", "abc123")
    

        def test_is_valid_new_account_info(self):
            pass

        def test_is_available_username(self):
            pass

        def test_is_available_email(self):
            pass

        def test_is_valid_new_email(self):
            pass

        def test_is_valid_new_password(self):
            pass

        def test_validate_email_and_password(self):
            pass

        def test_get_registered_player_via_username(self):
            print("test:")
            player_id = lh.get_registered_player_via_username("adam")
            expected_id = 1
            self.assertEqual(player_id, expected_id, "should return first user")

        def test_get_registered_player_via_email(self):
            pass


        def test_is_correct_password_for_current_player(self):
            pass

        def test_email_passcode(self):
            pass

        def test_five_digit_passcode(self):
            pass

if __name__ == '__main__':
    unittest.main()
