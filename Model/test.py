import rpg_database as db
from player import Player

db.drop_all_tables()
db.create_all_tables()
player1 = Player("aaa@gmail.com", "aaa", "abcdefghi123")

print(player1.email == "aaa@gmail.com")
print(player1.health == 100)
print(player1.player_id == 1)
