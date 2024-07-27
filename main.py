import contacts
import Hangman
import notes
import rps
import todo
import weather

def main_menu():
    while True:
        print("Welcome to the Mobile Phone Simulator!")
        print("Please select an option:")
        print("1. To-Do List")
        print("2. Notes")
        print("3. Contacts")
        print("4. Games")
        print("5. Weather")
        print("6. Shutdown Phone")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo.main_todolist()
        elif choice == '2':
            notes.main_notes()
        elif choice == '3':
            contacts.main_contacts()
        elif choice == '4':
            games_menu()
        elif choice == '5':
            weather.weather_menu()  # Ensure this calls the correct function
        elif choice == '6':
            print("Shutting down the phone...")
            break
        else:
            print("Invalid choice. Please try again.")

def games_menu():
    while True:
        print("Games Menu")
        print("1. Hangman")
        print("2. Rock Paper Scissors")
        print("3. Back to Main Menu")

        game_choice = input("Enter your choice: ")

        if game_choice == '1':
            Hangman.hangman()
        elif game_choice == '2':
            rps.play_game()
        elif game_choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
