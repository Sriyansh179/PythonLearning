stock = {"apple": {"stock": 20, "price": 2}, "orange": {"stock": 30, "price": 3}, "banana": {"stock": 10, "price": 4}, "pineapple": {"stock": 15, "price": 4}, "papaya": {"stock": 20, "price": 3}, "strawberry": {"stock": 25, "price": 5}}
cart = {}
cost = 0

def funcAdd(fruit, quantity):
    global cost
    if fruit in cart:
        cart[fruit] += quantity
        cost = cost + ((stock[fruit]["price"])*quantity)

    elif fruit in stock:
        cart.update({fruit: quantity})
        cost = cost + ((stock[fruit]["price"])*quantity)
    else:
        print("Item not in stock.")

    print("Your cart: " + str(cart))
    print("Your total cost: $" + str(cost))


def funcRemove(rFruit, rQuantity):
    global cost
    if rFruit in cart:
        if rQuantity > cart[rFruit]:
             print("Can't remove more items than already in cart. ")

        else:
            cart[rFruit] -= rQuantity
            cost = cost - ((stock[rFruit]["price"])*rQuantity)
                
    else:
        print("Item not added in cart previously.")
            

    print("Your cart: " + str(cart))
    print("Your total cost: $" + str(cost))


decision = input("Do you want to shop? ").lower()

if decision == "yes":
    print("Items available: ")
    for k in stock:
        print(k + ": $" + str(stock[k]["price"]) + "\nStock available: " + str(stock[k]["stock"]) + "\n------------------------")
    
    while True:
        action = input("Do you want to add/remove items or exit? ")

        if action == "add":
            fruit = input("Which fruit do you want to add? ").lower()
            quantity = int(input("How many " + fruit + "s do you want to add? "))
            funcAdd(fruit, quantity)

        elif action == "remove":
            rFruit = input("Which fruit do you want to remove? ").lower()
            rQuantity = int(input("How many " + fruit + "s do you want to remove? "))
            funcRemove(rFruit, rQuantity)

        else:
            break

    print("Your cart: " + str(cart))
    print("Your total cost: $" + str(cost))

else:
    print("Come back later.")

