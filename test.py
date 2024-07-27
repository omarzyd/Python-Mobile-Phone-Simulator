message="""1- Write a new note
2- View your notes
3- Quit"""
notes=[]
def choose_123():
    x=input("")
    while True:
        if x in ['1','2','3']:
            return x
        else:
            print("choose from 1,2 and 3 only")
            x=input("Enter your choice again : ")
            print("_"*30)
def write_note():
    note=input("Write your note here \n")
    notes.append(note)
    print("Your note has been saved successfully ✅")
    print("_" * 30)
    file=open("Notes.txt","a")
    file.writelines(note)
def view_notes():
    for i in range(len(notes)):
        print(f'{i+1}- {notes[i]}')
    print("_" * 30)
def main_notes():
    while True:
        print(message)
        print("_" * 30)
        choice=choose_123()
        if choice=='1':
            write_note()
        elif choice=='2':
            view_notes()
        elif choice=='3':
            print("Existing the app 🔃")
            break
if __name__=="__notes__":
    main_notes()