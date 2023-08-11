import random
from game_data import data
from art import logo, vs
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def generator(data):
    """Generates a random item from list"""
    random_item = random.choice(data)
    return random_item


def check_answer(guess, item_a, item_b):
    """Takes the guess and the follower count and compares if is correct"""
    if item_a["follower_count"] > item_b["follower_count"]:
        return guess == "a"
    else:
        return guess == "b"


def game():
    game_should_continue = True
    score = 0
    item_a = generator(data)
    item_b = generator(data)
    print(logo)
    while game_should_continue:
        while item_b == item_a:
            item_b = generator(data)
        print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}.")
        print(vs)
        print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(guess, item_a, item_b)
        cls()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            item_a = item_b
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
