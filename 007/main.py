import os
import random
from hangman_words import word_list
from hangman_art import stages, logo
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ["_"] * word_length
lives = 6


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


print(logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    cls()

    if guess in display:
        print(f"You already guessed {guess}")

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print("You won")

    print(stages[lives])
