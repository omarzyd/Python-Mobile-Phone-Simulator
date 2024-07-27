import tkinter as tk
from tkinter import simpledialog, messagebox
import random

def get_user_choice():
    return simpledialog.askstring("Input", "Enter your choice (rock, paper, scissors):").lower()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    root = tk.Tk()
    root.title("Rock Paper Scissors")

    def start_game():
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        messagebox.showinfo("Result", f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}")

    tk.Button(root, text="Play", command=start_game, width=20).pack(pady=10)
    tk.Button(root, text="Quit", command=root.quit, width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    play_game()
