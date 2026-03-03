a = [1,2,3]
b = a

print(id(a))
print(id(b))
a = [1, 2, 3]
b = a

b.append(4)

print(a)

