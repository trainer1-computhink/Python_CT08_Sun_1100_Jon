import os
from datetime import datetime

# Step 1: Open and read the file
input_filename = "encrypted_note.txt"  # Input file containing the encoded message

# Open the file in read mode
print("Opening the file '{}'...".format(input_filename))
with open(input_filename, "r") as file:
    # Read all content of the file
    content = file.read()

# Display the original content
print("\nOriginal Encrypted Note:")
print(content)

# Step 2: Clean the passage by removing punctuation
print("\nCleaning the passage (removing punctuation)...")

# Manually define all punctuation marks
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# Initialize an empty string for cleaned content
cleaned_content = ""

# Loop through each character in the content
for char in content:
    # Check if the character is not a punctuation mark
    if char not in punctuation:
        cleaned_content += char  # Add the character to cleaned_content

# Display the cleaned content
print("\nCleaned Content:")
print(cleaned_content)

# Step 3: Decode the message by extracting the first letter of each word
print("\nDecoding the message...")

# Split the cleaned content into words
words = cleaned_content.split()

# Initialize an empty string for the decoded message
decoded_message = ""

# Loop through each word and get the first letter
for word in words:
    if len(word) > 0:  # Ensure the word is not empty
        decoded_message += word[0]  # Add the first letter of the word to the message

# Display the decoded message
print("\nDecoded Message:")
print(decoded_message)

# Step 4: Save the decoded message to a new file with a timestamp
print("\nSaving the decoded message with a timestamp...")

# Generate a timestamp for the filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = "decoded_message_{}.txt".format(timestamp)

# Open the output file in write mode and save the decoded message
with open(output_filename, "w") as output_file:
    output_file.write("Decoded Message:\n")
    output_file.write(decoded_message)

# Confirm that the file has been saved
print("Decoded message saved successfully to '{}'.".format(output_filename))

# Step 5 (Bonus): Reverse the decoded message for further encryption
print("\nReversing the decoded message for bonus encryption...")

# Initialize an empty string for the reversed message
reversed_message = ""

# Loop through the decoded message in reverse order
for i in range(len(decoded_message) - 1, -1, -1):
    reversed_message += decoded_message[i]

# Save the reversed message to another file
reversed_output_filename = "reversed_message_{}.txt".format(timestamp)
with open(reversed_output_filename, "w") as reversed_file:
    reversed_file.write("Reversed Encrypted Message:\n")
    reversed_file.write(reversed_message)

# Display the reversed message
print("Reversed message saved successfully to '{}'.".format(reversed_output_filename))
print("\nBonus: Reversed Encrypted Message:")
print(reversed_message)
