# Caesar Cipher Program
# This program encrypts and decrypts text using ASCII values 
# for printable characters (32–126).
# It includes functionality to handle single characters, sentences, lists, and files.

def caesar_shift_character(char, key, mode):
    """
    Shifts a single character for encryption or decryption using the Caesar cipher method.

    Args:
        char (str): A single character to shift.
        key (int): The encryption/decryption key (shift value).
        mode (str): The operation mode, either "encrypt" or "decrypt".

    Returns:
        str: The shifted character. If the character is outside the printable range (32-126),
        it is returned unchanged.
    """
    # Define the start and end of the printable ASCII range
    ascii_start = 32
    ascii_end = 126

    # Calculate the total number of printable characters
    range_size = ascii_end - ascii_start + 1

    # Check if the character is within the printable ASCII range
    if ascii_start <= ord(char) <= ascii_end:
        # Convert the character to its ASCII value
        char_code = ord(char)

        # Determine the shift direction based on the mode
        if mode == "encrypt":
            # Positive shift for encryption
            shifted_code = char_code - ascii_start + key 

        elif mode == "decrypt":
            # Negative shift for decryption
            shifted_code = char_code - ascii_start - key  

        else:
            raise ValueError("Invalid mode. Use 'encrypt' or 'decrypt'.")

        # Wrap the shifted value within the printable range using modulo arithmetic
        wrapped_code = shifted_code % range_size

        # Map the wrapped value back to the printable ASCII range
        final_code = wrapped_code + ascii_start

        # Convert the resulting ASCII value back to a character
        return chr(final_code)
    else:
        # Return the character unchanged if it is outside the printable range
        return char

def caesar_shift_sentence(sentence, key, mode):
    """
    Shifts a sentence for encryption or decryption using the Caesar cipher method.

    Args:
        sentence (str): The sentence to shift.
        key (int): The encryption/decryption key (shift value).
        mode (str): The operation mode, either "encrypt" or "decrypt".

    Returns:
        str: The shifted sentence.
    """
    # Initialize an empty string to store the shifted result
    shifted_sentence = ""

    # Iterate through each character in the sentence
    for char in sentence:
        # Shift the character based on the mode
        shifted_sentence += caesar_shift_character(char, key, mode)

    # Return the shifted sentence
    return shifted_sentence

def caesar_shift_list(sentences, key, mode):
    """
    Shifts a list of sentences for encryption or decryption using the Caesar cipher method.

    Args:
        sentences (list): A list of sentences to shift.
        key (int): The encryption/decryption key (shift value).
        mode (str): The operation mode, either "encrypt" or "decrypt".

    Returns:
        list: A list of shifted sentences.
    """
    # Initialize an empty list to store shifted sentences
    shifted_list = []

    # Iterate through each sentence in the list
    for sentence in sentences:
        # Shift the sentence and add it to the list
        shifted_sentence = caesar_shift_sentence(sentence, key, mode)
        shifted_list.append(shifted_sentence)

    # Return the list of shifted sentences
    return shifted_list

def caesar_shift_file(input_filename, output_filename, key, mode):
    """
    Shifts a file for encryption or decryption by processing each line.

    Args:
        input_filename (str): The name of the input file.
        output_filename (str): The name of the output file.
        key (int): The encryption/decryption key (shift value).
        mode (str): The operation mode, either "encrypt" or "decrypt".

    Returns:
        None
    """
    # Open the input file for reading
    with open(input_filename, "r") as infile:
        # Open the output file for writing
        with open(output_filename, "w") as outfile:
            # Iterate through each line in the input file
            for line in infile:
                # Shift the line and write it to the output file
                shifted_line = caesar_shift_sentence(line.strip(), key, mode)
                outfile.write(shifted_line + "\n")


def brute_force_decrypt(filename):
    """
    Attempts to decrypt a file using all possible keys and prints each result.

    Args:
        filename (str): The name of the encrypted file to decrypt.

    Returns:
        None
    """
    # Define the ASCII range for printable characters
    ascii_start = 32
    ascii_end = 126

    # Calculate the total number of possible keys
    range_size = ascii_end - ascii_start + 1

    # Open the file containing the encrypted content
    with open(filename, "r") as infile:
        # Read all lines from the file
        encrypted_content = infile.readlines()

    # Print a header for the brute force results
    print("\nBrute Force Decryption Results:")

    # Try every possible key in the defined range
    for key in range(range_size):
        print("\nKey# {}:".format(key))  # Indicate the current key being tried

        # Decrypt only the first 3 lines from the encrypted file
        for line in encrypted_content[:3]:
            decrypted_line = caesar_shift_sentence(line.strip(), key, "decrypt")
            print("key #{} : {}".format(key, decrypted_line))



def menu_system():
    """
    Menu system for selecting Caesar cipher options.
    """
    while True:
        # Display the menu options
        print("\nCaesar Cipher Menu:")
        print("1. Encrypt a Single Sentence")
        print("2. Decrypt a Single Sentence")
        print("3. Encrypt a List of Sentences")
        print("4. Decrypt a List of Sentences")
        print("5. Encrypt a File")
        print("6. Decrypt a File")
        print("7. Brute Force Decrypt a File")
        print("8. Exit Program")

        # Prompt the user for their choice
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue

        # Handle encryption and decryption of a single sentence
        if choice in [1, 2]:
            # Prompt the user for a sentence and key
            sentence = input("Enter the sentence: ")
            key = int(input("Enter the key: "))
            if choice == 1:
                mode == "encrypt"
            else:
                mode == "decrypt"

            # Perform the encryption or decryption
            result = caesar_shift_sentence(sentence, key, mode)
            print("Result: {}".format(result))

        # Handle encryption and decryption of a list of sentences
        elif choice in [3, 4]:
            # Prompt the user for the number of sentences
            num_sentences = int(input("How many sentences? "))
            sentences = []

            # Collect each sentence from the user
            for i in range(num_sentences):
                sentence = input("Enter sentence {}: ".format(i + 1))
                sentences.append(sentence)

            # Prompt the user for a key and determine the mode
            key = int(input("Enter the key: "))
            if choice == 3:
                mode = "encrypt"
            else:
                mode = "decrypt"

            # Perform the encryption or decryption on the list
            result = caesar_shift_list(sentences, key, mode)
            print("Result: {}".format(result))

        # Handle encryption and decryption of a file
        elif choice in [5, 6]:
            # Prompt the user for file names and key
            input_filename = input("Enter the name of the input file: ")
            # in github, you need to append your repository name as below
            #input_filename = "OLC2024-Main\\" + input_filename
            output_filename = input("Enter the name of the output file: ")
            # in github, you need to append your repository name as below
            # output_filename = "OLC2024-Main\\" + output_filename
            key = int(input("Enter the key: "))
            if choice == 5:
                mode = "encrypt"
            else:
                mode = "decrypt"

            # Perform the file encryption or decryption
            caesar_shift_file(input_filename, output_filename, key, mode)
            print("File processed successfully. Output saved in '{}'.".format(output_filename))

        # Handle brute force decryption of a file
        elif choice == 7:
            # Prompt the user for the encrypted file
            filename = input("Enter the name of the file to brute force decrypt: ")
            filename = "OLC2024-Main\\"+filename
            brute_force_decrypt(filename)

        # Exit the program
        elif choice == 8:
            print("Exiting program. Goodbye!")
            break
        # Handle invalid menu choices
        else:
            print("Invalid choice! Please select a valid option.")

# Call the main menu system
menu_system()