num = int(input("Enter the number  : "))
a = num
sum = digit = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num //= 10
print(f"Sum of {a} is : {sum}")