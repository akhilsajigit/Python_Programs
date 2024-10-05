str1 = input("Enter the string : ")
lower =''
upper =''

for i in str1:
    if i.isupper():
        upper += i
    elif i.islower():
        lower += i
    elif i == ' ':
        pass
    else:
        print("Invalid")

print("The Joined string is : ",lower + upper)