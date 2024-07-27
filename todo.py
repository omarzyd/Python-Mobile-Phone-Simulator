import tkinter as tk
from tkinter import simpledialog, messagebox

tasks = []

def add_task():
    task = simpledialog.askstring("Input", "Enter task:")
    if task:
        tasks.append({"task": task, "completed": False})
        messagebox.showinfo("Info", f'You added a new task successfully\n{task}')

def mark_task():
    incomplete_tasks = [task for task in tasks if not task["completed"]]
    if incomplete_tasks:
        task_list = "\n".join([f'{i+1}. {task["task"]}' for i, task in enumerate(incomplete_tasks)])
        task_num = simpledialog.askinteger("Input", f"Enter the task number to mark as finished:\n{task_list}")
        if task_num and 1 <= task_num <= len(incomplete_tasks):
            incomplete_tasks[task_num-1]["completed"] = True
            messagebox.showinfo("Info", f'{incomplete_tasks[task_num-1]["task"]} ✔')
        else:
            messagebox.showerror("Error", "Please choose from the available tasks")
    else:
        messagebox.showinfo("Info", "You have no incomplete tasks")

def view_tasks():
    if tasks:
        task_list = "\n".join([f'{i+1}. {task["task"]}, {"✔" if task["completed"] else "❌"}' for i, task in enumerate(tasks)])
        messagebox.showinfo("Tasks", task_list)
    else:
        messagebox.showinfo("Info", "You have no tasks to view")

def main_todolist():
    root = tk.Tk()
    root.title("To-Do List")

    tk.Button(root, text="Add Task", command=add_task, width=20).pack(pady=10)
    tk.Button(root, text="Mark Task as Completed", command=mark_task, width=20).pack(pady=10)
    tk.Button(root, text="View Tasks", command=view_tasks, width=20).pack(pady=10)
    tk.Button(root, text="Quit", command=root.quit, width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_todolist()
