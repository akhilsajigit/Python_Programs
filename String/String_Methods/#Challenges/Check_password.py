# check the password and confirm password are same

pass1 = input("Enter the password : ")
pass2 = input("Enter the confirm password : ")

if pass1.casefold() == pass2.casefold():
    print("Correct password")
else:
    print("Please check the password ")