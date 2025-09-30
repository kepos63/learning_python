"""
# Модули, библиотеки, системные и сторониие
# Системные библиотеки
# import this

# Библиотека random
import random  # Подключаем библиотеку random
import datetime  # Подключаем библиотеку для работы со временем и датой
import time  # Подключаем библиотеку для работы со временем
import time, datetime, random, string  # Подключение несколько библиоте в одной строчке
import sys, os # sys, os библиотеки для работы ОС и проводником
import math # Библиотека для математических функций
from math import *

print('##################################Random###########################################')
x = random.randint(1, 100)  # Получение рандомного числа
y = random.randrange(1, 100)
print(f'Рандомное число: {x}')
print(f'Рандомное число: {y}')

abc = 'abcdefghij'
s = random.choice(abc)  # Получение рандомного символа из строки abc
print(f'Рандомный символ из строки "abc": {s}')

names = ['Александр', 'Кирилл', 'Елена']  # Получить случайный элемент
name = random.choice(names)
print(f'Радомный элемент: {name}')

print('##################################Datatime###########################################')

print(datetime.datetime.now())  # Получения текущего времени

print(f'Текущая дата: {datetime.date.today()}')
print(f'Текущий год: {datetime.datetime.now().year}')
print(f'Текущий месяц: {datetime.datetime.now().month}')
print(f'Текущий день: {datetime.datetime.now().day}')
print(f'Текущий час: {datetime.datetime.now().hour}')
print(f'Текущие минуты: {datetime.datetime.now().minute}')
print(f'Текущие сеук: {datetime.datetime.now().second}')
print(f'Текущие миле-секунды: {datetime.datetime.now().microsecond}')

print('##################################time###########################################')

print(f'Подождите 5 секунд...')
time.sleep(0)  # Задержка или пауза в коде в данном случае 5 секунд
print('Прошло 5 секунд твоей бесполезной жизни......')

print('##################################string###########################################')

abc1 = string.ascii_lowercase  # Полученгия английский алфавит в нижнем регистре
abc2 = string.ascii_uppercase  # Полученгия английский алфавит в верхнем регистре
abc3 = string.ascii_letters  # Полученгия английский алфавит и верхнем регистре и нижнем регистре
abc4 = string.digits  # Получения цифры
abc5 = string.punctuation  # Получения спец символов
print(abc1)
print(abc2)
print(abc3)
print(abc4)
print(abc5)

print('##################################math###########################################')
print(f'sin: {math.sin(x)}')
print(f'cos: {math.cos(x)}')
print(f'tan: {math.tan(x)}')
print(f'sqrt: {math.sqrt(16)}')
print(f'logX: {math.log(5, 10)}')
#from math import * - импортировать только определенные элементы из модуля
print(f'sin: {sin(1)}') # Если импортировать модуль через from можно сократить написание функции без указания модуля

print('##################################SYS OS###########################################')

print(f'Ваша ОС: {sys.platform}') #Платформа windows - win32, debian - linux
print(f'{sys.version}') #Версия python
#print(os.getcwd()) #Текущая директория
#print(os.chdir('c://test//')) #Перейти в директорию(сменить)
#print(os.mkdir('c:/test/test2')) #Создать директорию
print(os.listdir('c://test//test2//')) #Список файлов в директории
"""
import os
# 🔸Модули и библиотеки
import random, time, string

from pyexpat.errors import messages

"""
# 1 Игра кости. Пользователь угадывает число (вводит число от 1 до 6). Программа загадывает число (получает рандомное число от 1 до 6). Если пользователь угадывает число программы: вывести сообщение (вы победили). Иначе: (Вы проиграли. Выпало n).

try:
    num_user = int(input('Введите число от 1 до 6: '))
    num_prog = random.randint(1, 6)
    if 6 >= num_user >= 1:
        if num_user == num_prog:
            print(f'Вы победили')
        else:
            print(f'Вы проиграли. Выпало {num_prog}')
    else:
        print('Ошибка: Введите числа из диапазона от 1 до 6')
except ValueError:
    print(f'Ошибка: Введи число')
"""
"""
#2 Игра камень, ножницы, бумага. Программа загадывает предмет (получает рандомный элемент из списка кнб). Пользователь делает свой выбор (вводит камень, ножницы или бумага). Программа информирует пользователя о победе / проигрыше / ничья.

game_element = ['Камень', 'Ножницы', 'Бумага']
user_element = input('Сделайте выбор( Камень Ножницы или Бумана:')
try:
    random_element = random.choice(game_element)
    if random_element.lower() == user_element.lower():
        print('Ничья')
    elif (random_element.lower() == 'камень' and user_element == 'ножницы') or (random_element.lower() == 'ножницы' and user_element == 'бумага') or (random_element.lower() == 'бумага' and user_element == 'камень'):
        print('Вы проиграли ')
    else:
        print('Вы выйграли')
except ValueError:
    print('Цифры нельзя вводить... выберете предложеное значение... ')
"""
"""
#3. Полет Гагарина. Программа выводит сообщение (Начинаю обратный отсчет). Программа выводит числа от 10 до 0 с перерывом в 1 секунду, после чего сообщает об успешном запуске.
int('Начинаю обратный отсчет')
for i in range(10, 0, -1):
    print(f'{i}...')
    time.sleep(1)

print('Запуск')
"""
# 4Генератор паролей. Создайте программу, которое будет генерировать случайный пароль:
# Лайт: выводится рандомный пароль из 5 символов
# Среднее: Дополнительно пользователь указывает длину пароля
# Профи: Пользователь указывает длину пароля, выбирает алфавит.
"""

abc3 = string.ascii_letters
your_pass = []

for i in range(5):
    s = random.choice(abc3)
    if s not in your_pass:
        your_pass.append(s)
print(f'Твой пароль: {your_pass[0] + your_pass[1] + your_pass[2] + your_pass[3] + your_pass[4] + your_pass[5]}')
print(*your_pass, sep='')


#вариант 2 
mass = []
def mass_to_str(d):
    string = ''
    for element in d:
        string += str(element)
    return string

mass_to_str(mass)
#print(mass_to_str(mass))


user_add_long_pass = int(input('Укажите длинну пароля: '))
abc_2 = string.ascii_letters
your_pass_2 = []
for user_add_long_pass in range(user_add_long_pass, 0, -1):
    symbol_2 = random.choice(abc_2)
    if symbol_2 not in your_pass_2:
        your_pass_2.append(symbol_2)
#print(your_pass)
print(mass_to_str(your_pass_2))


#Средний
abc_1 = string.ascii_letters
your_pass_1=[]
for i in range(5):
    symbol_1 = random.choice(abc_1)
    if symbol_1 not in your_pass_1:
        your_pass_1.append(symbol_1)
#print(your_pass)
print(mass_to_str(your_pass_1))

#ХАРД
def abc_rus_eng(a, b):
    your_pass_3 = []   
    for b in range(b, 0, -1):
        if a.lower() == 'rus':
            abc_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
            symbol_3 = random.choice(abc_rus)
            if symbol_3 not in your_pass_3:
                your_pass_3.append(symbol_3)
        else:
            abc_eng = string.ascii_letters
            symbol_3 = random.choice(abc_eng)
            if symbol_3 not in your_pass_3:
                your_pass_3.append(symbol_3)      
    return mass_to_str(your_pass_3) 

user_add_long_pass = int(input('Укажите длинну пароля: '))
user_sel_lang = input('Выберите язык(rus или eng): ')

print(abc_rus_eng(user_sel_lang, user_add_long_pass))

"""
"""
#6
crap_1 = int(input('Введите количество сторон для 1 кубика:'))
crap_2 = int(input('Введите количество сторон для 2 кубика:'))
enter = input('Нажмите на Enter, чтобы бросить кости....')

if crap_1 and crap_2 in (4, 6, 8, 10):
    print(f'Кубик d{crap_1}: {random.randint(1, crap_1)}')
    print(f'Кубик d{crap_2}: {random.randint(1, crap_2)}')

else: 
    print('Введите числа 4, 6, 8, 10')

"""
"""
#7
#Лайт
s = ['Участник 1', 'Участник 2', 'Участник 3', 'Участник 4', 'Участник 5', 'Участник 6', 'Участник 7', 'Участник 8', 'Участник 9', 'Участник 10']
#print(f'Победил: {str(random.choices(s))}')
"""
"""
#Среднее
s = ['Участник 1', 'Участник 2', 'Участник 3', 'Участник 4', 'Участник 5', 'Участник 6', 'Участник 7', 'Участник 8', 'Участник 9', 'Участник 10']
n = int(input('введите число от 1 до 3: '))
while n > 0:
    n -=1
    print(f'Призеры: {str(random.choices(s))}')
"""

"""
#Профи

def winner(n):
    s = ['Участник 1', 'Участник 2', 'Участник 3', 'Участник 4', 'Участник 5', 'Участник 6', 'Участник 7', 'Участник 8',
         'Участник 9', 'Участник 10']
    p = ['Приз 1', 'Приз 2', 'Приз 3', 'Приз 4', 'Приз 5']
    x = ''
    for i in range(n):
        print(f'Призеры: {random.choice(s)}, приз: {random.choices(p)}')
        
num = int(input('введите число от 1 до 3: '))
winner(num)
"""
"""
#8

def create_folder(no,nc):
    for i in range(no, nc + 1):
        print(i)
        os.chdir('C:/Users/Student_python/Documents/python/')
        name_folder = ('lesson_' + str(i) + '.py')
        os.open(f'{name_folder}', os.O_CREAT | os.O_WRONLY)
num_folder_open = 10
num_folder_close = 15
create_folder(num_folder_open, num_folder_close)
"""
"""
#Профи препод
import random

s = ["Участник 1", "Участник 2","Участник 3", "Участник 4", "Участник 5", "Участник 6", "Участник 7", "Участник 8", "Участник 9", "Участник 10"]
p = ["Ноутбук", "Планшет", "Телефон"]
n = int(input("Введите количество призеров: "))
winners = []
prizes = []

if 1 <= n <= 3:
    while len(winners) != n:
        winner = random.choice(s)
        prize = random.choice(p)
        if winner not in winners:
            winners.append(winner)
            prizes.append(prize)
else:
    print("Вы ввели некорректный диапазон")

i = 0
while i < len(winners):
    print("--------------------------------------------------------")
    print(f"Победитель: {winners[i]}\nполучает приз: {prizes[i]}")
    i += 1
"""
# 9
import datetime, time

"""
user_month = datetime.date.today().month
if user_month in (12, 1, 2):
    #print('Зимняя распродажа')
    season = 'ЗИМНЯЯ'
elif user_month in (3, 4, 5):
    #print('Весеняя распродажа')
    season = 'ВЕСЕННЯЯ'
elif user_month in (6, 7, 8):
    #print('Летняя распродажа')
    season = 'ЛЕТНЯЯ'
else:
    season = 'ОСЕННЯЯ'
    #print('Осеняя распродажа')
date_sale_hour = datetime.datetime.now().hour + 3
print(f' {season} распродажа закончится в: {date_sale_hour}:00:00')
"""
"""
user_month = 4
date_sale_hour = datetime.datetime.now().hour + 3
print(f' ВЕСЕННЯЯ распродажа закончится в {date_sale_hour}:00:00')
"""

"""


s = ["Участник 1", "Участник 2","Участник 3", "Участник 4", "Участник 5", "Участник 6", "Участник 7", "Участник 8", "Участник 9", "Участник 10"]
p = ["100 рублей", "200 рублей", "300 рублей"]
winner = []
while True:
    try:
        k = int(input("Введите количество призеров от 1 до 3: "))
        if 1 <= k <= 3:
            while len(winner) != k:
                x = random.choice(s)
                if x not in winner:
                    winner.append(x)
            print(f"Победитель розыгрыша призов: {winner}")
            print(f"Призы участников:")
            for element in winner:
                print(f"{element} - {random.choice(p)}")
            break
        else:
            print("Введено не верное количество участников.")
    except ValueError:
        print("Ошибка: Введено не число! ")
"""
import random, string, math

# 10

# y_i - Номер i-того символа в закрытом тексте
# x_i — номер i-того символа в открытом тексте
# k — ключ
# n — число символов в алфавите
# yi = (xi + k) mod n  - формула для шифрования
# xi = ( yi + (n - k)) mod n
"""
mess = input('Введите сообщение: ')
k = int(input('Введите ключ: '))
abc3 = string.ascii_letters
ces = ''
for i in mess:
    print(i)
    if i in abc3:
        element = abc3.index(i)
        if element <= 26:
            y_i = (element + k) % len(abc3)
            ces += str(abc3[y_i])
            # break
        else:
            y_i = (element + k) % len(abc3)
            ces += str(abc3[y_i])
    else:
        print('Введите сообщение на анг')
        exit()
print('Ввели', ces)
"""
while True:
    try:
        mess = input(
            'Введите сообщение состоящее исключительно из символов английского алфавита, которое хотите зашифровать: ')
        key = int(input('Введите ключ: '))
        abc3 = string.ascii_letters

        def eng_letter(let, k):
            ces = ''
            for i in let:
                if i not in abc3:
                    new_let = 'Ошибка: Ах, Балдаа, сказали же состоящее исключительно из символов английского алфавита!!!'
                    return new_let
                else:
                    element = abc3.index(i)
                    if element <= 26:
                        y_i = (element + k) % len(abc3)
                        ces += str(abc3[y_i])
                        # break
                    else:
                        y_i = (element + k) % len(abc3)
                        ces += str(abc3[y_i])
            return ces

        print(eng_letter(mess, key))
    except ValueError:
            print('Ошибка: Введите число')
