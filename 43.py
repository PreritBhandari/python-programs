#remove item from a tuple
a=(1,2,3,4,5)

print(a)

b=list(a)
print(b)
b.pop(1)
print(b)
c=tuple(b)
print(c)

