import rpg_database as rpg
from player import Player

rpg.drop_all_tables()
rpg.create_all_tables()

player1 = Player("aaa@gmail.com", "aaa", "abcdefghi123")
rpg.print_player_table()
