# This will separate string by word that includes in method from left hand side

s = 'Python is very easy'
print('__Partition__')
print(s.partition('is'))
print(s.partition('easy'))

# r-partition is same as partition but is will partition upon from right hand-side

print('__rPartition__')
print(s.rpartition('is'))
