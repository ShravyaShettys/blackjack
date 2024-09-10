import random

# Function to deal a card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Function to calculate the score of the cards
def calculate_score(cards):
    # Check for blackjack (a hand with only 2 cards: ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Check for ace (11), if the score is over 21, replace 11 with 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Initializing the user and computer cards
user_cards = []
computer_cards = []

# Deal two cards to both the user and the computer
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# Step 6: Calculate the scores
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

# Check for game over conditions
is_game_over = False

if user_score == 0 or user_score > 21:
    is_game_over = True

# Print the user's cards and score, and the computer's first card
print(f"Your cards are {user_cards} and your score is {user_score}")
print(f"Computer's first card is {computer_cards[0]}")
