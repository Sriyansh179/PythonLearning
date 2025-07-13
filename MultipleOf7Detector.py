
newNum = int(input("Enter a number "))
sum = 0

while newNum % 7:
    sum = sum + newNum
    newNum = int(input("Enter a number "))

print("The total sum: " + str(sum))
