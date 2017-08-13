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
    "Fight": "Fight!",
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
    "4": ("4", "Fight","Back","Exit"),
    "5": ("5","Back", "Exit"),
    "6": ("6","Back", "Exit"),
    "7": ("7","Back", "Exit")
}

npc = {
    "GameMaster": ("1")
}
