#database
import sqlite3

connection = sqlite3.connect("cat.db")
cursor = connection.cursor()

def create_cat_table():
    print("create_cat_table()")
    cursor.execute('''CREATE TABLE Cats(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL);''')

def add_new_cat(cat_tuple):
    print("add_new_cat()")
    command = "INSERT INTO Cats (name, age) VALUES (?, ?)"
    cursor.execute(command, cat_tuple)


def print_cat_table():
    print("print_cat_table()")
    data = cursor.execute("SELECT * From Cats")
    for i in data:
        print(i)

def drop_cat_table():
    print("drop_cat_table()")
    cursor.execute('DROP TABLE IF EXISTS Cats')
