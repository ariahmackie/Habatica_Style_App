
class Pet:
    def __init__(self, type):
        self.level = 0
        self.feeding_level = 0
        self.type = type

    def feed_pet(self, food):
        if self.type == food.type:
            self.feeding_level += food.calories

    def level_up_pet(self, food):
        if self.feeding_level >= 20:
            self.level += 1
            self.feeding_level = self.feeding_level - 20

    def play_with_pet(self):
        """user gets a surprise when they do this"""
        pass


class Hunter(Pet):
    def __init__(self):
        self.type = "hunter"

    def hunt(self):
        pass

    def run(self):
        pass

class Cat(Hunter):
    def __init__(self):
        self.description = "cat"
        self.strength = 2
        self.speed = 3

class Dog(Hunter):
    def __init__(self):
        self.description = "dog"
        self.strength = 3
        self.speed = 3

class Fox(Hunter):
    def __init__(self):
        self.description = "fox"
        self.strength = 3
        self.speed = 2

class Lion(Hunters):
    def __init__(self):
        self.description = "lion"
        self.strength = 5
        self.speed = 1

class Wolf(Hunter):
    def __init__(self):
        self.description = "wolf"
        self.strength = 4
        self.speed = 1

class Tiger(Hunter):
    def __init__(self):
        self.description = "tiger"
        self.strength = 5
        self.speed = 2

class Leopard(Hunter):
    def __init__(self):
        self.description = "leopard"
        self.strength = 4
        self.speed = 2

class Cheetah(Hunter):
    def __init__(self):
        self.description = "cheetah"
        self.strength = 3
        self.speed = 5

class Monkey(Hunter):
    def __init__(self):
        self.description = "monkey"
        self.strength = 1
        self.speed = 1

class Mount(Pet):
    def __init__(self):
        self.type = "mount"

    def ride(self):
        pass

class Horse(Mount):
    def __init__(self):
        self.description = "horse"
        self.strength = 5
        self.speed = 5

class Donkey(Mount):
    def __init__(self):
        self.description  = "donkey"
        self.strength = 3
        self.speed = 3


class Swimmer(Pet):
    def __init__(self):
        self.type = "swimmer"

    def swim(self):
        pass

    def go_fishing(self):
        pass

class Whale(Swimmer):
    def __init__(self):
        self.description = "whale"
        self.strength = 5
        self.speed = 3

class Dolphin(Swimmer):
    def __init__(self):
        self.description = "dolphin"
        self.strength = 3
        self.speed = 5

class Goldfish(Swimmer):
    def __init__(self):
        self.description = "goldfish"
        self.strength = 1
        self.speed = 1

class Flyer(Pet):
    def __init__(self):
        self.type = "flyer"

class Bat(Flyer):
    def __init__(self):
        self.description = "bat"
