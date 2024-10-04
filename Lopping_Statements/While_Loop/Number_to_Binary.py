n = int(input("Enter the number : "))
bin_num = ''

while n>0:
    r = n % 2
    n = n // 2
    bin_num = str(r) + bin_num

print(bin_num)