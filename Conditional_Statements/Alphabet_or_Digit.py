char = input("Enter something : ")

if char.isalpha():
    print(f"{char} is Character")
elif char.isdigit():
    print(f"{char} is digit")
else:
    print(f"{char} is a Special Character")