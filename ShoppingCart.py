stock = {"apple": {"stock": 20, "price": 2}, "orange": {"stock": 30, "price": 3}, "banana": {"stock": 10, "price": 4}, "pineapple": {"stock": 15, "price": 4}, "papaya": {"stock": 20, "price": 3}, "strawberry": {"stock": 25, "price": 5}}
cart = {}
cost = 0

decision = input("Do you want to shop? ").lower()

if decision == "yes":
    print("Items available: ")
    for k in stock:
        print(k + ": $" + str(stock[k]["price"]) + "\nStock available: " + str(stock[k]["stock"]) + "\n------------------------")

    while True:
        decision2 = input("Do you want to add/remove items or exit? ")

        if decision2 == "add":
            item = input("Which fruit do you want? ").lower()

            if item in cart:
                quantity = int(input("How many " + item + "s do you want? "))
                cart[item] += quantity
                cost = cost + ((stock[item]["price"])*quantity)

            elif item in stock:
                quantity = int(input("How many " + item + "s do you want? "))
                cart.update({item: quantity})
                cost = cost + ((stock[item]["price"])*quantity)
            else:
                print("Item not in stock.")

            print("Your cart: " + str(cart))
            print("Your total cost: $" + str(cost))
            

        elif decision2 == "remove":
            removeItem = input("Which item do you want to remove? ").lower()

            if removeItem in cart:
                removeQuantity = int(input("How many " + removeItem + "s do you want to remove? "))

                if removeQuantity > cart[removeItem]:
                    print("Can't remove more items than already in cart. ")

                else:
                    cart[removeItem] -= removeQuantity
                    cost = cost - ((stock[removeItem]["price"])*removeQuantity)
                
            else:
                print("Item not added in cart previously.")
            

            print("Your cart: " + str(cart))
            print("Your total cost: $" + str(cost))

        else:
            break

    print("Your final cart: " + str(cart))
    print("Your final cost: $" + str(cost))
        
else:
    print("Come back later.")


