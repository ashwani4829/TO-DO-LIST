# ✅ To-Do List App

A simple and user-friendly **To-Do List Application** built using **Python** and **Tkinter**. This desktop application allows users to efficiently manage their daily tasks by adding, deleting, and automatically saving tasks for future use.

---

## 🚀 Features

- ➕ Add new tasks
- ❌ Delete completed tasks
- 💾 Automatically save tasks to a file
- 📂 Load saved tasks on application startup
- 🖥️ Simple and interactive Graphical User Interface (GUI)
- ⚡ Lightweight and beginner-friendly

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter (GUI Library)**
- **File Handling**

---

## 📁 Project Structure

```text
ToDo_List_App/
│
├── todo.py
├── tasks.txt
├── README.md
└── screenshots/
    └── app.png
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/todo-list-app.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd todo-list-app
```

### 3️⃣ Run the Application

```bash
python todo.py
```

---

## ▶️ How to Use

### ➕ Add a Task

1. Type a task into the input field.
2. Click the **Add Task** button.
3. The task will appear in the list.
4. The task is automatically saved in **tasks.txt**.

### ❌ Delete a Task

1. Select a task from the list.
2. Click the **Delete Task** button.
3. The selected task will be removed from both the application and the saved file.

---

## 📸 Screenshots

Place screenshots inside the **screenshots** folder.

Example:

```text
screenshots/
│
└── app.png
```

---

## 🔍 How It Works

### Adding Tasks

- User enters a task.
- Task is added to the Listbox.
- Task is saved in **tasks.txt**.

### Deleting Tasks

- User selects a task.
- Selected task is removed.
- The task file is automatically updated.

### Saving Tasks

All tasks are stored in a text file:

```text
tasks.txt
```

Example:

```text
Study Python
Complete Assignment
Buy Milk
Exercise
```

### Loading Tasks

When the application starts:

- Reads tasks from **tasks.txt**
- Displays all saved tasks in the Listbox

---

## 📊 Example Workflow

### Step 1: Add Tasks

```text
Study Python
Buy Milk
Exercise
```

### Step 2: Application Displays

```text
Study Python
Buy Milk
Exercise
```

### Step 3: Delete a Task

```text
Buy Milk
```

### Step 4: Updated Task List

```text
Study Python
Exercise
```

---

## 🧠 Concepts Used

- Python Functions
- Tkinter GUI
- Labels
- Buttons
- Entry Widgets
- Listbox
- Event Handling
- File Handling
- Exception Handling

---

## 🎯 Learning Outcomes

This project helps in understanding:

- Desktop GUI development using Tkinter
- Event-driven programming
- File handling in Python
- User input processing
- Data persistence
- Building beginner-friendly desktop applications

---

## 🧪 Sample Output

```text
+----------------------------------+
|         My To-Do List            |
|                                  |
| [__________________________]     |
|                                  |
|      [ Add Task ]                |
|                                  |
|    [ Delete Task ]               |
|                                  |
| Study Python                     |
| Buy Milk                         |
| Exercise                         |
|                                  |
+----------------------------------+
```

---

## 🚀 Future Enhancements

- ✏️ Edit existing tasks
- ⭐ Task priorities
- 📅 Due dates
- 🌙 Dark mode
- 📂 Task categories
- 🔔 Notifications and reminders
- 🗄️ SQLite database integration
- 🔍 Search tasks

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project for educational and personal purposes.

---

## 👨‍💻 Author

**Ashwani Dwivedi**

Python Internship Project • 2026

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub. It motivates me to build more Python projects and share them with the community.
