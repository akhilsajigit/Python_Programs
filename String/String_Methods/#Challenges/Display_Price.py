item = input("Enter the item : ")
price = input("Enter its price : ")

dots = len(item) + len(price)
if dots >= 25:
    print("Item should need to short ")
else:
    print(item + dots * '.' + price)