""" find the occurrence of the substring
 It will start looking for o from the left hand of the string . The result is 4 cause we found ‘ o ‘ there
 The result will be -1 . Why it is -1 because the character will start from 0 . -1 means outside the range . So it is invalid position
"""

s = 'hello, how are you'
print(s.find('o'))

print(s.find('o',5))
print(s.find('u',9,18))