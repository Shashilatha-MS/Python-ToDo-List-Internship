
# To-Do List CLI App
# CodeOrbit Tech - Python Programming Internship

import os

FILE_NAME = "tasks.txt"


def load_tasks():
    """Load saved tasks from the text file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file if line.strip()]
    return []


def save_tasks(tasks):
    """Save tasks to the text file."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    """Display all tasks with numbers."""
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\n--- YOUR TO-DO LIST ---")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")


def add_task(tasks):
    """Add a new task."""
    task = input("Enter your new task: ").strip()

    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def remove_task(tasks):
    """Remove a task using its number."""
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to remove: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    """Display the menu and run the application."""
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST APP =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Thank you for using the app!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
