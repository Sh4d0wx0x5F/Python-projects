logo = """


 ________  ___  ___  _______   ________   ________      
|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\     
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|_    
 \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \   
  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \  
   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \ 
    \|_______|\|_______|\|_______|\_________\\_________\
                                 \|_________\|_________|

"""
from random import randint

easy_level = 10
hard_level = 5


def check_answer(guess, AI, turns):
    if guess > AI:
        print("Too high")
        return turns - 1
    elif guess < AI:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it right! The answer was {AI}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_level
    elif level == "hard":
        return hard_level


def game():
    print(logo)

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    AI = randint(1, 100)

    turns = set_difficulty()

    guess = 0

    while guess != AI:

        print(f"You have {turns} attempts remaining to guess the number")

        guess = int(input("Make a guess: "))
        turns = check_answer(guess, AI, turns)

        if turns == 0:
            print("You 've run out of guesses, you lose.")
            return
        elif turns != 0:
            print("Guess again")


game()
