size = int(input("Enter the size : "))
count = Max = 0

while count < size:
    n = int(input("Enter the numbers: "))
    if n > Max:
        Max = n
    count += 1
print(f"Max of number are {Max}")
