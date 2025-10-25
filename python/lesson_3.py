#Циклы while, for

"""
i=0
while i < 5:
    print('Привет!')
    i = i + 1
"""
from tabnanny import Whitespace
from xmlrpc.client import FastParser

"""
i=1
while i <= 10:
    print(i)
    i += 1
"""
"""
for i in range(10):
    print(i)
"""
"""
i = 0
while True:
    i = i + 1
    if i == 15:
        continue    #Прерывает шаг цикла если значение будет равно 15
    print(i)
    if i > 20:
        break       #Останавливает цикл при достижение числа 20 
"""
"""
#1
for i in range(10, 50):
    print(i)

i = 10
while i <= 50:
    print(i)
    i += 1
 """
"""
#2

i = 10
while i > 0:
    print(i)
    i -= 1
"""
"""
#3
for i in range(0, 1000+1):
    if i % 2 == 0:
        print(i)
        i+=1
"""
"""
#4
x = int(input('Введите число: '))
for i in range(x, 0, -1):
    print(i)
"""
"""
i=int(input('Введите число: '))
while True:
    i -= 1
    print(i)
    if i == 0:
        break
"""
"""
#5
n = int(input('Введите число: '))
if n < 0:
    while True:
        n+=1
        print(n)
        if n == 0:
            break
elif n > 0:
    while True:
        n-=1
        print(n)
        if n == 0:
            break
else:
    print('недопустимое значение')
"""
"""
#6
for i in range(1, 100+1):
        print(f"{i} * 7 = {7 * i}")
"""
"""
#7
num = int(input('Введите число: '))
for i in range(1, 10+1):
       print(f"{i} * {num} = {num * i}")
"""
#8
"""
passUser = input('Введите пароль')

if passUser == '1':
    print('доступ разрешен')
else:

    while True:
        passUser = input('пароль не верный, Введите еще пароль')
        if passUser == '1':
            print('доступ разрешен')
            break

"""
"""
passUser = input('Введите пароль')
for i in range(1, 100+1):
    if passUser == '1':
        print('доступ разрешен')

    else:
        passUser = input('пароль не верный, Введите еще пароль')

"""
num = int(input('Введите число: '))
if num > 0:
    for i in range(1, 10+1):
       print(f"{i} * {num} = {num * i}")
