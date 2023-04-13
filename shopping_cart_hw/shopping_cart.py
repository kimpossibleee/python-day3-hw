import os
from ascii import shopping_cart_img


def shopping_cart():
    user_cart = {}
    print(shopping_cart_img)
    is_active = True

    def print_cart():
        print("\nSHOPPING CART")
        for k, v in user_cart.items():
            print(f"Item: {k} - Quantity: {v}")

    while is_active == True:
        print("\n")
        user_input = input(
            "1) Add Items\n2) Delete Items \n3) View Cart\n4) Quit\nWhat would you like to do today? (Enter a number): ")
        if int(user_input) == 1:
            os.system('clear')
            item = input("What would you like to add to your cart?: ").upper()
            user_cart[item] = user_cart.get(item, 0) + 1
        elif int(user_input) == 2:
            if not user_cart:
                print("Your cart is currently empty. There is nothing to delete.")
            else:
                print_cart()
                del_item = input("What would you like to delete? ").upper()
                if item not in user_cart.keys():
                    print(
                        "This item does not exist in your cart. Please try a different item.")
                else:
                    user_cart[item] = user_cart.get(item, 0) - 1
                    if user_cart[item] == 0:
                        user_cart.pop(item)

        elif int(user_input) == 3:
            os.system('clear')
            if not user_cart:
                print("\nYour cart is currently empty.\n")
            else:
                print_cart()
        elif int(user_input) == 4:
            os.system('clear')
            if not user_cart:
                print("You have an empty cart. Have a nice day!")
            else:
                print("Here are the items currently in your cart. Have a nice day!")
            print_cart()
            is_active = False
        else:
            os.system('clear')
            print("Please try a vaild number between 1-4")
            continue


shopping_cart()
