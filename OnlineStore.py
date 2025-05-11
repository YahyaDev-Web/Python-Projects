# dictionary of available items with their prices and quantity 
items = { 
'iPhone 13': {'price': 1000, 'quantity': 10}, 
 
'MacBook Pro': {'price': 2000, 'quantity': 5}, 
 
'AirPods Pro': {'price': 250, 'quantity': 2}, 
 
'iPad Pro': {'price': 800, 'quantity': 15}, 
 
'Apple Watch Series 7': {'price': 600, 'quantity': 3}, 
} 
 
   



welcome_msg = "Welcome to Codezilla Store!"

options = """
Available Options:
1. View Available Items
2. View Cart
3. Total Cart Price
4. Clear Cart
5. Quit
"""

cart = {}


def main():
    print(welcome_msg)
    while True:
        print(options)
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            view_available_items()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            total_cart_price()
        elif choice == "4":
            clear_cart()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please enter a valid choice.")
            


# function helper
def total_calculator():
    return sum(cart[item]["quantity"] * cart[item]["price"] for item in cart)





def view_available_items():
    items_name = []
    for i, item  in enumerate(items,1) :
        items_name.append(item)
        items_quantity = items[item]["quantity"]
        if items_quantity == 0:
            print(f"{i}. {item} (Not available)")
        else:
            print(f"{i}. {item}")
    try:
        item_purshase = int(input("Enter the number of the item to purshase (Enter 0 to return to previous menu):"))
        if item_purshase == 0:
            return
        if 1 <= item_purshase <= len(items_name):
            user_choice = items_name[item_purshase - 1]
            available_quantity = items[user_choice]["quantity"]
            print(f"Available quantity: {available_quantity}")
            try:
                chosen_quantity = int(input("Please, Enter the quantity: "))
                if chosen_quantity > available_quantity:
                    print(f"Sorry, we only have {available_quantity} of this item.")
                else:
                    item_price = items[user_choice]["price"]
                    cart[user_choice] = {"price": item_price,"quantity": chosen_quantity}
                    print(f"{user_choice} has been added to cart successfully.")
                    # reduce the stock
                    items[user_choice]["quantity"] -= chosen_quantity

            except ValueError:
                input("Please, enter a valid number for quantity ")
        else:
            print("Please , enter a number between 1 and 5.")
    except ValueError:
        print("Please , enter a valid number.")


def view_cart():
    if cart:
        print("-"*25)
        for item in cart:
            item_price = cart[item]["price"]
            item_quantity = cart[item]["quantity"]
            print(f"{item}: ${item_price} x {item_quantity} = ${item_price * item_quantity}")
        print("-"*25)

    else:
        print("Cart is empty, go buy an item from the shop !")

def total_cart_price():
    if cart:
        print(f"Total Price of Cart: ${total_calculator():.2f}")
    else:
        print("You didn't buy anything yet !")



def clear_cart():
    if cart:
        print("Items in the cart before clearing it:")
        print("Cart:")
        view_cart()
        checking_sys = input("Are you sure you want to clear the cart? (y/n): ").lower()
        if checking_sys == "y":
            cart.clear()
            print("Cart has been cleared successfully.")
        else:
            return
    else:
        print("Cart is empty , there is nothing to clear !")

if __name__ == "__main__":
    main()
