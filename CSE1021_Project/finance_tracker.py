import datetime

# 1. THE SHOP INVENTORY (This is a "Dictionary")
# Think of this as your Menu Card. 
# "101" is the ID. Inside, we have Name, Price, and Stock.
inventory = {
    "101": {"name": "Milk", "price": 60, "stock": 20},
    "102": {"name": "Bread", "price": 45, "stock": 15},
    "103": {"name": "Eggs", "price": 80, "stock": 10},
    "104": {"name": "Butter", "price": 250, "stock": 5},
    "105": {"name": "Rice", "price": 90, "stock": 30}
}

# 2. THE SHOPPING CART (This is a "List")
# This starts empty, like a physical basket you pick up at the entrance.
cart = []

# 3. FUNCTION TO SHOW ITEMS
def view_items():
    print("\n--- Available Items ---")
    print("ID   Name        Price   Stock")
    for item_id, details in inventory.items():
        print(f"{item_id}  {details['name']:<10} {details['price']:<5}   {details['stock']}")

# 4. FUNCTION TO BUY ITEMS
def add_to_cart():
    view_items()
    choice = input("\nEnter Item ID to buy: ")
    
    # Check if ID exists (Conditionals)
    if choice in inventory:
        qty = int(input("Enter Quantity: "))
        
        # Check if we have enough stock
        if qty <= inventory[choice]['stock']:
            # Calculate cost
            cost = inventory[choice]['price'] * qty
            
            # Add to basket (List Append)
            cart.append({"name": inventory[choice]['name'], "qty": qty, "total": cost})
            
            # Reduce stock from shelf (Dictionary Update)
            inventory[choice]['stock'] -= qty
            print("Item added to cart!")
        else:
            print("Sorry, not enough stock!")
    else:
        print("Invalid Item ID")

# 5. FUNCTION TO PRINT BILL
def generate_bill():
    print("\n--- FINAL BILL ---")
    total = 0
    
    # Loop through the basket to sum up prices
    for item in cart:
        print(f"{item['name']} x {item['qty']} = {item['total']}")
        total += item['total']
        
    print("-" * 20)
    print(f"Grand Total: ₹{total}")
    print("-" * 20)
    print("Thank you!")
    cart.clear() # Empty the basket for the next customer

# 6. MAIN MENU (The Loop)
def main():
    while True: # This loop runs forever until you choose Exit
        print("\n1. View Items")
        print("2. Buy Item")
        print("3. Checkout (Bill)")
        print("4. Exit")
        
        opt = input("Choose Option: ")
        
        if opt == '1':
            view_items()
        elif opt == '2':
            add_to_cart()
        elif opt == '3':
            generate_bill()
        elif opt == '4':
            break # Breaks the loop and stops program
        else:
            print("Wrong choice!")

# Start the program
main()