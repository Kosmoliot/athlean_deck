import tkinter as tk
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

# Set up the GUI
root = tk.Tk()
root.geometry("300x200")
root.title("Card Workout Generator")

# Workout text area
workout_text = tk.StringVar()
workout_label = tk.Label(root, textvariable=workout_text, justify="left")
workout_label.pack(pady=10)

# Function to generate the next workout
def generate_next_workout():
    if deck:  # If there are cards left
        card, suit = deck.pop(0)  # Pop the first card from the deck
        exercise = workout_key[card]
        reps = suit_reps[suit]
        workout_text.set(f"{card} of {suit}: {reps} {exercise}")
    else:
        workout_text.set("No more combinations left.")
        exit()

# Generate button
generate_button = tk.Button(root, text="Generate Workout", command=generate_next_workout)
generate_button.pack(pady=20)

# Run the application
root.mainloop()
