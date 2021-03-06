# colors are a tuple with RGB values
colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)
}

config = {
    "caption": "Text Adventure Game, My Dude!",
    "display_height": 1000,
    "display_width": 1000,
    "FPS": 60
}

dialog = {
    "1": "Welcome to T E X T B O Y S",
    "2": "Go forth!",
    "3": "You find yourself in a forest clearing. Where would you like to go?",
    "4": "Grassy Plains",
    "5": "Friendly Forest",
    "6": "Clumpy Cliffs",
    "7": "Town",
    "8": "You are fighting a wild Beefsteak!",
    "9": "You see some friendly chipmunks.",
    "10": "You find some scorpions, but they do not really do anything.",
    "11": "I do not even know",
    "Fight": "Fight!",
    "Attack": "Attack!",
    "Defend": "Defend!",
    "Explore": "Explore!",
    "Exit": "Exit",
    "Back": "Back"
}

"""
In the dialog_options, the tuple represents the following in order:
[0] - Dialog line
[1+] - Dialog options
"""
dialog_options = {
    "1": ("1", "2"),
    "2": ("3", "4", "5", "6", "7"),
    "4": ("4", "Fight", "Back", "Exit"),
    "5": ("5", "Explore", "Back", "Exit"),
    "6": ("6", "Back", "Exit"),
    "7": ("7", "Back", "Exit"),
    "8": ("8", "Attack", "Back"),
    "9": ("9", "Back"),
    "10": ("10", "Back"),
    "11": ("11", "Back")
}

locations = {
    "1": "Grassy Plains",
    "2": "Friendly Forest"
}

events = {
    "1": ("9", "10", "11")
}

npc = {
    "GameMaster": ("1")
}
