size = int(input("Enter the size of numbers : "))

count = sum = 0

while count < size:
    # the condition because the count is starting from zero and the number should equal when the count is less than size
    n = int(input("Enter the numbers : "))
    sum += n
    count += 1

print(f"Sum of numbers {sum}")