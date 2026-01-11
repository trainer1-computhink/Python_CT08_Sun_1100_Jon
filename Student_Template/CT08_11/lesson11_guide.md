# Lesson 11 - Caesar Encryption

## Task 1: Encrypt/ Decrypt a single character

### Create a function to encrypt/ decrypt a single character
`caesar_shift_character ()`
- **Arguments**: 
  - **char (str)**: A single character to shift.
  - **key (int)**: The encryption/decryption key (shift value).
  - **mode (str)**: "encrypt" or "decrypt" to specify the operation.
- **Return Value**:
  - **str**: The shifted character, or the original character if it’s outside the printable ASCII range.

### Notes
*This is the hardest function as it handles the encryption/ decryption at the character level.*

*Take some time to understand the math and algorithm in the previous slides!*

*Ask your Code Mentor to explain to you!*

## Task 2: Encrypt/ Decrypt a single sentence

### Encrypts or decrypts a full sentence by shifting each character.

`caesar_shift_sentence()`
- **Arguments**: 
  - **sentence (str)**: The sentence to shift.
  - **key (int)**: The encryption/decryption key.
  - **mode (str)**: "encrypt" or "decrypt".

- **Return Value**:
  - **str**: The shifted sentence.

### Notes
*This function will call the previous function caesar_shift_character*

*You will need to loop through all the characters in a string and encrypt/ decrypt.*

*Further on, all these functions will go into a menu system*

## Task 3: Encrypt/ Decrypt a list of sentences

### Encrypts or decrypts a list of sentences using the Caesar cipher.

`caesar_shift_list()`
- **Arguments**: 
  - **sentences (list)**: A list of strings to shift.
  - **key (int)**: The encryption/decryption key.
  - **mode (str)**: "encrypt" or "decrypt".

- **Return Value**:
  - **str**: A list of shifted sentences.
 
### Notes
*This function will call the previous function caesar_shift_sentence*

*You will need to loop through all the sentences in the list and encrypt/ decrypt.*

*Further on, all these functions will go into a menu system*

## Task 4: Encrypt/ Decrypt a file
### Encrypts or decrypts the contents of a file line by line.

`caesar_shift_file()`
- **Arguments**: 
  - **input_filename (str)**: The name of the input file.
  - **output_filename (str)**: The name of the output file.
  - **key (int)**: The encryption/decryption key.
  - **mode (str)**: "encrypt" or "decrypt".

- **Return Value**:
  - **None**
    - **Note**: The output file will be saved

### Notes
*You will need to use your File IO codes to open, read and write to a file.*

*Further on, all these functions will go into a menu system*

## Task 5: Brute Force Hacking
### Attempts to decrypt a file by testing all possible keys and printing the results for each key.

`brute_force_decrypt()`
- **Arguments**: 
  - **filename (str)**: The name of the encrypted file to decrypt.

- **Return Value**:
  - None
    
### Notes
*Imagine you come across a file which contains encrypted data… how would you try to hack the file and read the contents?*

*Solution: Loop through all possible permutations to find the key, then decrypt the file!*

## Task 6: Interactive Menu System
### Provides a menu interface for users to interact with the Caesar cipher program.

`menu_system()`
- **Arguments**: 
  - None

- **Return Value**:
  - None

### Notes
*This task ties together all the previous functions into a friendly interface.*

*Ensure that you validate the user inputs!*