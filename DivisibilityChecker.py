number = int(input("Input a number of your choice: "))
if number%3 == 0 and number%5 == 0:
    print(str(number) + " is divisible by both 3 and 5!")
elif number%3 == 0:
    print(str(number) + " is divisible by 3!")
elif number%5 == 0:
    print(str(number) + " is divisible by 5!")
else:
    print(str(number) + " is not divisible by 3 nor 5!")
