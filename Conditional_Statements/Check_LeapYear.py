# Python program to check leap year

year = int(input("Enter a year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# lower = int(input("Enter the initial year: "))
# upper = int(input("Enter the final year: "))
#
# for yr in range(lower, upper+1):
#     if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0):
#         print(yr)
