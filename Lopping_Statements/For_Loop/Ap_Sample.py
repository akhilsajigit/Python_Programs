a = int(input("Enter the first term : "))
n = int(input("Enter the number of terms : "))
d = int(input("Enter the common Difference "))

for i in range(a,a + n * d, d):
    print(i)