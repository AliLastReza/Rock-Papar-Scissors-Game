import random

from constants import GAME_CHOICES, INTRO, RULES, scoreboard


def get_user_choice():
    """get and validate player input, recursively"""
    user_input = input("Rock paper scissors shoot (r, p, s)\nYou: ")
    if user_input not in GAME_CHOICES:
        print("Please enter a valid choice. choose between r, p, s.")
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
        msg = "You"
    else:
        scoreboard["system"] += 1
        msg = "System"

    print("#" * 34)
    print("##", f'You: {scoreboard["user"]}'.ljust(28), "##")
    print("##", f'System: {scoreboard["system"]}'.ljust(28), "##")
    print("##", f"This round's winner: {msg}".ljust(28), "##")
    print("#" * 34)


def play():
    result = {"user": 0, "system": 0}

    while result["user"] < 3 and result["system"] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)

        if winner == user_choice:
            msg = "You win :)"
            result["user"] += 1
        elif winner == system_choice:
            msg = "You lose :("
            result["system"] += 1
        else:
            msg = "Draw"
        print(f"System: {system_choice}\nResult: {msg}\n")

    update_scoreboard(result)

    play_again = input("Do you wanna play again? (y/n) ")
    if play_again == "y":
        print()
        return play()
    print("Hope you enjoyed the game!")


def main():
    """Main function to play the game"""
    print(INTRO)

    play()


if __name__ == "__main__":
    main()
