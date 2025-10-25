#Функции def, return, передаваевый параметры
from zoneinfo import reset_tzpath

"""
def helloworld():
    print("Hello \nWorld!")


def sum_ab(a, b):           #a и b - внутренние переменные
    print(f'a + b = {a + b}')


helloworld() #Вызов функции
#def sum_ab(a, b)               # Функция с передаваемыми параметрами. a и b - передаваемый параметр


sum_ab(2, 5)
sum_ab(6, 7)

num1 = int(input('a = '))   #внешняя переменная
num2 = int(input('b = '))   #внешняя переменная
sum_ab(num1, num2)          #Функция с передаваемыми параметрами. a и b - передаваемый параметр


#Функция конвертации температуры

def conv(tc):
    tf = tc * 9 / 5 + 32
    return tf               #Возращаем результат выполнения функции, которая выводит результат с помощью команды print()

#Конвертируется температура из Цельсия в Фаренгейты
print(conv(10))             #Вызываем функцию со занчением 10
print(conv(100))




def run_all():
    helloworld()
    sum_ab(10, 5)
    print(conv(10))


run_all()
"""
#Функция которая вызывает сама себя называется рекурсивной функцией.
#Факториал !4 это произведений всех вход чисел 1,2,3,4

"""
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
print(factorial(1))
"""

"""
def factorial2(n):
    if n == 1:
        return 1
    else:
        return factorial2(n-1) * n

#print(factorial2(0))
print(f'5!={factorial2(5)}')

"""
"""
#1
def helloworld():
    for i in range(5):
       print('Hello!')
print(helloworld())
print(helloworld())
print(helloworld())
"""
#2
"""
def xyz(a, b, c):
    print(f'(x + y + z)2 = {(a**2 + b**2 + c**2)}')
    print(f'(x + y + z)2 = {(a+b+c)**2}')

xyz(int(input('x = ')), int(input('y = ')), int(input('z = ')))
"""
"""
#3

def bigger_smoller_number(a, b, c):
    if a > b and a > c:
        if b > a:
            return print(f' Наибольшее число {a}, Н1аименьшее число {b}')
        else:
            return print(f' Наибольшее число {a}, Наименьшее число {c}')
    elif b > a and b > c:
        if c > a:
            return print(f' Наибольшее число {b}, Наименьшее число {a}')
        else:
            return print(f' Наибольшее число {b}, Наименьшее число {c}')
    elif c > a and c > b:
        if a > b:
            return print(f' Наибольшее число {c}, Наименьшее число {b}')
        else:
            return print(f' Наибольшее число {c}, Наименьшее число {a}')
    return None
bigger_smoller_number(int(input('a = ')), int(input('b = ')), int(input('c = ')))
"""
"""
#4 НЕ ПОНЯТНО 
def nod(a,b):
    return f'a = {b}, b = {a % b}'





print(nod(5, 2))
"""
"""
#5
def ver_pass(a):
    if a == '1':
        return True
    else:
        return False


print(ver_pass('1'))
"""
"""
#6
def calc(a, b, c):

    if c == '/':
        return f"{a / b}"
    elif c == '+':
        return f"{a + b}"
    elif c == '-':
        return f"{a - b}"
    else:
        return f"{a * b}"


print(calc(int(input('Первое число = ')), int(input('Второе число = ')), input('Введи знак *, /, +, -:')))
"""
"""
#7
def geometria(a, b):
    if a == b:
        print(f' Площадь равна = {a**2}, Периметр = {4*a}, ЭТО КВАдрат')
    else:
        print(f' Площадь равна = {a*b}, Периметр = {2*(a+b)}, ЭТО Прямоугольник')


geometria(2,2)
"""
"""
#Доп
print(eval("3*5+1"))
print(eval(input("Введите арифметическое выражение: ")))
"""
