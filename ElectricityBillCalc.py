units = int(input("Enter the number of electricity units consumed: "))
price = 0
if units <= 100:
    price = 1.5*units
elif units <= 200:
    price = 2.5*units
else:
    price = 4*units


if price > 500:
    price = price + 50

print("Your total cost: ₹" + str(price))
