menu = {
    "cheeseburger": 5.50,
    "double bacon burger": 7.90,
    "spicy chicken sandwich": 6.20,
    "veggie delight burger": 5.00,
    "crispy fries": 2.80,
    "chocolate sundae": 3.00,
    "apple pie": 2.50,
    "milkshake": 4.20,
    "coke": 2.00
}

orders = {}

TITLE = "Order Summary"
PRICE_COL_WIDTH = 10  # enough space for "$" + price formatting


def calc_item_col_width(menu_dict):
    # +2 gives a little spacing so it looks nicer
    longest = 0
    for item_name in menu_dict:
        if len(item_name) > longest:
            longest = len(item_name)
    # Also consider the word "Total"
    if len("total") > longest:
        longest = len("total")
    return longest + 2


ITEM_COL_WIDTH = calc_item_col_width(menu)
RECEIPT_WIDTH = ITEM_COL_WIDTH + 3 + 1 + PRICE_COL_WIDTH  # item + " : " + "$" + price col
if RECEIPT_WIDTH < len(TITLE):
    RECEIPT_WIDTH = len(TITLE)


def print_line():
    print("-" * RECEIPT_WIDTH)


def format_menu_entry(item_name, price):
    # item_name stored in lowercase; display nicely using title()
    print(f"{item_name.title():<{ITEM_COL_WIDTH}} : ${price:>{PRICE_COL_WIDTH}.2f}")


def ask_yes_no(prompt):
    while True:
        response = input(prompt).lower().strip()
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False
        print("Please enter y/yes or n/no.")

wallet_balance = 10

print("Welcome to HanBaoBao!")
print("Here's our menu:")

for item_name, price in menu.items():
    format_menu_entry(item_name, price)

while True:
    order = input("\nWhat would you like to order? (type 'nm' if no more): ").lower().strip()
    order_part = order.split()
    # Handle removal
    if len(order)> 1 and order_part[0] in ("remove", "Remove"):
        order_part.pop(0)
        order_to_remove = " ".join(order_part)            
        if order_to_remove not in orders:
            print(f"{order_to_remove.title()} is no longer in your order.")
        elif order_to_remove in orders and orders[order_to_remove] == menu[order_to_remove]:
            del orders[order_to_remove]
            wallet_balance += menu[order_to_remove]
            print(f"{order_to_remove.title()} have been removed from your order.")
        else:
            orders[order_to_remove] -= menu[order_to_remove]
            wallet_balance += menu[order_to_remove]
            qty_left = orders[order_to_remove]/menu[order_to_remove]
            print(f"One {order_to_remove.title()} have been removed from your order. {qty_left:.0f} remaining in order.")
        continue
        

    # Handle exit commands first
    if order in ("nm", "no more"):
        print("Ok, thank you for your order.")
        break

    if order not in menu:
        print("Sorry, we don't have that item.")
        continue

    print(f"{order.title()} costs ${menu[order]:.2f}.")

    if ask_yes_no("\nDo you want to add it to your order? (y/n): "):
        # check for wallet balance
        if wallet_balance - menu[order] < 0:
            print(f"{order.title()} cost ${menu[order]:.2f}. You only have ${wallet_balance:.2f} left in your wallet.")
            print("Order not added.")
            continue
        else:
            wallet_balance -= menu[order]

        # check for existing orders
        if order in orders:
            orders[order] += menu[order]
        else:
            orders[order] = menu[order]
        print(f"{order.title()} was added to your order.")
        print(f"Remaining wallet balance: ${wallet_balance:.2f}")
    else:
        print(f"{order.title()} was not added to your order.")

# Print receipt
total = 0.0
print(f"\n{TITLE:^{RECEIPT_WIDTH}}")
print_line()

for item_name, price in orders.items():
    format_menu_entry(item_name, price)
    total += price

print_line()
format_menu_entry("Total", total)
format_menu_entry("Remaining", wallet_balance)
