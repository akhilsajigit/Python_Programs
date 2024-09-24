password = input("Enter password: ")
if len(password) < 8:
    print("Password too short")
elif not any(char.isdigit() for char in password):
    print("Password should have digits")
elif not any(char.isalpha() for char in password):
    print("Password should have letters")
else:
    print("Password valid")