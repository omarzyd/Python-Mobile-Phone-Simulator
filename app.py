import tkinter as tk
from tkinter import messagebox

class MobilePhoneSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mobile Phone Simulator")
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Welcome to the Mobile Phone Simulator!", font=("Helvetica", 16)).pack(pady=20)

        tk.Button(self.root, text="To-Do List", command=self.open_todo_list, width=20).pack(pady=10)
        tk.Button(self.root, text="Notes", command=self.open_notes, width=20).pack(pady=10)
        tk.Button(self.root, text="Contacts", command=self.open_contacts, width=20).pack(pady=10)
        tk.Button(self.root, text="Games", command=self.open_games_menu, width=20).pack(pady=10)
        tk.Button(self.root, text="Weather", command=self.open_weather, width=20).pack(pady=10)
        tk.Button(self.root, text="Shutdown Phone", command=self.root.quit, width=20).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def open_todo_list(self):
        self.clear_window()
        import todo
        todo.main_todolist()

    def open_notes(self):
        self.clear_window()
        import notes
        notes.main_notes()

    def open_contacts(self):
        self.clear_window()
        import contacts
        contacts.main_contacts()

    def open_games_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Games Menu", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self.root, text="Hangman", command=self.play_hangman, width=20).pack(pady=10)
        tk.Button(self.root, text="Rock Paper Scissors", command=self.play_rps, width=20).pack(pady=10)
        tk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu, width=20).pack(pady=10)

    def play_hangman(self):
        self.clear_window()
        import Hangman
        Hangman.hangman()

    def play_rps(self):
        self.clear_window()
        import rps
        rps.play_game()

    def open_weather(self):
        self.clear_window()
        import weather
        weather.weather_menu()

if __name__ == "__main__":
    root = tk.Tk()
    app = MobilePhoneSimulatorApp(root)
    root.mainloop()
