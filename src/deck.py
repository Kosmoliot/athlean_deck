# import tkinter as tk
# import random

# # Define card deck and workout key
# deck = ["Ace", "King", "Queen", "Jack"] * 4  # 16 cards (4 of each)
# suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
# workout_key = {
#     "Ace": "Push-ups",
#     "King": "Squats",
#     "Queen": "Lunges",
#     "Jack": "Burpees"
# }
# suit_reps = {
#     "Hearts": 10,
#     "Diamonds": 15,
#     "Clubs": 20,
#     "Spades": 25
# }

# # Shuffle deck of cards
# cards = [(card, suit) for card in deck for suit in suits]
# random.shuffle(cards)

# # Function to generate the workout
# def generate_workout():
#     # Reset workout text
#     workout_details = "Workout:\n"
    
#     # Loop through shuffled cards and add workout details
#     for card, suit in cards:
#         exercise = workout_key[card]
#         reps = suit_reps[suit]
#         workout_details += f"{card} of {suit}: {reps} {exercise}\n"
    
#     # Update the workout text variable with the generated workout
#     workout_text.set(workout_details)

# # Set up the GUI
# root = tk.Tk()
# root.title("Card Workout Generator")

# # Workout text area
# workout_text = tk.StringVar()
# workout_label = tk.Label(root, textvariable=workout_text, justify="left")
# workout_label.pack(pady=10)

# # Generate button
# generate_button = tk.Button(root, text="Generate Workout", command=generate_workout)
# generate_button.pack(pady=20)

# # Run the application
# root.mainloop()

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
