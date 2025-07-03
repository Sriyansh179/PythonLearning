CP = int(input("Input the cost price: "))
SP = int(input("Input the sales price: "))

if SP > CP:
    print("You made a profit of $" + str(SP - CP) + " which is +" + str(((SP - CP) / CP)*100) + "%!")
elif CP > SP:
    print("You made a loss of $" + str(CP - SP) + " which is -" + str(((CP - SP) / CP)*100) + "%!")
else:
    print("You broke-even!")
