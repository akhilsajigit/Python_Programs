# Program to remove punctuation marks from string

str1 = input("Enter the string : ")
punct = """!@#$%^&*()_+={}[].,<>/?"""
str2 = ""

for i in str1:
    if i not in punct:
        str2 += i
print(str2)