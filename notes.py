import tkinter as tk
from tkinter import simpledialog, messagebox

notes = []

def add_note():
    note = simpledialog.askstring("Input", "Write your note here:")
    if note:
        notes.append(note)
        with open("Notes.txt", "a") as file:
            file.writelines(note + "\n")
        messagebox.showinfo("Info", "Your note has been saved successfully ✅")

def view_notes():
    if notes:
        note_list = "\n".join([f'{i+1}. {note}' for i, note in enumerate(notes)])
        messagebox.showinfo("Notes", note_list)
    else:
        messagebox.showinfo("Info", "You have no notes to view")

def main_notes():
    root = tk.Tk()
    root.title("Notes")

    tk.Button(root, text="Add Note", command=add_note, width=20).pack(pady=10)
    tk.Button(root, text="View Notes", command=view_notes, width=20).pack(pady=10)
    tk.Button(root, text="Quit", command=root.quit, width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_notes()
