bookshop_catalog = {
    "notebook": 2.50,
    "pencil": 0.50,
    "pen": 1.20,
    "ruler": 1.50,
    "eraser": 0.50,
    'writing pad': 2.50,
    "marker": 2.00,
    "glue": 3.00,
    "calculator": 35.00
}

order = {}

print("Welcome to the Bookshop Ordering System (BOS)!")
print("\nHere is our menu:")

for item, price in bookshop_catalog.items():
    print(f"{item}: ${price:.2f}")

def ask_yes_no(qns):
    while True:
        response = input(qns).lower().strip()
        if response in ("yes", "y"):
            return True
        if response in ("no", "n"):
            return False
        print("Please enter y/yes or n/no.")

    

while True:

    item = input("\nWhat would you like to buy? " ).lower().strip()

    # Exit the loop
    if item in ("no more", "nm"):
        break

    if item in bookshop_catalog:
        print(f"{item.title()} costs ${bookshop_catalog[item]:.2f}.")
    else:
        print(f"Sorry, we don't have ${item} in our store.")

    if ask_yes_no(f"\nDo you want to add {item} to your order? (y/n): "):
        order[item] = bookshop_catalog[item]
        print(f"{item.title()} has been added to your order.")
    else:
        print(f"{item.title()} was not added to your order.")


total = 0
for item, price in order.items():
    total += price
    print(f"{item}: ${price:.2f}")

print(f"Total: ${total:.2f}")
print(f"\nYour total bill is ${total:.2f}. Thank you!")
