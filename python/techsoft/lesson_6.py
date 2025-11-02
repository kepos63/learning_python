"""
# Списки, словари

colors = ["red", "black", "white", "orange"]
print(colors)
"""
from traceback import print_tb

from ctypes.macholib.framework import framework_info
from turtledemo.sorting_animate import enable_keys

"""
# индексы и срезы
s1 = [3, 5, 10, 123, -5, 0, 89]
s2 = [123, "строка", 0.25, True, False, [12, 5, 2], "привет"]

print(f'one elements list: {s1[2]}')
#print(f'Срез 2 элементов списка: {colors[:2]}')
#print(f'Срез 2 элементов списка: {colors[-1:]}')
print(f'Вывод элемента внутреннего списка: {s2[5][0]}') #выберем элемент внутри списка списка
print(f'Вывод символа внутреннего строки: {s2[-1][2]}')
"""
"""
#Арифметика

print(s1+s2)
print(s1*3)
"""
"""
#Замена значения элементов
s1[1] = 20
print(s1)
"""
"""
#Перебор
s1 = [3, 5, 10, 123, -5, 0, 89]
print('----------элементы списка-----------')
for element in s1:
    print(element)
print('-------------------------------------')

s2 = "Привет"
print('----------элементы строки-----------')
for element in s2:
    print(element)
print('-------------------------------------')

s3 = [3, 5, 10, 123, -5, 0, 89]
print('----------Пополнение баллов-----------')
for i in range(0, len(s3)):
    s3[i] += 100
print(s3)
print('-------------------------------------')
"""
"""
#Команды
num = [3, 5, 10, 123, -5, 0, 89]
print(f'длина строки: {len(num)}')
print(f'Максимальное значение списка: {max(num)}')
print(f'Минимальное значение списка: {min(num)}')

 if 10 in num:
    print(f'Число 10 содержится в списке. Значение: {10 in num}')

if 1 not in num:
    print(f'Число 1 не содержится в списке. Значение: {1 in num}')

num.append(234) #не возвращает значение функцией print() добавляем элемента
print(f'Добавить элемент в конец списка:  {num}')

num.pop(-1) #обращаемся к индексу
print(f'Удаляем элемент с индексом -1:  {num}')

print(f'Удаляем элемент с индексом 123:  {num.index(123)}')

print(f'Количество повторений определенного элемента: {num.count(5)}')
print(f'Сумма элементов: {sum(numbers)}'

num.sort()
print(f'Отсортированный списко: {num}')
num.reverse())
"""

#🔸Списки и словари
"""
#1Создайте список, состоящий из 5 фамилий.
surname = ["Ivanov", "Petrov", "Sidorov", "Sergeev", "Snow"]
print(f'Список студентов: {surname}')
"""
"""
#2Создайте список чисел и найдите сумму, среднее и максимум.
num = [1, 2, 3, 4, 5, 6, 7]
print(f'Сумма чисел: {sum(num)}\nСреднее значение: {(sum(num))/len(num)}\nМаксимальное занчение: {max(num)}')

"""
"""
#3Удалите дубликаты из списка. Отсортируйте список. Вывести их индексы и значения.
num = [1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 9, 10]



new_num =[]

for element in num:
    if element not in new_num:
        new_num.append(element)
print(new_num)

for i in range(0, len(num)):
    if i < len(num):
        ind = i
        el = num[i]
        



"""
"""
#4

surname = ["Иванов", "Петров", "Сидоров", "Поселенов", "Snow"]
new_surname = []

for element in surname:
    if len(new_surname) < len(element):
        new_surname = element
print(new_surname)
"""
"""
#5
add_surname = input('Введите фамилию: ')
surname = ["Иванов", "Петров", "Сидоров", "Поселенов", "Snow"]
if add_surname in surname:
    print('доступ разрешен')
else:
    print('данного участника нету в списке')
"""
"""
#6
color = []

i = 0
while i < 5:
    user_add_color = input('Введите цвет: ')
    color.append(user_add_color)
    i += 1
print(color)
"""
"""
#7  Создайте пустой список ([]). ПОКА пользователь не введет значение 0: Программа будет запрашивать у пользователя ввести число и будет добавлять это значение к пустому списку. После того, как пользователь ввел значение 0 (этот элемент не должен добавляться к списку): программа выводит отсортированный список без повторяющихся элементов.

num  = []
add_user_num = int(input('Введите число: '))
while add_user_num != '0':
    if add_user_num not in num:
        num.append(add_user_num)
        add_user_num = int(input('Введите число: '))
    else:
        add_user_num = int(input('Введите число: '))
num.sort()
print(num)
"""
"""
#8 Привет, Алиса v2. Пользователь вводит сообщение (например: Привет). ЕСЛИ он ввел привет: вывести сообщение (Привет). Но нужно учитывать, что пользователь может ввести любое значение из этого списка: (Привет, прив, приветствую, бонжур, хелло, hello, hi).

user_words = input('Введите сообщение: ')
hello_list = ['Привет', 'Прив', 'приветсвую', 'бонжур', 'хелло', 'hello', 'hi']

if user_words in hello_list:
    print('привет')
else:
    print('Комманда не опознана')
    
"""
"""
#3
num = [9, 2, 3, 4, 5, 6, 7, 2, 3, 4, 1, 10]
new_num = []
for element in num:
    if element not in new_num:
        new_num.append(element)
new_num.sort()
print(new_num)

"""


