# dictionary of available items with their prices and quantity 
items = { 
'iPhone 13': {'price': 1000, 'quantity': 10}, 
 
'MacBook Pro': {'price': 2000, 'quantity': 5}, 
 
'AirPods Pro': {'price': 250, 'quantity': 2}, 
 
'iPad Pro': {'price': 800, 'quantity': 15}, 
 
'Apple Watch Series 7': {'price': 600, 'quantity': 3}, 
}



print("🏬 Welcome To YAHYA'S store 🏬")

options = """
Available Otions:
1. View Available Items
2. View Cart
3. Total Cart Price
4. Clear Cart
5. Quit
"""
cart = {}


def main():
    while True:
        print(options)
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            view_items()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            total_cart_price()
        elif choice == "4":
            clear_cart()
        elif choice == "5":
            print("Thank you for shopping at Yahya's Store! ")
            view_cart()
            break
        else:
            print("Invalid choice, please enter a valid choice.")

# helper function
def total_calculate():
    return sum(cart[item]["price"] * cart[item]["quantity"] for item in cart)




def view_items():
    items_name = []
    # print the available items
    for i,item in enumerate(items,1):
        items_name.append(item)
        items_quantity = items[item]["quantity"]
        if items_quantity == 0:
            print(f"{i}. {item} (Out of stock)")
        else:
            print(f"{i}. {item}")
    try:
        # ask user for the item that he/she wants
        item_choice = int(input("Number of the item to purchase (Enter 0 to return to previous menu): "))
        if item_choice == 0:
            return
        # print to the user the available quantity of the chosen item
        user_item = items_name[item_choice - 1]
    except IndexError:
        print("Please Enter a number between 1 and 5.")
    except ValueError:
        print("Please Enter a number between 1 and 5.")
    # end of the fixing problems for the list
    try:
        available_quantity = items[user_item]["quantity"]
        print(f"Available quantity: {available_quantity} ")
        quantity = int(input("Please, Enter the quantity: "))
        if quantity > available_quantity:
            print(f"Sorry, we only have {available_quantity} of this item. ")
        else:
            # reduce the quanity that the user entred from items
            items[user_item]["quantity"] -= quantity
            # check if item is in the cart else add it to the cart
            if user_item in cart:
                cart[user_item]["quantity"] += quantity
            else:
                cart[user_item] = {"price": items[user_item]["price"] , 
                                "quantity": quantity }
    except ValueError:
        print("Please Enter the number of the available quantity. ")


    
def view_cart():
    # view the items that the user purchased
    if cart:
        print("Cart: ")
        print("-"*25)
        total_sum = 0
        for cart_items in cart:
            price = cart[cart_items]['price']
            quantity = cart[cart_items]['quantity']
            total = price * quantity
            total_sum += total
            print(f"{cart_items}: ${price} x {quantity} = ${total:.2f}")
        print("-"*25)
        print(f"Total Price of Cart: ${total_calculate():.2f}")
    else:
        print("No items have been bought.")


def total_cart_price():
    if cart:
            print(f"Total Price of Cart: ${total_calculate():.2f}")
    else:
        print("No items have been bought")



def clear_cart():
    if cart:
        print("Items in the Cart Before clearing it: ")
        view_cart()
        checkig_sys = input("Are you sure you want to clear the cart?: (y/n): ").lower()
        if checkig_sys == "n":
            return
        else:
            # restoring the the old quantity 
            for cart_item in cart:
                items[cart_item]["quantity"] += cart[cart_item]["quantity"]
            cart.clear()
            print("Cart has been cleared succesfully !")
    else:
        print("No items have been bought !")






if __name__ == "__main__":
    main()