
from collections import namedtuple

stats = namedtuple("stats", "strength, charisma, intelligence, perception")
journey = namedtuple("Journey",  "title, type, Xp, appropriate_pet_type, stats")

white_whale_plot = [
"One day you are out on the ocean fishing and you see white gleaming from the water from about 50 yards away. What could it be?",
"You borrow your first mate's bernocolars(sp?) and identify the object. It is a white whale!",
"You ask your first mate about the whale. He tells you it is a rare albino killer whale. You decide you must take a close photo of this whale and sell it as an NFT",
"You scan horizon once again for the whale, but it is gone. How will you take your photo now?",
"Suddenly, you realize that the whale probably wants fish. You dump all your fish overboard. Your first mate is furious. He caught all of those fish.",
"You argue with your first mate over the dumped fish when you see a dorsal fin. 'Quick! Its the whale!' You steer towards the fin.'",
"But its not a great white whale, its a great white shark. The shark misses a chunk of fish and takes a chunk out of your boat instead",
"Your boat is sinking and the sharks are surrounding you and your crew. Your first mate thinks you're an idiot. You must come up with a plan.",
"You radio for help. Help is on its way but your boat is ruined and you still are gaining water fast.",
"You decide to video tape the sinking of your boat for insurance purposes. You are facing the camera when suddenly just 10 feet away from the boat the white whale jumps into the air just behind you. You have your photo at last!"
]

white_whale = ("white_whale", "Find the White Whale", "sea", 10, "Swimmer", (1, 0, 1, 5) )

class Journey():
    def __init__(self, title = '', XP = 10 appropriate_pet_type = '', plot = '', stats = (), progress = 0):
        self.title = title
        self.XP = XP
        self.appropriate_pet_type = appropriate_pet_type
        self.plot = plot
        self.stats = stats
        self.progress = progress
        self.step = 0

    def display_plot(self):
        current_place = plot[0:self.progress]
        [print(event) for event in current_place]

    def next_steps(self, value):
        self.step += value
        if self.step >= 3:
            self.progress_plot()
            self.step = self.step - 3

    def progress_plot(self):
        self.progress = += 1

    
