import random
import os
from art import logo

# Clearing the terminal after play a round of the game
def clear():
    os.system('clear')

# Randomly choose a card & 11 is the Ace
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Calculating scores
def calculate_score(list):
    """Calculating total score of the computer and user"""
    if sum(list) == 21 and len(list) == 2:
        return 0
    
    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
        
    return sum(list)

# Comparing the scores of the user and computer to determine the winner
def compare(user_score, computer_score):
    """Comparing the user's and computer's scores to declare a winner"""
    if user_score == computer_score:
        return "It's a draw." 
    elif computer_score == 0:
        return "The computer has a blackjack. The user loses."
    elif user_score == 0:
        return "The computer has a blackjack. The user wins."
    elif user_score > 21:
        return "The user loses."
    elif computer_score > 21:
        return "The user wins."
    elif user_score > computer_score:
        return "The user wins. "
    elif computer_score > user_score:
        return "The user loses."

def play_game():
    print(logo)
    # Deal 2 cards each using deal_card() and append()
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False

    while not is_game_over:
        user_total = calculate_score(user_cards)
        computer_total = calculate_score(computer_cards)

        print(f"   User's cards: {user_cards}, User's total: {user_total}")
        print(f"   Computer's first card: {computer_cards[0]}.")

        if user_total == 0 or computer_total == 0 or user_total > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to draw another card? type 'y' to get another card or type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_total != 0 and computer_total > 21:
        computer_cards.append(deal_card)
        computer_total = calculate_score(computer_cards)

    print(f"   The user's cards: {user_cards}. The user's final score: {user_total}")
    print(f"   The computer's cards: {computer_cards}. The computer's final score: {computer_total}")
    print(compare(user_score=user_total,computer_score=computer_total))

while input("Do you want to play Blackjack? 'y' or 'n' ") == "y":
    clear()
    play_game()