str1 = input("Enter string : ")

rev = str1[::-1]
if str1 == rev:
    print("String is Palindrome ")
else:
    print("Not Palindrome But we can convert as palindrome ")
    con = str1+rev
    print(f"The converted string are {con} and it is palindrome ")