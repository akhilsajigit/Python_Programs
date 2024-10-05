# print('---------------------------------------')
# s1 = 'Python'
# print(s1.islower())
# print(s1.isupper())
# print(s1.istitle())
# print('---------------------------------------')
#
#
# s2 = 'python123'
# print(s1.isalnum())
# print(s1.isalpha())
# print(s1.isspace())
# print(s1.isascii())
# print(s1.islower())
# print('---------------------------------------')

# s3 = 'length1'
# print(s3.isidentifier()) # Checks the input can be identifier or not

# s4 = 'k\n'
# print(s4.isprintable()) # checks the input can be printable or not

# Checking decimal or not
# s5 = '125'
# print(s5.isdecimal())

# s6 = '15'
# print(s6.isdigit())
#
# s7 = '15'
# print(s6.isnumeric())

# s8 = '8\u00b2'
# print(s8)
# print(s8.isdecimal())
# print(s8.isdigit())
# print(s8.isnumeric())

# Arabic letters unicodes
s9 = '\u0661\u0662\u0663'
print(s9)
print(s9.isdecimal())
print(s9.isdigit())
print(s9.isnumeric())
