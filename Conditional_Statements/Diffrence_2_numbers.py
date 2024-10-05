# Find difference of two numbers


num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the Second number : "))

difference = num1-num2

if difference > 0:
    print(f"Difference of {num1} and {num2} is : {difference}")
else:
    print(f"Difference of {num1} and {num2} is : ",num2-num1)