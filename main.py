a, b, c = 10, 14, 'slm'

print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))

c, b, a = a, c, b

print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))