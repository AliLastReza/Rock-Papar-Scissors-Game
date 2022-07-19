import random

from rich import print
from rich.console import Console

from constants import GAME_CHOICES, INTRO, RULES, scoreboard

console = Console()


def get_user_choice():
    """get and validate player input, recursively"""
    user_input = input("Rock paper scissors shoot (Choices: r, p, s)\nYou: ")
    user_input = user_input.lower()
    if user_input not in GAME_CHOICES:
        print("[bold blue]Please enter a valid choice. choose between r, p, s.[/bold blue]")
        return get_user_choice()
    return user_input


def get_system_choice():
    """choice random from GAME_CHOICES"""
    return random.choice(GAME_CHOICES)


def find_winner(user, system):
    """
    receive user and system choices, sort them and compare with game rules if
    they are not the same.
    :param user:
    :param system:
    :return: winner
    """
    match = {user, system}

    if len(match) == 1:
        return None

    return RULES[tuple(sorted(match))]


def update_scoreboard(result):
    """
    Update scoreboard after each hand of the game and show live result
    until now + last hand result
    """
    if result["user"] == 3:
        scoreboard["user"] += 1
        msg = "You :)"
        text_color = "green"
    else:
        scoreboard["system"] += 1
        msg = "System :("
        text_color = "red"

    console.print("#" * 42)
    console.print("##", f'You: {scoreboard["user"]}'.ljust(36), "##")
    console.print("##", f'System: {scoreboard["system"]}'.ljust(36), "##")
    console.print("##", f"This round's winner: {msg}".ljust(36), "##", style=text_color)
    console.print("#" * 42)


def play():
    result = {"user": 0, "system": 0}

    while result["user"] < 3 and result["system"] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)

        if winner == user_choice:
            msg = f"You win :)"
            result["user"] += 1
            text_color = "green"
        elif winner == system_choice:
            msg = f"You lose :("
            result["system"] += 1
            text_color = "red"
        else:
            msg = "Draw"
            text_color = "gray"
        console.print(f"System: {system_choice}\nResult: [bold {text_color}]{msg}[bold /{text_color}]\n")

    update_scoreboard(result)

    play_again = input("Do you wanna play again? (y/n) ")
    if play_again.lower() == "y":
        print()
        return play()
    console.print("Hope you enjoyed the game!", style="bold green")


def main():
    """Main function to play the game"""
    console.print(INTRO)

    play()


if __name__ == "__main__":
    main()
