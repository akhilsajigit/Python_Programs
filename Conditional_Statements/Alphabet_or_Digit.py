# Program to find entering input is alphabet or digit

char = input("Enter something : ")

# checking input string using string comparison methods
if char.isalpha():
    print(f"{char} is Character")
elif char.isdigit():
    print(f"{char} is digit")
else:
    print(f"{char} is a Special Character")