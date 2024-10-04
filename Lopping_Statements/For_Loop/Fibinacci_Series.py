n = int(input("Enter the number : "))
first_term = sum = 0
second_term = 1
print(first_term)
print(second_term)

for i in range(3,n+1):
    sum = first_term + second_term
    first_term = second_term
    second_term = sum
    print(sum)
