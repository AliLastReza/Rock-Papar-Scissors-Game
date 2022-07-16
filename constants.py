GAME_TITLE = "Rock Paper Scissors"
INTRO = f"""
Hello, and welcome to the [bold magenta]{GAME_TITLE}[/bold magenta] Game!
The game is simple, you can [u green]choose between rock, paper and scissors[/u green].
Every time you and computer will choose one of these three.
Enter 'r' for 'rock', 'p' for 'paper' or 's' for 'scissors'.

Ok, [red]let's start the game![/red]
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
