#Нахождение максимального числа из 5
a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
d = int(input('d= '))
e = int(input('e= '))
max1 = 0
max2 = 0
max = 0
if a < b:
    max1 = b
else:
    max1 = a
if c < d:
    max2 = d
else:
    max2 = c
if max1 < max2:
    max = max2
else:
    max = max1
if max < e:
    max = e
else:
    max = max
print(max)