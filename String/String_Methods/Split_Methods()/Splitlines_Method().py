s = 'aaa\nbbb\tccc\rddd\feee'

print(s.splitlines())  # \t is not a splitting line so it will not split
print(s.splitlines(keepends=True))


print('But When we use split with s string it will split the \t also')
print(s.split())