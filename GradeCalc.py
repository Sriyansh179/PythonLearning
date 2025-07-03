marks = int(input("Enter marks recieved: \n"))

percentage = (marks/150)*100
if percentage >= 95:
    print("Your grade: A")
elif percentage >= 80:
    print("Your grade: B")
elif percentage >= 70:
    print("Your grade: C")
else:
    print("Your grade: F")
    
