stock = {"apple": {"stock": 20, "price": 2}, "orange": {"stock": 30, "price": 3}, "banana": {"stock": 10, "price": 4}, "pineapple": {"stock": 15, "price": 4}, "papaya": {"stock": 20, "price": 3}, "strawberry": {"stock": 25, "price": 5}}
cart = {}
cost = 0

def funcAdd(**kwargs):
    global cost
    for fruit, quantity in kwargs.items():
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


def funcRemove(**rKwargs):
    global cost
    for rFruit, rQuantity in rKwargs.items():
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
            numAdd = int(input("Enter the number of fruits you want to add: "))
            addDict = {}

            for i in range(numAdd):
                key = input("Enter fruit: ")
                value = int(input("Enter quantity: "))
                addDict[key] = value

            funcAdd(**addDict)

        elif action == "remove":
            numRemove = int(input("Enter the number of fruits you want to remove: "))
            removeDict = {}

            for k in range(numRemove):
                rKey = input("Enter fruit: ")
                rValue = int(input("Enter quantity: "))
                removeDict[rKey] = rValue

            funcRemove(**removeDict)

        else:
            break

    print("Your cart: " + str(cart))
    print("Your total cost: $" + str(cost))

else:
    print("Come back later.")
