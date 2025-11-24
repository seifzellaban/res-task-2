import os

# The name of the file used to store tasks
FILE_NAME = "tasks.txt"


def load_tasks():
    """
    Reads the 'tasks.txt' file and returns a list of tasks.
    Initializes the file if it doesn't exist.
    """
    tasks = []

    # Check if the file exists. If not, we start with an empty list.
    if not os.path.exists(FILE_NAME):
        return tasks  # Return the empty list

    # Open the file in 'read' mode ('r') using the 'with' statement for safe handling
    try:
        with open(FILE_NAME, "r") as file:
            # Loop through the lines in the file
            for line in file:
                # Strip the newline character ('\n') and any extra whitespace
                task = line.strip()
                if task:  # Only add non-empty lines
                    tasks.append(task)
    except IOError as e:
        print(f"Error loading file: {e}")
        # In case of read error, we proceed with an empty list
        return []

    return tasks


def save_task(task):
    """
    Appends a SINGLE new task to the file.
    """
    # Open the file in 'append' mode ('a')
    # This adds content to the end without deleting existing content.
    try:
        with open(FILE_NAME, "a") as file:
            # Write the task to the file, ensuring a newline character is added
            file.write(task + "\n")
    except IOError as e:
        print(f"Error saving task: {e}")


def rewrite_file(tasks):
    """
    Overwrites the ENTIRE file with the current list of tasks.
    Used when a task is deleted to sync the changes to disk.
    """
    # Open the file in 'write' mode ('w'). This wipes the file clean first.
    try:
        with open(FILE_NAME, "w") as file:
            # Loop through the 'tasks' list in memory
            for task in tasks:
                # Write each task back to the file, followed by a newline
                file.write(task + "\n")
    except IOError as e:
        print(f"Error rewriting file: {e}")


def view_tasks(tasks):
    """
    Prints the list of tasks with index numbers for user reference.
    """
    print("\n--- Your To-Do List ---")

    # Check if the list is empty
    if not tasks:
        print("Your list is empty! Add a new task.")
        return

    # Loop through tasks using enumerate() to get the index (starting at 1)
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print("-" * 25)


def delete_task(tasks):
    """
    Displays tasks, asks the user which number to delete, updates the list, and saves to file.
    """
    # Display current tasks to help the user choose
    view_tasks(tasks)

    if not tasks:
        return

    try:
        # Ask user for the number to delete
        task_num_str = input

        # Validate input: check if the number is within a valid range
        if 0 <= task_index < len(tasks):
            # Remove the item from the 'tasks' list in memory
            deleted_task = tasks.pop(task_index)

            # Sync changes to disk by rewriting the entire file
            rewrite_file(tasks)
            print(f"\nTask deleted: '{deleted_task}'")
        else:
            print("\nInvalid task number. Please try again.")

    except ValueError:
        print("\nInvalid input. Please enter a number.")


def main():
    print("Welcome to the Terminal To-Do App!")

    # Load existing tasks from file into memory at startup
    current_tasks = load_tasks()

    while True:
        print("\n--- Menu ---")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Delete a Task")
        print("4. Exit")
        print("-" * 12)

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter new task description: ")
            if task:
                current_tasks.append(task)
                save_task(task)
                print(f"Task added: '{task}'")

        elif choice == "2":
            view_tasks(current_tasks)

        elif choice == "3":
            delete_task(current_tasks)

        elif choice == "4":
            print("Goodbye, Seif! Have a productive day.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
