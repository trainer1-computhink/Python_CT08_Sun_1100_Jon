import random

# Function to generate a strong password
def generate_password(length=12):
    """
    Generate a strong password with uppercase, lowercase, numbers, and symbols.
    """
    if length < 12:
        print("Password length must be at least 12 characters.")
        return None

    password = ""
    for _ in range(length):
        char_type = random.choice(["upper", "lower", "digit", "symbol"])
        if char_type == "upper":
            password += chr(random.randint(65, 90))  # Uppercase letters
        elif char_type == "lower":
            password += chr(random.randint(97, 122))  # Lowercase letters
        elif char_type == "digit":
            password += chr(random.randint(48, 57))  # Numbers
        elif char_type == "symbol":
            password += chr(random.randint(33, 47))  # Symbols
    return password

# Task 1: Create a new user
def create_new_user(user_db):
    """
    Create a new username and assign a strong password.
    """
    username = input("Enter a username: ").strip().lower()

    if username in user_db:
        print("Error: Username already exists!")
        return None
        
    password = generate_password()  # Generate a strong password
    user_db[username] = password
    print("Username created: {}".format(username))
    print("Your password: {}".format(password))

# Task 2: Update password
def update_password(user_db):
    """
    Update an existing user's password after verifying their current password.
    """
    username = input("Enter your username: ").strip().lower()
    if username not in user_db:
        print("Error: Username not found!")
        return

    current_password = input("Enter your current password: ").strip()
    if user_db[username] != current_password:
        print("Error: Incorrect password!")
        return

    new_password = generate_password()  # Generate a new strong password
    user_db[username] = new_password  # Update the user's password in the database
    print("Password updated successfully for {}.".format(username))
    print("Your new password: {}".format(new_password))

# Task 3: View stored usernames and passwords
def view_user_data(user_db):
    """
    Display all usernames and their masked passwords.
    """
    if not user_db:
        print("No user data available.")
        return
    print("\nUsernames and Passwords:")
    for username, password in user_db.items():
        print("{}: {}".format(username, "*" * len(password)))

# Task 4: Login function
def login(user_db):
    """
    Allow a user to log in by verifying their username and password.
    """
    username = input("Enter your username: ").strip().lower()
    if username not in user_db:
        print("Error: Username not found!")
        return False  # Login failed

    password = input("Enter your password: ").strip()
    if user_db[username] == password:
        print("Login successful! Welcome, {}.".format(username))
        return True  # Login successful
    else:
        print("Error: Incorrect password!")
        return False  # Login failed

# Task 5: Menu system
def menu_system(user_db):
    """
    Interactive menu system for username and password management.
    """
    while True:
        print("\nUsername and Password Manager")
        print("1. Create a New User")
        print("2. Update Password")
        print("3. Login")
        print("4. View Stored Usernames and Passwords")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            create_new_user(user_db)

        elif choice == 2:
            update_password(user_db)

        elif choice == 3:
            login(user_db)

        elif choice == 4:
            view_user_data(user_db)

        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

# Main execution
if __name__ == "__main__":
    user_db = {}  # Initialize an empty dictionary to store user data
    menu_system(user_db)  # Start the menu system
