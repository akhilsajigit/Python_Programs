num = int(input("Enter the number  : "))
count = 0
a = num
while num > 0:
    num = num // 10
    count += 1

print(f"Number of digits in {a} is {count}")