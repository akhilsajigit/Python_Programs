num = int(input("Enter the number : "))
# making a copy for checking condition
a = num
# need rev var to store reversed number and digit need to iterate ech digit from number
digit = rev = 0

while num > 0:
    # To get  last positioned digit from number by iteration
    digit = num % 10
    # calculating reverse by adding elements and multiply with ten for higher position
    rev = rev * 10 + digit
    # delete last taken digit for taking another element
    num = num // 10
if a == rev:
    print(f"{a} is palindrome ")
else:
    print(f"{a} is not palindrome")
