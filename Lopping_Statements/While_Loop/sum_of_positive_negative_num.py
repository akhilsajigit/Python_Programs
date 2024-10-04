size = int(input("Enter the size of numbers : "))

ps_sum = neg_sum = count = 0

while count < size:
    n = int(input("Enter the numbers : "))
    if n >= 0:
        ps_sum += n
        count += 1
    elif n< 0:
        neg_sum += n
        count += 1
    else:
        print("invalid")
print("Sum of positive numbers : ",ps_sum)
print("Sum of negative numbers : ",neg_sum)