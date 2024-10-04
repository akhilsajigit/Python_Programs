import random

num = random.randint(1, 10)
guess = 0

while guess != num:
    guess = int(input("Enter the number between(1-10)  : "))
    if guess > num:
        print("The number is larger")
    elif guess < num:
        print("Number is Smaller ")
    else:
        print("Number is correct ")