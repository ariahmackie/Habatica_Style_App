# code to import from different directories
from Model.player import Player, Task

def create_test_user1():
    player1 = Player("to@example.com", "bob", "123abc!")
    player1.add_to_tasklist(Task("read"))
    player1.add_to_tasklist(Task("exercise"))
    player1.add_to_tasklist(Task("take a walk"))
    player1.coins = 100
    player1.level = 5
    player1.backpack.items = {"rubies": 10, "growth potion" : 3, "egg": 1, "tree seed": 2}
    return player1

def create_test_user2():
    player2 = Player("ariah@gmail.com", "bill", "123abc!")
    player2.add_to_tasklist(Task("clean kitchen"))
    player2.add_to_tasklist(Task("study"))
    player2.coins = 50
    player2.level = 2
    player2.backpack.items = {"swords": 10, "helmets": 2}
    return player2
