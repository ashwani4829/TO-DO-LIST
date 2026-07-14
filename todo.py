from tkinter import *
from tkinter import messagebox

# ---------- Functions ----------

def add_task():
    task = task_entry.get()

    if task != "":
        task_listbox.insert(END, task)

        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

        task_entry.delete(0, END)

    else:
        messagebox.showwarning("Warning", "Please enter a task!")


def delete_task():

    try:
        selected = task_listbox.curselection()[0]

        task_listbox.delete(selected)

        save_tasks()

    except:
        messagebox.showwarning("Warning", "Select a task first!")


def save_tasks():

    tasks = task_listbox.get(0, END)

    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():

    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

            for task in tasks:
                task_listbox.insert(END, task.strip())

    except FileNotFoundError:
        open("tasks.txt", "w").close()

# ---------- GUI ----------

root = Tk()

root.title("To-Do List App")

root.geometry("450x500")

root.resizable(False, False)

title_label = Label(
    root,
    text="My To-Do List",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=10)

task_entry = Entry(
    root,
    font=("Arial", 14),
    width=30
)

task_entry.pack(pady=10)

add_button = Button(
    root,
    text="Add Task",
    width=15,
    command=add_task
)

add_button.pack(pady=5)

delete_button = Button(
    root,
    text="Delete Task",
    width=15,
    command=delete_task
)

delete_button.pack(pady=5)

task_listbox = Listbox(
    root,
    width=40,
    height=15,
    font=("Arial", 12)
)

task_listbox.pack(pady=20)

load_tasks()

root.mainloop()