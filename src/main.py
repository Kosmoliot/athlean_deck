import tkinter as tk
import random

# Define card deck and workout key
deck = ["Ace", "King", "Queen", "Jack"] * 4  # 16 cards (4 of each)
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
workout_key = {
    "Ace": "Push-ups",
    "King": "Squats",
    "Queen": "Lunges",
    "Jack": "Burpees"
}
suit_reps = {
    "Hearts": 10,
    "Diamonds": 15,
    "Clubs": 20,
    "Spades": 25
}

# Shuffle deck of cards
cards = [(card, suit) for card in deck for suit in suits]
random.shuffle(cards)

# Function to generate the workout
def generate_workout():
    # Reset workout text
    workout_details = "Workout:\n"
    
    # Loop through shuffled cards and add workout details
    for card, suit in cards:
        exercise = workout_key[card]
        reps = suit_reps[suit]
        workout_details += f"{card} of {suit}: {reps} {exercise}\n"
    
    # Update the workout text variable with the generated workout
    workout_text.set(workout_details)

# Set up the GUI
root = tk.Tk()
root.title("Card Workout Generator")

# Workout text area
workout_text = tk.StringVar()
workout_label = tk.Label(root, textvariable=workout_text, justify="left")
workout_label.pack(pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate Workout", command=generate_workout)
generate_button.pack(pady=20)

# Run the application
root.mainloop()