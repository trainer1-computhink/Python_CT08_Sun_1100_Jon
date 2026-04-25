# Qns: Debug the Code (Very Hard)

# This program should be a simple shopping cart menu system.

# The program should:
# 1. Keep showing the menu until the user chooses 6
# 2. Allow the user to add an item into the cart
# 3. Allow the user to remove an item from the cart by position
# 4. Allow the user to update an item by position
# 5. Allow the user to search for an item
# 6. Allow the user to print all items with numbering
# 7. Exit when the user chooses 6

# Rules:
# 1. You are NOT allowed to remove any lines.
# 2. You can only MODIFY existing lines.

cart = ["apple", "banana", "coconut"]

choice = 0

while choice != 6
    print("===== Shopping Cart Menu =====")
    print("1. Add item")
    print("2. Remove item")
    print("3. Update item")
    print("4. Search item")
    print("5. Print all items")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice = 1:
        item = input("Enter item to add: ")
        cart.insert(item)
        print(item + " added.")

    elif choice == 2
        position = input("Enter position to remove: ")
        removed_item = cart.pop(position)
        print("Removed: " + removed)

    elif choice == 3:
    position = int(input("Enter position to update: "))
        new_item = input("Enter new item: ")
        cart[position] == new_item
        print("Item updated.")

    elif choice == 4:
        search_item = input("Enter item to search: ")

        if search_item not cart:
            print(search_item + " is in the cart")
        else:
            print(search_item + " is not in the cart")

    elif choice == 5:
        for i in range(len(cart) + 1):
            print(str(i) + ". " + cart[i])

    elif choice == 6:
        print("Goodbye!")

    else
        print("Invalid choice")

print("Final cart: " + cart)