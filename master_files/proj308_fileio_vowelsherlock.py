# Program to analyze text in "sherlock.txt" and save results to "results.txt"

# Step 1: Open the input file and read its contents
input_filename = "sherlock.txt"  # Input file
output_filename = "results.txt"  # Output file to save results

# Open the file in read mode
with open(input_filename, "r") as file:
    # Read all content of the file
    content = file.read()

# Step 2: Count the total number of characters
# Includes all characters (spaces, punctuation, etc.)
total_characters = len(content)

# Step 3: Count the total number of vowels
vowels = "aeiouAEIOU"
total_vowels = 0
# Iterate through each character to check if it is a vowel
for char in content:
    if char in vowels:
        # Increment if character is a vowel
        total_vowels += 1

# Step 4: Count the frequency of each vowel
# Initialize a dictionary to store vowel frequencies
vowel_frequency = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
# Iterate through each character to update vowel frequency
for char in content:
    if char.lower() in vowel_frequency:  # Check if character is a vowel (case insensitive)
        # Update frequency count for the vowel
        vowel_frequency[char.lower()] += 1

# Step 5: Calculate the percentage of vowels in the text
# Prevent division by zero
if total_characters > 0:
    # Calculate percentage of vowels
    percentage_vowels = (total_vowels / total_characters) * 100
else:
    # Set to 0 if total characters is zero
    percentage_vowels = 0

# Step 6: Save results to a new file "results.txt"
# Open the file in write mode
with open(output_filename, "w") as out_file:
    # Write the header
    out_file.write("Sherlock Holmes Text Analysis\n")
    out_file.write("-" * 30 + "\n")
    # Write the total character count
    out_file.write("Total Characters: {}\n".format(total_characters))
    # Write the total vowel count
    out_file.write("Total Vowels: {}\n\n".format(total_vowels))
    # Write the vowel frequencies
    out_file.write("Vowel Frequency:\n")
    for vowel, count in vowel_frequency.items():
        out_file.write("{} = {}\n".format(vowel, count))
    # Write the percentage of vowels
    out_file.write("\nPercentage of Vowels in Text: {:.2f}%\n".format(percentage_vowels))

# Step 7: Print the results to the console
# Notify the user that the analysis is complete
print("Analysis complete. Results saved to 'results.txt'.\n")
# Print the total character count
print("Total Characters: {}".format(total_characters))
# Print the total vowel count
print("Total Vowels: {}".format(total_vowels))
# Print the vowel frequencies
print("\nVowel Frequency:")
for vowel, count in vowel_frequency.items():
    print("{} = {}".format(vowel, count))
# Print the percentage of vowels
print("\nPercentage of Vowels in Text: {:.2f}%".format(percentage_vowels))
