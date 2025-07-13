number = 0
preNum = 0
newNum = int(input("Enter a number: "))
sum = 0
i = 0

while newNum > preNum:
    i = i + 1
    preNum = newNum
    sum = sum + newNum
    newNum = int(input("Enter a number greater than the previous number entered: "))

print("The total sum is: " + str(sum))
print("The total number of numbers that were entered: " + str(i))
