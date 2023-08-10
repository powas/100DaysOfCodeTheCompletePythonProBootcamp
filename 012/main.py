from art import logo
import random

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5


def difficulty():
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
        return EASY_DIFFICULTY
    else:
        return HARD_DIFFICULTY


def check_answer(guess, the_number, lives):
    """Checks answer agains guess. Returns the number of turns remaining"""
    if guess == the_number:
        print(f"You got it! The answer was {the_number}.")
    elif guess < the_number:
        print("Too low.")
        return lives - 1
    elif guess > the_number:
        print("Too high.")
        return lives - 1


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    the_number = random.randint(1, 100)
    print(f"Pssst, the correct answer is {the_number}")
    lives = difficulty()
    guess = 0

    while not guess == the_number:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        lives = check_answer(guess, the_number, lives)
        if lives == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != the_number:
            print("Guess again")



game()
