num = float(input("Enter the number : "))

flag = False
if num < 0:
    print("Please a positive number ")
elif num == 1 or num == 0:
    print(f"{num} is not a prime ")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break
    if flag:
        print(num,"is not a prime "+"mbjabd")
    else:
        print(f"{num} is a prime ")
else:
    print("Invalid input ")
