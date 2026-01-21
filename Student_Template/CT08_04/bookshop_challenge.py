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

purchase = {}

item_max_length = 0

print("Welcome to the Bookshop Ordering System (BOS)!")
print("\nHere is our menu:")

for item, price in bookshop_catalog.items():
    if len(item) > item_max_length:
        item_max_length = len(item)
    print(f"{item}: ${price:.2f}")

def ask_yes_no(qns):
    while True:
        response = input(qns).lower().strip()
        if response in ("yes", "y"):
            return True
        if response in ("no", "n"):
            return False
        print("Please enter y/yes or n/no.")

def ask_quantity(qns):
    while True: 
        response = input(qns).strip()
        if response.isdigit():
            qty = int(response)
            if qty > 0:
                return qty
            else:
                print("Please enter at least 1 for quantity.")
        else:
            print("Please enter a whole number.")

while True:

    item = input("\nWhat would you like to buy? " ).lower().strip()

    # Exit the loop
    if item in ("no more", "nm"):
        break
    temp_qty = 0
    if item in bookshop_catalog:
        temp_qty = ask_quantity(f"{item.title()} costs ${bookshop_catalog[item]:.2f}. How many would you like to buy?: ")
        
    else:
        print(f"Sorry, we don't have ${item} in our store.")



    if ask_yes_no(f"\nDo you want to add {temp_qty} {item} to your order? (y/n): "):
        # check for existing order
        if item in purchase:
            purchase[item]["quantity"] += temp_qty
        else:
            temp_qty_cost = {
                "quantity": temp_qty,
                "cost": bookshop_catalog[item]
            }
            purchase[item] = temp_qty_cost
        
        print(f"{item.title()} has been added to your order.")
    else:
        print(f"{item.title()} was not added to your order.")

TITLE = "Order Summary"
WIDTH = 20*"-"
HEADING = WIDTH + TITLE + WIDTH

print(HEADING)

total = 0
for item, detail in purchase.items():
    quantity = detail["quantity"]
    price = detail["cost"]
    item_total = quantity * price
    total += item_total
    print(f"{item}: {quantity} @ ${price:.2f} each - ${item_total:.2f} ")

print(f"\nOriginal Total: ${total:.2f}")

if total > 20:
    discount = 0.1 * total
    total -= discount
    
    print(f"Discount Applied: -${discount:.2f} (10% off)")
    print("")
    print(len(HEADING) * "-")
    print(f"Final Total: ${total:.2f}")

print(f"\nYour total bill is ${total:.2f}. Thank you!")
