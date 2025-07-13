num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))


def max(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2

print("The max is: " + str(max(num1, num2)))
    
    
    
