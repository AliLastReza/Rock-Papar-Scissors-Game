GAME_TITLE = "Rock Paper Scissors"
INTRO = f"""
Hello, and welcome to the {GAME_TITLE} Game!
The game is simple, you can choose between rock, paper and scissors.
Every time you and computer will choose one of these three.
Enter 'r' for 'rock', 'p' for 'paper' or 's' for 'scissors'.

Ok, let's start the game!
"""

GAME_CHOICES = ("r", "p", "s")  # Rock, Paper, Scissors


RULES = {
    ('p', 'r'): 'p',
    ('p', 's'): 's',
    ('r', 's'): 'r',
}


scoreboard = {
    'user': 0,
    'system': 0
}




PLAYER_OPTIONS = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}


CONTROL_OPTIONS = {'e': 'Exit', 'c': 'Clear'}


GAME_RULES = {
    'r': {'r': 0, 'p': -1, 's': 1},
    'p': {'r': 1, 'p': 0, 's': -1},
    's': {'r': -1, 'p': 1, 's': 0}
}


RESULT_BANNER = {
    1: "You Won",
    0: "Draws",
    -1: "You Lost"
}
