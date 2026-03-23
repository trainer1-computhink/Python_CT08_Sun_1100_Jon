import os

menu_string = """
Menu:
1. Create a new task file
2. View all tasks
3. Add a new task
4. Delete a task
5. Mark a task as done
6. Exit

Enter your choice:
"""
TASK_FILE = "tasks.txt"

def write_new_file():
    with open("tasks.txt","w") as file:
        file.write("My Task List")
    print("Task list file created.")

def view_all_tasks():
    with open("tasks.txt", "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if i == 0:
                print(f"{lines[i]}")
            else:
                print(f"{i}. {lines[i]}")

def add_new_task():
    task = input("Enter a new task: ")
    with open(TASK_FILE, "a") as file:
        file.write("\n" + task)
        print("Task added successfully")
    

y_n_options = ["y","n"]
def intialise_file_task():
    if os.path.exists("tasks.txt"):
        print(f"Task file 'tasks.txt' already exits.")
        while True:
            option_y_n = input("Overwrite? (y/n): ").lower().strip()

            if option_y_n not in y_n_options:
                print("please insert only y or n")
                continue
            
            if option_y_n == "y":
                write_new_file()
            break
    else:
        write_new_file()
        



def menu():
    while True:
        menu_choice = input(menu_string)

        if not menu_choice.isdigit():
            print("The menu choice should be digit from 1 - 6")
            continue
        elif not (int(menu_choice) < 7 and int(menu_choice) >= 0):
            print("The menu choice should be between 1 - 6") 
            continue
        else:
            choice = int(menu_choice)
            if choice == 1:
                intialise_file_task()
            if choice == 2:
                view_all_tasks()
            if choice == 3:
                add_new_task()
    
menu()