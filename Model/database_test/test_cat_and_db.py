# test
import db
from cat import Cat


db.drop_cat_table()
db.create_cat_table()
my_cat = Cat()
db.print_cat_table()
db.add_new_cat(("bob", 3))
db.print_cat_table()
