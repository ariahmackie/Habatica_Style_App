import sys
import os
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)



import unittest
import Helpers.login_helper as lh
import Model.rpg_database as db
from Model.player import Player

class TestLoginHelper(unittest.TestCase):
        def setUp(self):
            db.drop_all_tables()
            self.set_up_existing_players()

        def set_up_existing_players(self):
            db.create_player_table()
            player1 = Player("adam@gmail.com", "adam", "abcdefghi123")
            player2 = Player("sam@gmail.com", "sam", "abcdefghi123")

        def test_is_valid_new_account_info(self):
            bad_username = "adam" # already in database
            good_username = "ben"
            bad_email = "sam@gmail.com" # already in database
            bad_email2 = "aabdefef" #not a valid email
            good_email = "aaa@gmail.com"
            bad_password = "abc"
            good_password = "abcdefghij123"
            is_valid = lh.is_valid_new_account_info(bad_username, good_email, good_password)
            self.assertEqual(is_valid, False, "username already in database")
            is_valid = lh.is_valid_new_account_info(good_username, bad_email, good_password)
            self.assertEqual(is_valid, False, "email already in database")
            is_valid = lh.is_valid_new_account_info(good_username, bad_email2, good_password)
            self.assertEqual(is_valid, False, "not valid email format")
            is_valid = lh.is_valid_new_account_info(good_username, good_email, bad_password)
            self.assertEqual(is_valid, False, "password is wrong")
            is_valid = lh.is_valid_new_account_info(good_username, good_email, good_password)
            self.assertEqual(is_valid, True, "password is good")


        def test_is_available_username(self):
            is_available = lh.is_available_username("adam") # should not be available
            expected = False
            self.assertEqual(is_available, expected, "adam should not be available because it is already in the database")
            is_available = lh.is_available_username("May")  # should be available
            expected = True
            self.assertEqual(is_available, expected, "May is an available username")

        def test_is_available_email(self):
            is_available = lh.is_available_email("adam@gmail.com")
            expected = False
            self.assertEqual(is_available, expected, "adam@gmail.com is already taken ")
            is_available = lh.is_available_email("stacy@gmail.com")
            expected = True
            self.assertEqual(is_available, expected, "stacy@gmail.com is an available email")

        def test_is_valid_new_email(self):
            is_valid = lh.is_valid_new_email("aaa@ff")
            self.assertEqual(is_valid, False, "this is not a valid email")
            is_valid = lh.is_valid_new_email("bcef.com")
            self.assertEqual(is_valid, False, "also not a valid email")
            is_valid = lh.is_valid_new_email("xxx@.com")
            self.assertEqual(is_valid, False, "still not a valid email")
            is_valid = lh.is_valid_new_email("xxx@x.com")
            self.assertEqual(is_valid, True, "is valid")

        def test_is_valid_new_password(self):
            '''passwords must be atleast 8 characters and have a number and a letter'''
            is_valid = lh.is_valid_new_password("a")
            self.assertEqual(is_valid, False, "too short")
            is_valid = lh.is_valid_new_password("abcdefghij")
            self.assertEqual(is_valid, False, "password needs a number")
            is_valid = lh.is_valid_new_password("123343535")
            self.assertEqual(is_valid, False, "password needs letters")
            is_valid = lh.is_valid_new_password("abcdefghi1")
            self.assertEqual(is_valid, True, "password needs 8 or more charcters and must contain numbers ")

        def test_validate_email_and_password(self):
            good_email = "sam@gmail.com"
            bad_email = "bob@gmail.com" # not in database
            good_password = "abcdefghi123" #sam's password
            bad_password = "abcdefgh123" #typo
            is_valid = lh.validate_email_and_password(good_email, bad_password )
            self.assertEqual(is_valid, False, "not a matching password")
            is_valid = lh.validate_email_and_password(bad_email, good_password)
            self.assertEqual(is_valid, False, "email is not in database")
            is_valid = lh.validate_email_and_password(good_email, good_password)
            self.assertEqual(is_valid, True, "password matches user email")

        def test_get_registered_player_via_username(self):
            player_id = lh.get_registered_player_via_username("adam")
            expected_id = 1
            self.assertEqual(player_id, expected_id, "should return first user")

        def test_get_registered_player_via_email(self):
            player_id = lh.get_registered_player_via_email("adam@gmail.com")
            expected_id = 1
            self.assertEqual(player_id, expected_id, "should return first user")
            non_existing_player_id = lh.get_registered_player_via_email("john@gmail.com")
            expected_id = 0
            self.assertEqual(non_existing_player_id, expected_id, "should return 0 when the player email does not exist")

        def test_is_correct_password_for_current_player(self):
            pass

        def test_email_passcode(self):
            pass

        def test_five_digit_passcode(self):
            pass

if __name__ == '__main__':
    unittest.main()
