import random

# Define the cards and suits
cards = ["Ace", "King", "Queen", "Jack"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

# Define the exercise associated with each card
workout_key = {
    "Ace": "Heels to the Heaven",
    "King": "High Knees",
    "Queen": "Mountain Climbers",
    "Jack": "Jump Squats"
}

# Define the reps associated with each suit
suit_reps = {
    "Hearts": 15,
    "Diamonds": 12,
    "Clubs": 20,
    "Spades": 10
}

# Create a deck of 16 cards (4 of each type, each paired with a suit)
deck = [(card, suit) for card in cards for suit in suits]

# Shuffle the deck to randomize the order
random.shuffle(deck)

# Function to generate the next workout
def generate_next_workout():
    if deck:  # If there are cards left
        card, suit = deck.pop(0)  # Pop the first card from the deck
        exercise = workout_key[card]
        reps = suit_reps[suit]
        print(f"{card} of {suit}: {reps} {exercise}")
    else:
        print("No more combinations left.")
        exit()

# Function to refill and shuffle the deck when it's empty
def refill_deck():
    global deck
    # Refill the deck with all 16 unique combinations of card-suits and shuffle
    deck = [(card, suit) for card in cards for suit in suits]
    random.shuffle(deck)

# Main loop to generate the next workout on Enter press

while True:
    input("Next...\n")
    generate_next_workout()
    print("\n---------------------\n")
