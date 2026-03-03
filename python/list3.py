list =[7,8,8,9,10]
print(list[1:3])
list.append(9)
print(list)
list.insert(1,0)
print(list)
list[1]=70
print(list)

list.remove(8)
print(list)
list.pop()
print(list)

for n in list:
  (print(n))
for n in range(1,4):
	print(list[n])
	
while 8 in list:
	list.remove(8)
	
print(list)
print(list[:3])
print(list[::-1])
print(list[::-2])
b=list[:]
b.append(10)
print(b)
print(list)
lst = [10,20,30,40,50,60,70]
print(lst[1:5:-1])
a = "hello"
b = a
b = b.upper()

print(a)
print(b)
