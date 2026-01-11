# Code a Personal Planner that saves its data 
# to a file. You will need to use file io to achieve this

import os

# Constants for file handling
FILENAME = "tasks.txt"  # Name of the file to store tasks
FILEPATH = os.getcwd()  # Get the current working directory
FULLPATH = os.path.join(FILEPATH, FILENAME)  # Construct the full path for the task file

# Function to create a new task file
def create_new_file(fullpath):
    """
    Creates a new task file if it does not already exist.
    If the file exists, it notifies the user.
    """
    print("\nOK, creating a new task file...")
    if os.path.exists(fullpath):
        print("File [{}] exists.".format(fullpath))  # Inform the user if the file exists
    else:
        with open(fullpath, 'w') as taskfile:  # Create a new file
            taskfile.write("My Task List")  # Add a header for the task list

# Function to view all tasks
def view_all_tasks(fullpath):
    """
    Reads and displays all tasks from the file.
    Tasks are numbered for easy reference.
    Returns the list of tasks (including the header).
    """
    print("\nOK, viewing all tasks...")

    with open(fullpath, "r") as taskfile:  # Open the file in read mode
        lines = taskfile.readlines()  # Read all lines into a list

        if len(lines) == 1:  # Check if the file contains only the header
            print("\nNo Task Found!")  # Inform the user if no tasks are present
            return []  # Return an empty list
        else:
            linecount = 1
            for eachline in lines[1:]:  # Skip the header and display tasks
                print("{}. {}".format(linecount, eachline.strip()))  # Remove trailing newlines
                linecount += 1

    return lines  # Return the list of tasks

# Function to add a new task
def add_new_task(fullpath):
    """
    Prompts the user to enter a new task and appends it to the task file.
    """
    with open(fullpath, "a") as taskfile:  # Open the file in append mode
        newtask = input("Enter a new task: ")  # Get the new task from the user
        taskfile.write("\n" + newtask)  # Add the task to the file with a newline

# Function to mark a task as done
def mark_task_as_done(fullpath):
    """
    Marks a specific task as done by appending '[DONE]' to it.
    """
    print("\nMarking a task as done...")
    lines = view_all_tasks(fullpath)  # Display and get the list of tasks

    if len(lines) <= 1:  # If no tasks are available to mark
        print("\nNo tasks available to mark as done!")
        return

    # Prompt the user to choose a task
    task_number = int(input("\nEnter the task number to mark as done: "))
    if task_number < 1 or task_number > len(lines) - 1:  # Validate the task number
        print("\nInvalid task number. Try again!")
        return

    # Mark the task as done if not already marked
    task_index = task_number  # Map to the correct line in the file
    if "[DONE]" in lines[task_index]:  # Check if the task is already marked as done
        print("\nThis task is already marked as done!")
    else:
        lines[task_index] = lines[task_index].strip() + " [DONE]\n"  # Append '[DONE]' to the task
        print("\nTask {} marked as done.".format(task_number))

    # Write the updated tasks back to the file
    with open(fullpath, "w") as taskfile:
        taskfile.writelines(lines)

# Function to delete a task
def delete_task(fullpath):
    """
    Deletes a specific task from the task file.
    """
    print("\nDeleting a task...")
    lines = view_all_tasks(fullpath)  # Display and get the list of tasks

    if len(lines) <= 1:  # If no tasks are available to delete
        print("\nNo tasks available to delete!")
        return

    # Prompt the user to choose a task to delete
    task_number = int(input("\nEnter the task number to delete: "))
    if task_number < 1 or task_number > len(lines) - 1:  # Validate the task number
        print("\nInvalid task number. Try again!")
        return

    # Confirm deletion
    confirm = input("\nAre you sure you want to delete task {}? (y/n): ".format(task_number)).lower()
    if confirm != 'y':  # Cancel deletion if the user says no
        print("\nTask deletion canceled.")
        return

    # Delete the selected task
    task_index = task_number  # Map to the correct line in the file
    deleted_task = lines.pop(task_index).strip()  # Remove the task from the list

    # Write the updated tasks back to the file
    with open(fullpath, "w") as taskfile:
        taskfile.writelines(lines)

    print("\nTask '{}' deleted successfully.".format(deleted_task))


# Main program loop
print("\nWelcome to Personal Planner")

while True:
    # Display menu options to the user
    print("\n")
    print("1. Create a new task file")
    print("2. View all tasks")
    print("3. Add a new task")
    print("4. Delete a task")
    print("5. Mark a task as done")
    print("6. Exit")

    # Get the user's choice
    choice = input("\nInput choice: ")

    if choice == '1':  # Create a new task file
        create_new_file(FULLPATH)

    elif choice == '2':  # View all tasks
        view_all_tasks(FULLPATH)
        
    elif choice == '3':  # Add a new task
        add_new_task(FULLPATH)

    elif choice == '4':  # Delete a task
        delete_task(FULLPATH)    

    elif choice == '5':  # Mark a task as done
        mark_task_as_done(FULLPATH)
        
    elif choice == '6':  # Exit the program
        print("\nExiting... Bye!")
        break

    else:  # Handle invalid input
        print("\nInvalid choice. Try again!")
