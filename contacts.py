import tkinter as tk
from tkinter import simpledialog, messagebox

contacts = []

def add_contact():
    name = simpledialog.askstring("Input", "Enter Name:")
    phone_number = simpledialog.askstring("Input", "Enter Phone Number:")
    email = simpledialog.askstring("Input", "Enter Email:")
    if name and phone_number and email:
        contact_info = {"Name": name, "Phone number": phone_number, "Email": email}
        contacts.append(contact_info)
        with open("Contacts.txt", "a") as file:
            file.write(f"{name} | {phone_number} | {email}\n")
        messagebox.showinfo("Info", "Contact added successfully")

def view_contacts():
    if contacts:
        contact_list = "\n".join([f'{i+1}. {contact["Name"]} | {contact["Phone number"]} | {contact["Email"]}' for i, contact in enumerate(contacts)])
        messagebox.showinfo("Contacts", contact_list)
    else:
        messagebox.showinfo("Info", "You have no contacts to view")

def main_contacts():
    root = tk.Tk()
    root.title("Contacts")

    tk.Button(root, text="Add Contact", command=add_contact, width=20).pack(pady=10)
    tk.Button(root, text="View Contacts", command=view_contacts, width=20).pack(pady=10)
    tk.Button(root, text="Quit", command=root.quit, width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_contacts()
