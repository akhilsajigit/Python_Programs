name = input("Enter your name : ")
gender = input("""
M = male
F = Female
O = other
Enter your gender : """)
x = gender.upper()

if x == "M":
    print("Male")
elif x == "F":
    print("Female")
elif x == "O":
    print("Other")
else:
    print("Invalid input")