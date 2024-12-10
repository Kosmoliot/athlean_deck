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
root.geometry("400x200")
root.configure(bg="grey")
root.title("Card Workout Generator")

# Workout text area using Text widget
workout_text = tk.Text(root, width=40, height=3, wrap="word", bg="grey")
workout_text.tag_configure("center", justify="center")
workout_text.pack(pady=10)

# Update the workout text in the Text widget
def generate_next_workout():
    if deck:  # If there are cards left
        card, suit = deck.pop(0)  # Pop the first card from the deck
        exercise = workout_key[card]
        reps = suit_reps[suit]
        workout_text.delete(1.0, tk.END)  # Clear previous text
        workout_text.insert(tk.END, f"{card} of {suit}: {reps} {exercise}", "center")
    else:
        workout_text.delete(1.0, tk.END)
        workout_text.insert(tk.END, "No more combinations left.", "center")

# Generate button
generate_button = tk.Button(
    root, 
    text="Generate Workout", 
    command=generate_next_workout, 
    highlightthickness=0, 
    borderwidth=0, 
    relief="flat",
    bg="grey",   # Match button background to the root background
    fg="black",  # Set text color if desired for contrast
    highlightbackground="grey",  # Match to background to remove shadow
    highlightcolor="grey"        # Match to background to remove shadow
)
generate_button.pack(padx=(20, 20), pady=20, fill="both")  # Make button resize with window

# Run the application
root.mainloop()