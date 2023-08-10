import random
# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
options = [rock, paper, scissors]
user_choice = int(input("What do you Choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice < 0 or user_choice > 2:
    print("That is not a valid option, you lose!")
else:
    print(options[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{options[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == computer_choice + 1 or user_choice == computer_choice - 2:
        print("You win!")
    else:
        print("You lose!")
