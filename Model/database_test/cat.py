import db

class Cat:
    def __init__(self):
        self.name = "cat"
        self.age = 4
        db.add_new_cat(("cat", 4))
