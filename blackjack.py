import random

# Function to deal a card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)  # Corrected syntax
    return card

# Function to calculate the score of the cards
def calculate_score(cards):
    # Check for blackjack (a hand with only 2 cards: ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 will represent a blackjack
    # Check for ace (11), if the score is over 21, replace 11 with 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Function to compare scores and determine the outcome
def compare(u_Score, c_Score):
    if u_Score == c_Score:
        return "It's a draw"
    elif c_Score == 0:
        return "You lose, opponent has a blackjack"
    elif u_Score == 0:
        return "You win with a blackjack"
    elif u_Score > 21:
        return "You lose, you went over 21"
    elif c_Score > 21:
        return "You win, opponent went over 21"
    elif u_Score > c_Score:
        return "You win"
    else:
        return "You lose"

# Initializing the user and computer cards
user_cards = []
computer_cards = []

# Deal two cards to both the user and the computer
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# Game loop
is_game_over = False
while not is_game_over:
    # Calculate the scores
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # Check for game over conditions
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

# Computer's turn: keep drawing cards until the score is at least 17 or it gets a blackjack
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

# Compare final scores
print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))
