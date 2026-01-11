# Define the menu as a dictionary with food items as keys and 
# their prices as values
menu = {
    'cheeseburger': 5.5, 
    'double bacon burger': 7.9,
    'spicy chicken burger': 6.2, 
    'veggie delight burger': 5,
    'crispy fries': 2.8, 
    'cheese fries': 4.5,
    'chocolate sundae': 3, 
    'apple pie': 2.5,
    'milkshake': 4.2, 
    'coke': 2
}

# Initialize an empty dictionary to store the customer's order
customer_order = {} 

# Print a welcome message formatted with centered text and decorative symbols
print("\n")
print("{:^10}Welcome to HanBaoBao{:^10}".format('*'*10, '*'*10))
print("{:^20}Menu{:^20}".format('-'*10, '-'*10))

# Loop through each item in the menu dictionary and print it in a formatted way
for food, price in menu.items():
    # Display each menu item aligned within 30 spaces and price formatted to 2 decimal places
    print("{:^30}:${:^8.2f}".format(food, price))

# Start an infinite loop to handle the customer's ordering process
while True:
    # Prompt the customer to enter their order
    order = input("\nEnter order, type 'no more' to end: ").lower()
    
    # Check if the customer wants to stop ordering
    if order == 'no more':
        # Print the order summary header
        print("{:^15}Order Summary{:^15}".format('*'*10, '*'*10))
        
        # Initialize a variable to calculate the total order amount
        order_total = 0
        
        # Loop through the items in the customer's order
        for food, price in customer_order.items():
            # Display each ordered item and its price, formatted for readability
            print("{:^30}:${:^8.2f}".format(food, price))
            
            # Add the item's price to the total order amount
            order_total = order_total + price
        
        # Print a decorative separator for clarity
        print("*" * 40)
        
        # Display the total cost of the order
        print("Total: ${:.2f}\n".format(order_total))
        
        # Display a final message with the total amount to be paid
        print("Please pay ${:.2f}. Enjoy your meal!\n".format(order_total))
        
        # Exit the loop and end the program
        break
    else:
        # Check if the entered item exists in the menu
        if order in menu:
            # Display the price of the selected menu item
            print("{} costs ${:.2f}".format(order, menu[order]))
            
            # Ask the customer if they want to add the item to their order
            confirm = input("Add {} to order? y/n: ".format(order)).lower()
            
            if confirm == "y":
                # Add the item and its price to the customer's order
                customer_order[order] = menu[order]
                print("{} has been added to your order.".format(order))
            else:
                # Inform the customer that the item was not added
                print("{} not added to order.".format(order))
        else:
            # Inform the customer that the entered item is not available in the menu
            print("Sorry, we don't have {}".format(order))
