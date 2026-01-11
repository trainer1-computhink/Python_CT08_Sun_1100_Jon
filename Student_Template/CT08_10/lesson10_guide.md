# Lesson 10- User Management System

## Task 1: Generate a strong password

### Generate a strong password that meets security guidelines.

- **Function name**: `generate_password()`
- **Params**: length (int) – desired password length
- **return**: password (string) - randomly generated password string.


### Notes
*Use the ASCII table and what you have learned earlier to generate a random and strong password*:
- *12 characters*
- *Uppercase*
- *Lowercase*
- *numbers*
- *special characters*

## Task2: Create a new user

### creates a new username and assigns a strong password using the `generate_password()` function.

- **Function name**: `create_new_user()`
- **Params**: user_db (dictionary) – A dictionary to store usernames and passwords.
- **return**: user_db (dictionary) – Updated dictionary
  - Prints the username and password

### Notes
*Use the earlier password generation program to generate a strong password for the user.*

## Task 3: Update password
Allows an existing user to reset their password by verifying their current password first.

- **Function name**: `update_password()`
- **Params**: user_db (dictionary) – A dictionary to store usernames and passwords.
- **return**: user_db (dictionary) – Updated dictionary
  - Prints the username and password
### Notes
*Checks for username existence in user_db.*

*Verifies the user’s current password before allowing updates.*

*Generates a new strong password using generate_password.*

## Task 4: Login

## Allows users to log in by verifying their username and password.

- **Function name**: `login()`

- **Params**: user_db (dictionary) – A dictionary to store usernames and passwords.

- **returns**: auth_status(boolean) – True or False indicating success or failure.

### Notes
*Ensures the username exists in user_db.*

*Matches the entered password with the stored password for validation.*

## Task 5: View Username and passwords
### Displays all stored usernames and their masked passwords (e.g., ********)

- **Function name**: `view_user_data()`

- **Params**: user_db (dictionary) – A dictionary to store usernames and passwords.

- **returns**: none
  - Prints a list of username and passwords

### Notes
*Strictly speaking, this function should not exist in any system, as it could lead to abuse of a user’s private data.*

*But for verifying whether your program works, we have put this in.*

*Challenge: Mask part of the password. i.e. put (*) instead of the real password.*

## Task 6: Build a menu system

### Build a menu that allows you to access all the functions in the system.

- **Function name**: view_menu()

- **Params**: none

- **returns**: none

### Notes
*The following menu options should be available to you.*

*Your menu should validate the available options inputted by the user.*