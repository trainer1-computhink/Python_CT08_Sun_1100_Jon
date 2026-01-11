# Lesson 4 - Bookshop Ordering System (BOS)

## Task 1: Create the Menu
**Display the Menu**

Write a program that:​
- Shows a list of school supplies and their prices.​
- Create a dictionary with items as keys and prices as values (e.g., {"Notebook": 2.50, "Pencil": 0.50} ).​
- Use a loop to display each item and its price.

## Task 2: Check if item exists
**Take the Customer’s Order and Check if it Exists​**

Extend the previous program that:​
- Asks the customer for the item they want to order.​- Checks if the item exists in the menu.​
    - If it exists: Print the item and its price.​
    - If it does not exist: Display a message saying the item is unavailable.​
- Keep asking again and again until customer says “no more”

## Task 3: Add ordered items to another dictionary
**Add the Ordered Item to Another Dictionary​**

Extend your program so that it:​
- If the item exists, asks the customer if they want to add it to their order.​
    - If the customer says "yes," ​
        - add the item and its price to a separate dictionary that stores the customer’s order​
    - If the customer says "no," ​
        - display a message confirming the item was not added.

## Task 4: Display Order Summary and Total Cost
**Display the Order Summary and Total Cost​**

After the customer finishes ordering:​
- Display all the items in their order with the prices.​
- Calculate and display the total cost of the order.

## Challenge 1: Track Quantities of Items
Allow the customer to specify how many of each item they want to buy.​
Store both the item and quantity in a nested dictionary.​
- purchases = ​{"Notebook": {"quantity": 2, "cost": 5.00}}​
Calculate the total cost based on quantities.

## Challenge 2: Apply Discounts
The goal of this challenge is to introduce a discount system to your program, allowing customers to receive a percentage discount if their total spending exceeds a certain threshold.​
- Example: If the customer spends more than $20, they get a 10% discount on their bill.