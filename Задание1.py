#Напишите программу которая проверяет, является ли одно число квадратом другого
a = int(input('a = '))
b = int(input('b = '))
if a < b:
    a = a ** 2
else:
    b = b ** 2
if a == b:
    print('Да, является')
else:
    print('Нет, не является')

    