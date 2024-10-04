num = int(input("Entr the number : "))
a = num
rev = digit = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print(f"Reverse of {a} is : {rev}")