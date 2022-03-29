'''Create Database for All Classes in RPG Game'''
import sqlite3
import random

#connect to database and cursor

connection =sqlite3.connect("rpg_data.db")
cursor = connection.cursor()

#--------------------- PLAYER TABLE------------------------------------------------------------------
def create_player_table():
    cursor.execute('''CREATE TABLE Player(
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    isloggedin INTEGER NOT NULL,
    level INTEGER NOT NULL,
    coins INTEGER NOT NULL,
    experience INTEGER NOT NULL,
    health INTEGER NOT NULL,
    strength INTEGER NOT NULL,
    perception INTEGER NOT NULL,
    intelligence INTEGER NOT NULL,
    charisma INTEGER NOT NULL,
    image BLOB);''')

def add_new_player( email, username, password):
    command = "INSERT INTO Player (email, username, password, isloggedin, level, coins, experience, health, strength, perception, intelligence, charisma) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )"
    player_tuple = (email, username, password, 1, 1, 100, 0, 100, 0, 0, 0, 0)
    cursor.execute(command, player_tuple)

def get_player(id):
    cursor.execute("SELECT * FROM Player where id =%d" % id)
    player = cursor.fetchone()
    return player

def find_players_with_feature(feature_type, value):
    cursor.execute("SELECT * From player where %s=?" % feature_type, (value,))
    players = cursor.fetchall()
    return players


def get_value_from_player(value_type, player_id):
    command = "SELECT %s FROM Player WHERE id=?" % value_type
    cursor.execute(command, (player_id,))
    value = cursor.fetchone()[0]
    return value

def change_value_in_player(value_type, value, player_id):
    command = "UPDATE Player SET %s = ? WHERE id=?" % value_type
    cursor.execute(command, (value, player_id))

def decrease_value_from_player(value_type, value, player_id):
    current_value = get_value_from_player(value_type, player_id)
    updated_value = current_value - value
    change_value_in_player(value_type, updated_value, player_id)

def increase_value_in_player(value_type, value, player_id):
    current_value = get_value_from_player(value_type, player_id)
    updated_value = current_value + value
    change_value_in_player(value_type, updated_value, player_id)

def increase_health(player_id, value):
    health = get_value_from_player("health", player_id)
    if health + value >= 100:
        print("health is full")
        health = 100
    else:
        health = health + value
    change_value_in_player("health", health, player_id)


def decrease_health(player_id, value):
    health = get_value_from_player("health", player_id)
    if health - value <= 0:
        print("health is 0")
        health = 0
    else:
        health = health - value
    change_value_in_player("health", health, player_id)

def drop_player_table():
    cursor.execute('DROP TABLE IF EXISTS Player')

def print_player_table():
    print("Player Table")
    player_tuple = ("id", 'email', "username", "password", "isloggedin", "level", "coins", "experience", "strength", "perception", "intelligence", "charisma", "image")
    print(player_tuple)
    data = cursor.execute("SELECT * From Player")
    for i in data:
        print(i)
    print("")

#-----------------------------INVENTORY TABLE ---------------------------------------------------------------
def create_inventory_table():
    cursor.execute('''CREATE TABLE Inventory(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    count INTEGER NOT NULL,
    stock_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    FOREIGN KEY(player_id) REFERENCES Player(id),
    FOREIGN KEY(stock_id) REFERENCES Stock(id));''')

def drop_inventory_table():
    cursor.execute('DROP TABLE IF EXISTS Inventory')

def add_a_prize(player_id):
    item_id = get_random_itemid()
    add_item_by_id(item_id, player_id)

def get_item_by_id(id):
    cursor.execute("SELECT * FROM INVENTORY WHERE id=?", (id,))
    item = cursor.fetchone()
    return item

def add_item_by_id(item_id, player_id):
    item_tuple = select_stockitem_by_id(item_id)
    add_item(item_tuple, player_id)

def add_item_by_name(item_name, player_id):
    item_tuple = select_stockitem_by_name(item_name)
    add_item(item_tuple, player_id)

def add_item(item_tuple, player_id):
    item_name = item_tuple[1]
    stock_id = item_tuple[0]
    #count = count_how_many_of_item(item_name, player_id)
    count = 1
    cursor.execute("INSERT INTO Inventory (name, stock_id, count, player_id) VALUES (?, ?, ?, ?)", (item_name, stock_id, count, player_id))

def count_how_many_of_item(item_name, player_id):
    cursor.execute("SELECT count FROM Inventory WHERE name=? AND player_id=?", (item_name, player_id))
    count = cursor.fetchone()[0]
    return count

def print_inventory_table():
    print(("id", "name", "count", "stock_id", "player_id"))
    values = cursor.execute("SELECT * FROM Inventory")
    for x in values:
        print(x)

#-------------------------------ITEM TABLE--------------------------------------------------------------------
                                                                                                                            # (level, coins, experience, strength, perception, intelligence, charisma)
fruit_tuples =[("apple", 2, "fruit"), ("banana", 3, "fruit"), ("berries", 1, "fruit"), ("cherries", 2, "fruit"), ("coconut", 3, "fruit"), ("grapefruit", 4, "fruit"), ("grapes", 1, "fruit"), ("kiwi", 2, "fruit"), ("lemon", 3, "fruit"), ("lime", 4, "fruit"), ("mango", 1, "fruit"), ("orange", 2, "fruit"), ("peach", 3, "fruit"), ("pear", 4, "fruit"), ("pineapple", 1, "fruit"),("strawberries", 2, "fruit"), ("watermelon", 3, "fruit")]

vegetable_tuples = [("artichoke", 1, "vegetable"), ("asparagus", 2, "vegetable"), ("broccoli", 3, "vegetable"), ("cabbage", 4, "vegetable"), ("carrot", 1, 'vegetable'), ("cauliflower", 2, "vegetable"), ("corn", 3, "vegetable"), ("cucumber", 4, "vegetable"), ("eggplant", 1, "vegetable"), ("lettuce", 2, "vegetable"), ("mushrooms", 3, "vegetable"),("onion", 4, "vegetable"), ("peas", 1, "vegetable"), ("potato", 4, "vegetable"), ("radishes", 2, "vegetable"), ("tomato", 3, "vegetable")]

dessert_tuples = [("chocolate chip cookies", 3, "dessert"), ("apple pie", 2, "dessert"), ("cheese cake", 1, "dessert"), ("carrot cake", 3, "dessert"), ("icecream", 2, "dessert"), ("birthday cake", 3, "dessert"), ("cotton candy", 2, "dessert"), ("brownies", 2, "dessert"), ("pumpkin pie", 3, "dessert"), ("red velvet cake", 2, "dessert"), ("donut", 2, "dessert"), ("lollypop", 1, "dessert"), ("cherry pie", 2, "dessert")]

meal_tuples = [("ramen", 1, "meal"), ("sushi", 1, "meal"), ("chow mein", 2, "meal"), ("orange chicken", 4, "meal"), ("roast chicken", 2, "meal"), ("rice", 3, "meal"), ("taco", 4, "meal"), ("roast beef", 3, "meal"), ("baked potato", 2, "meal"), ("enchilada", 3, "meal"), ("sandwich", 2, "meal")]

food_tuples = fruit_tuples + vegetable_tuples + dessert_tuples + meal_tuples
print(len(fruit_tuples) + len(vegetable_tuples) + len(dessert_tuples) + len(meal_tuples))

def create_stock_table():
    cursor.execute('''CREATE TABLE Stock(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    value INTEGER NOT NULL,
    type TEXT NOT NULL,
    image BLOB);''')

def select_stockitem_by_id(stock_id):
    command = "SELECT * FROM Stock WHERE id=?"
    cursor.execute(command, (stock_id,))
    stockitem = cursor.fetchone()
    return stockitem

def select_stockitem_by_name(stock_name):
    command = "SELECT * FROM Stock WHERE name=?"
    cursor.execute(command, (stock_name,))
    stockitem = cursor.fetchone()
    return stockitem

def populate_stock_table():
    command = "INSERT INTO Stock (name, value, type) VALUES (?, ?, ?)"
    for i in food_tuples:
        cursor.execute(command, i)

def get_num_items_in_stock():
    command = "SELECT COUNT(*) FROM Stock"
    cursor.execute(command)
    num_items = cursor.fetchone()[0]
    return num_items

def get_random_itemid():
    num_items = get_num_items_in_stock()
    id_list = range(1, num_items, 1)
    item_id = random.choice(id_list)
    return item_id

def print_stock_table():
    print("Stock Table")
    data = cursor.execute("SELECT * FROM Stock")
    for i in data:
        print(i)
    print("")

def drop_stock_table():
    cursor.execute('DROP TABLE IF EXISTS Stock')

#--------------------------------TASK TABLE ---------------------------------------
def create_task_table():
    cursor.execute('''CREATE TABLE Tasks(
    id INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    duedate TEXT,
    value INTEGER NOT NULL,
    is_repeatable INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    complete INTEGER NOT NULL,
    FOREIGN KEY(player_id) REFERENCES Player(id));''')

def drop_task_table():
    cursor.execute('DROP TABLE IF EXISTS Tasks')

def create_task(description, duedate, value, is_repeatable, person_id):
    command = "INSERT INTO Tasks (description, duedate, value, is_repeatable, player_id, complete) VALUES (?, ?, ?, ?, ?, ?)"
    task_tuple = (description, duedate, value, is_repeatable, person_id, 0)
    cursor.execute(command, task_tuple)

def get_task_by_id(task_id):
    command = "SELECT * From Tasks WHERE id=?"
    cursor.execute(command, (task_id,))
    task = cursor.fetchone()
    return task

def get_task_feature_by_id(feature, task_id):
    command = "SELECT %s FROM Tasks where id=?" %feature
    cursor.execute(command, (task_id, ))
    feature = cursor.fetchone()[0]
    return feature

def return_player_tasks(player_id):
    command = "SELECT * FROM Tasks where player_id=?"
    cursor.execute(command, (player_id,))
    tasks = cursor.fetchall()
    return tasks

def change_value_in_task(value_type, value, id):
    command = "UPDATE Tasks SET %s = ? WHERE id=?" % value_type
    cursor.execute(command, (value, id))

def delete_task(task_id):
    command = "DELETE FROM Tasks WHERE id=?"
    cursor.execute(command, (task_id,))

def complete_task(task_id):
    command = "UPDATE Tasks SET complete = 1 WHERE id=?"
    cursor.execute(command, (task_id,))
    cursor.execute("SELECT value FROM Tasks WHERE id=?", (task_id,))
    value = cursor.fetchone()[0]
    player_id = get_playerid_from_taskid(task_id)


def get_playerid_from_taskid(task_id):
    cursor.execute("SELECT player_id FROM Tasks WHERE id=?", (task_id,))
    player_id = cursor.fetchone()[0]
    return player_id


def print_task_table():
    task_tuple = ("id", "description", "duedate", "value", "is_repeatable", "player_id", "complete")
    print(task_tuple)
    data = cursor.execute("SELECT * FROM Tasks")
    for i in data:
        print(i)
    print('')

#--------------------All Tables ---------------------
def drop_all_tables():
    drop_player_table()
    drop_inventory_table()
    drop_task_table()
    drop_stock_table()

def create_all_tables():
    create_stock_table()
    create_inventory_table()
    create_task_table()
    create_player_table()


def close_connection():
    cursor.close()
    connection.close()
#------------------TEST FUNCTIONS -----------------------
