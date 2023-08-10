import os
from art import logo


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


bids = {}
should_continue = True
print(logo)
print("Welcome to the secret auction program.")


def finding_highest_bidder(bidding_record):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidding_record:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


while should_continue:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    more_bitters = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bitters == "no":
        should_continue = False
        finding_highest_bidder(bids)
    elif more_bitters == "yes":
        cls()
