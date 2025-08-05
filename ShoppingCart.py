stock = {"apple": [20, 2], "orange": [30, 3], "banana": [10, 4], "pineapple": [15, 4], "papaya": [20, 3], "strawberry": [25, 5]}
cart = []
cost = 0
decision2 = "yes"

decision = input("Do you want to shop? ").lower()

if decision == "yes":
    print("Items available: ")
    for k in stock:
        print(k + ": $" + str(stock[k][1]) + "\nStock available: " + str(stock[k][0]) + "\n------------------------")
    
    
    while decision2 == "yes":
        item = input("Which fruit do you want? ").lower()

        if item in stock:
            cart.append(item)
            cost = cost + stock[item][1]
            print("Your cart: " + str(cart))
        else:
            print("Item not in stock.")
        decision2 = input("Do you want to add more items to your cart? ").lower()

    print("Your cart: " + str(cart))
    print("Your total cost: $" + str(cost))
        
else:
    print("Come back later.")



