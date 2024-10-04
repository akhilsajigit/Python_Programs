num = int(input("Enter the number : "))
limit = int(input("Enter the limit : "))
for i in range(1,limit+1):
    mul = num * i
    print(f"{num} * {i} = {mul}")