string1 = input("Enter the first string : ")
string2 = input("Enter the second string : ")


if len(string1) != len(string2):
    print("Not an anagram")
else:
    for i in string1:
        if i not in string2:
            print("Not an anagram")
            break
    else:
        print("Anagram")