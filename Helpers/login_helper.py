"""functions for logging in, forgotten passwords, and creating a new account."""
import sys
import os
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

import random
from Helpers.email import Email
from Model import rpg_database as db
from validate_email import validate_email


# for Creating New Accounts ------------------------------------------


def is_valid_new_account_info(username: str, email: str, password: str) -> bool:
    """Validate username, email, and password are not taken and are formatted correctly."""
    if is_available_username(username):
        if is_available_email(email) and is_valid_new_email(email):
            if is_valid_new_password(password):
                return True
    return False

def is_available_username(username: str) -> bool:
    """Return True if username is not taken (not in the database)."""
    player = get_registered_player_via_username(username)
    if player is None:
        return True
    return False


def is_available_email(email: str) -> bool:
    """Return True if email is not taken (not in the database)."""
    player = get_registered_player_via_email(email)
    if player is None:
        return True
    return False


def is_valid_new_email(email: str) -> bool:
    """Return True if email if formatted correctly."""
    is_valid = validate_email(
        email_address = email,
        check_format = True,
        check_blacklist = False,
        check_dns = False,
        check_smtp = False)
    return is_valid


def is_valid_new_password(password: str) -> bool:
    """Password must be atleast 8 characters long and have letters and numbers."""
    has_letter = False
    has_digit = False
    long_enough = len(password) >= 8
    for ch in password:
        if ch.isalpha():
            has_letter = True
        if ch.isdigit():
            has_digit = True
    if has_letter and has_digit and long_enough:
        return True
    return False


def invalid_username_warning(error_list: list) -> str:
    """Return a string about what is wrong with username."""
    pass


def invalid_password_warning(error_list: list) -> str:
    """Return a string about what is wrong with password."""
    pass


# For Logging into Existing Accounts ------------------------------------------


def validate_email_and_password(email: str, password: str) -> bool:
    """Return True if email and password match in the database."""
    player = get_registered_player_via_email(email)
    if player != 0:
        print(player)
        if is_correct_password_for_current_player(player, password):
            print("fill out later")
        else:
            print("incorrect password")
    else:
        print("alert %s Is not registered email." % (email))


def is_correct_password_for_current_player(player: tuple, password: str) -> bool:
    pass


# Retrieve User Account Info from Database -------


def get_registered_player_via_username(username: str):
    player = db.find_player_with_feature("username", username)
    return player


def get_registered_player_via_email(email: str):
    player = db.find_player_with_feature("email", email)
    return player


# Handle forgotten password-----------------------
def email_passcode_1(players):
    receiver_address = str(raw_input("Please type your email >"))
    player = get_registered_player_via_email(receiver_address)
    if player is not None:
        global CURRENT_PLAYER
        CURRENT_PLAYER = player
        passcode = generate_five_digit_passcode()
        newemail = Email(receiver_address, "Passcode", str(passcode))
        newemail.send()
        user_submit_code(passcode)
    else:
        print("Sorry. That email doesn't exist in the database")

def email_passcode(email):
    receiver_address = email
    passcode = generate_five_digit_passcode()
    newemail = Email(receiver_address, "Passcode", str(passcode))
    newemail.send()
    return passcode

def generate_five_digit_passcode():
    passcode = random.randint(00000, 99999)
    return passcode

def user_submit_code(generatedpasscode):
    """user places their code, confirm if it is correct"""
    user_passcode = int(raw_input("Please type 5 digit passcode. >"))
    if generatedpasscode == user_passcode:
        welcome_menu()
    else:
        print("incorrect passcode")
