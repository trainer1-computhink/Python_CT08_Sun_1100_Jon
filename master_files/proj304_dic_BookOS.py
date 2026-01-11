# Practical Challenge: Bookshop Ordering System (BOS)

# A dictionary to represent items in the bookshop and their prices
bookshop = {
    'notebook': 2.5, 
    'pencil': 0.5, 
    'pen': 1.2, 
    'ruler': 1.5,
    'eraser': 0.5, 
    'marker': 2, 
    'glue': 3, 
    'calculator': 35
}

# A dictionary to store the customer's ordered items
ordered = {}

# Display a welcome message to the user
print("\nWelcome to the Bookshop Ordering System (BOS)!")
print("Here is the shopping list: ")

# Loop through the bookshop items to display the menu to the user
# Format the output to show the item name and its price in two decimal places
for item, price in bookshop.items():
    print("{} : ${:.2f}".format(item, price))

# Start a loop to take the user's order. This will keep running until the user decides to quit.
while True:
    # Prompt the user to choose an item or exit
    choice = input("\nWhat would you like to buy? Type end to stop: ").lower()

    # If the user types "end", break the loop and finish the ordering process
    if choice == "end":
        print("\nThank you for shopping! Exiting...")
        break
    # Check if the user's choice is a valid item in the bookshop
    elif choice in bookshop:
        # Display the item's price
        print("{} costs ${:.2f}".format(choice, bookshop[choice]))

        # Ask the user if they want to add the chosen item to their order
        buyopt = input("\nDo you want to add {} to your order? y or n: ".format(choice)).lower()
        
        # If the user confirms, add the item to the 'ordered' dictionary
        if buyopt == "y":
            ordered[choice] = bookshop[choice]
            print("{} has been added to your order".format(choice))
        # If the user declines, do nothing and notify them
        elif buyopt == "n":
            print("{} not added".format(choice))
        # Handle invalid inputs when asked for confirmation
        else:
            print("\nType only y or n to buy.")
    # If the user's choice is not found in the bookshop, notify them
    else:
        print("Sorry, we do not have {} in our store".format(choice))

# After the user finishes ordering, display the order summary
# Initialize a variable to keep track of the total cost of the order
total_order = 0
print("--- Order Summary ---")
for item, price in ordered.items():
    # Print each ordered item's name and price
    print("{} : {:.2f}".format(item, price))
    # Add the item's price to the total cost
    total_order += price

# Display a total separator and the total cost of all ordered items
print("-" * 20)
print("Total: ${:.2f}".format(total_order))

# Display the final payment message
print("\nPlease pay ${:.2f}. Thank you!".format(total_order))
