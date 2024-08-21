''' Create a program using a list which allows us to manage our to-do list
interactively, including adding tasks, marking tasks as done, removing tasks, and
viewing the current task. The tasks are stored in a list, where each task is represented
as a list containing the task name and a boolean value indicating whether it's done or
no '''


# To-Do List Manager

# Initialize the to-do list
todo_list = []

def add_task(task_name):
    """Add a new task to the to-do list."""
    todo_list.append([task_name, False])
    print(f"Task '{task_name}' added to the list.")

def mark_task_done(task_index):
    """Mark a task as done."""
    if 0 <= task_index < len(todo_list):
        todo_list[task_index][1] = True
        # [['car','true'],['bike','true']]
        print(f"Task '{todo_list[task_index][0]}' marked as done.")
    else:
        print("Invalid task index.")

def remove_task(task_index):
    """Remove a task from the to-do list."""
    if 0 <= task_index < len(todo_list):
        removed_task = todo_list.pop(task_index)
        print(f"Task '{removed_task[0]}' removed from the list.")
    else:
        print("Invalid task index.")

def view_tasks():
    """View the current tasks in the to-do list."""
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for i, (task_name, is_done) in enumerate(todo_list):
            status = "Done" if is_done else "Not Done"
            print(f"{i + 1}. {task_name} - {status}")

def main():
    """Main function """
    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. Mark a task as done")
        print("3. Remove a task")
        print("4. View tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task_name = input("Enter the task name: ")
            add_task(task_name)
        elif choice == '2':
            view_tasks()
            try:
                task_index = int(input("Enter the task number to mark as done: ")) - 1
                mark_task_done(task_index)
            except ValueError:
                print("Please enter a valid task number.")
        elif choice == '3':
            view_tasks()
            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                remove_task(task_index)
            except ValueError:
                print("Please enter a valid task number.")
        elif choice == '4':
            view_tasks()
        elif choice == '5':
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
