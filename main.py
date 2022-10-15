import random


def main():
    options = ['rock', 'paper', 'scissors']
    computer_choice = options[random.randint(0, 2)]

    welcome_message = """
    WELCOME TO THE ROCK-PAPER-SCISSORS PYTHON GAME
    🧱🧻✂️
    
    1. ROCK
    2. PAPER
    3. SCISSORS
    """

    print(welcome_message)

    try:
        user_choice = int(input('Please select an option: '))

        while (user_choice != 1) and (user_choice != 2) and (user_choice != 3):
            user_choice = int(input('Please select an option from 1 to 3: '))

        print(game_logic(
            user_choice=user_choice,
            computer_choice=computer_choice,
            options=options)
        )
    except ValueError:
        print('You can only use an option from 1 to 3, Please restart the game.')


def game_logic(user_choice, computer_choice, options):
    TIE = 'TIE'
    LOSE = 'LOSE'
    WIN = 'WIN'
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'

    if user_choice == 1:
        user_choice = ROCK
        print(f'YOU: {user_choice} vs PC: {computer_choice}')

        if computer_choice == options[0]:
            return TIE
        if computer_choice == options[1]:
            return LOSE
        if computer_choice == options[2]:
            return WIN

    if user_choice == 2:
        user_choice = PAPER
        print(f'YOU: {user_choice} vs PC: {computer_choice}')

        if computer_choice == options[0]:
            return WIN
        if computer_choice == options[1]:
            return TIE
        if computer_choice == options[2]:
            return LOSE

    if user_choice == 3:
        user_choice = SCISSORS
        print(f'YOU: {user_choice} vs PC: {computer_choice}')

        if computer_choice == options[0]:
            return LOSE
        if computer_choice == options[1]:
            return WIN
        if computer_choice == options[2]:
            return TIE


if __name__ == "__main__":
    main()
