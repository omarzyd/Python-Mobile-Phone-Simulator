import tkinter as tk
from tkinter import simpledialog, messagebox
import random

def choose_word():
    with open("RandomWords.txt", "r") as file:
        words = file.readlines()
    return random.choice(words).strip()

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    root = tk.Tk()
    root.title("Hangman")
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    def guess_letter():
        nonlocal attempts
        guess = simpledialog.askstring("Input", "Guess a letter:").lower()
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Error", "Please enter a single alphabetical character.")
            return
        if guess in guessed_letters:
            messagebox.showinfo("Info", "You already guessed that letter. Try again.")
            return
        guessed_letters.append(guess)
        if guess not in secret_word:
            attempts -= 1
            messagebox.showinfo("Info", f"Wrong guess! Attempts left: {attempts}")
        current_display = display_word(secret_word, guessed_letters)
        if "_" not in current_display:
            messagebox.showinfo("Info", f"Congratulations! You guessed the word: {secret_word}")
            root.quit()
        elif attempts == 0:
            messagebox.showinfo("Info", f"Out of attempts! The word was: {secret_word}")
            root.quit()

    tk.Button(root, text="Guess a Letter", command=guess_letter, width=20).pack(pady=10)
    tk.Button(root, text="Quit", command=root.quit, width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    hangman()
