count = 0
list1 = []
size = int(input("Size : "))
while count < size:
    n = int(input("Number for list : "))
    count += 1
    if n % 3 == 0:
        continue
    print(n)
    list1.append(n)
print("Taken numbers are : ",list1)

