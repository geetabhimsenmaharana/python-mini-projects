# day4_todo_app.py

# List to store tasks
tasks = []

def add_task():
    task_name = input("Enter the task name: ")
    tasks.append({"name": task_name, "status": "Pending"})
    print(f"✅ Task '{task_name}' added!")

def view_tasks():
    if not tasks:
        print("📋 No tasks yet!")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} [{task['status']}]")
    print("------------------")

def update_task():
    if not tasks:
        print("📋 No tasks to update!")
        return
    view_tasks()
    try:
        task_number = int(input("Enter task number to update: "))
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            print(f"Current task: {task['name']} [{task['status']}]")
            choice = input("Mark as Completed (c) or Edit name (e)? ").lower()
            if choice == "c":
                task["status"] = "Completed"
                print(f"✅ Task '{task['name']}' marked as Completed!")
            elif choice == "e":
                new_name = input("Enter new task name: ")
                task["name"] = new_name
                print(f"✏️ Task updated to '{new_name}'")
            else:
                print("❌ Invalid option")
        else:
            print("❌ Invalid task number")
    except ValueError:
        print("❌ Enter a valid number!")

def delete_task():
    if not tasks:
        print("📋 No tasks to delete!")
        return
    view_tasks()
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            task = tasks.pop(task_number - 1)
            print(f"🗑️ Task '{task['name']}' deleted!")
        else:
            print("❌ Invalid task number")
    except ValueError:
        print("❌ Enter a valid number!")

def main():
    while True:
        print("\n===== TO-DO APP =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting the app. Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    main()