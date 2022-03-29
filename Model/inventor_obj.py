
class Food:
    def _init__(self, type = "basic", calories = 10):
        self.type = type
        self.calories = calories

    def display_food(self):
        print(self.type)
        print("calories: "+ self.calories)
