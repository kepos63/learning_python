# ООП, Классы и объекты. Поля, конструкторы, инкапсуляция, полиморфизм, наследование
from email.errors import NonASCIILocalPartDefect

"""
class Home:  # Создали класс Home, чтобы отличить от функций, классы пишут с заглавной буквы
    number = None  # Элементы(переменные) внутри класса называются поля.
    address = None
    apartments = None
    # Функция класса, которая выводит значения полей класса
    def show_info(self):
        print('-----------------------------------------------------------')
        print(f'|Номер {self.number}\n{self.address}\n({self.apartments})|')

    # Функция класса, которая позволяет быстро заполнить поля класса
    def get_info(self, number, address, apartments):
        self.number = number
        self.address = address
        self.apartments = apartments

    def get_info_v2(self, number = 1, address = None, apartments = None): # Указали значения по умолчанию для параметров, если они не будут переданы
        self.number = number
        self.address = address
        self.apartments = apartments


# Создание объекта (инициализация класса)
home1 = Home()
home1.number = 1  # Заполнение полей
home1.address = 'ул. Самарская, 12'
home1.apartments = 150

#print(home1.number, home1.address, home1.apartments)

# Создание второго объекта
home2 = Home()
home2.number = 2  # Заполнение полей
home2.address = 'ул. Московская, 3'
#home2.apartments = 250

#print(home2.number, home2.address, home2.apartments)

home1.show_info() # Вызов функции для объекта home1
home2.show_info()

home3 = Home()
a = 3
b = 'ул. Санфирова, 951'
c = None
home3.get_info(a, b , c)
home3.show_info()
home4 = Home()
home4.get_info_v2()
home4.show_info()
home4.get_info_v2(2, '40 лет победы', 1213)
home4.show_info()
"""
#1 и 2
"""
class Employee:
    name = None
    surname = None
    cash = None

    def get_full_name(self):
        full_name =  self.surname +' '+ self.name
        print(f'ФИО сотрудника: {full_name}')

    def get_annual_salary(self):

        print(f'Годовая зарплата {self.surname} равно {self.cash*12}')



workers = Employee()
workers.name = 'Кирилл'
workers.surname = 'Поселенов'
workers.cash = 20000

workers.get_full_name()
workers.get_annual_salary()
"""



#3
"""
class Rectangle:
    width = None
    height = None

    def area(self):
        print(self.width * self.height)

    def perimeter(self):
        print(2*(self.width + self.height))

    def is_square(self):
        if self.height == self.width:
            print("Это квадрат")
        else:
            print("Это прямоугольник")

    def resize(self, h, w):
        self.height = h
        self.width = w
        print(f'Новая длинна  = {self.height} Новая ширина = {self.width}')

area1 = Rectangle()
area1.width = 10
area1.height = 20
area1.area()
area1.perimeter()
area1.is_square()
area1.resize(30, 10)
"""
#4
"""
import random

class Cube:
    num_sides = None # Количество сторон
    num_drop =  random.randint(1, 6)  # Выпавшее число
    def set_value(self, sides):
        self.num_sides = sides
        print(f'Количество сторон равно: {self.num_sides}')


    def roll_a_dice(self):
        print(f'Выпало число: {self.num_drop}')



cube1 = Cube()
cube1.num_sides = 5
#cube1.num_drop = 7
cube1.set_value(5)
cube1.roll_a_dice()
"""
#5
"""
class Cube_v2:
    num_sides = None # Количество сторон
    num_drop = None  # Выпавшее число
    def set_value(self, sides = 6):
        self.num_sides = sides
        print(f'Количество сторон равно: {self.num_sides}')


    def roll_a_dice(self):
        print(f'Выпало число: {self.num_drop}')



cube1 = Cube_v2()
cube1.num_sides = 5
cube1.num_drop = 7
cube1.set_value()
cube1.roll_a_dice()
"""
#6
"""
class Employee:
    name = None
    surname = None
    cash = None

    def get_full_name(self):
        full_name =  self.surname +' '+ self.name
        print('-----------------------------------------------------')
        print(f'ФИО сотрудника: {full_name}')


    def get_annual_salary(self):

        print(f'Годовая зарплата {self.surname} равно {self.cash*12}')
        print('-----------------------------------------------------')



workers0 = Employee()
workers0.name = 'Кирилл'
workers0.surname = 'Поселенов'
workers0.cash = 20000

workers1 = Employee()
workers1.name = 'Иван'
workers1.surname = 'Петров'
workers1.cash = 5000

workers2 = Employee()
workers2.name = 'Петр'
workers2.surname = 'Иванов'
workers2.cash = 10000

workers3 = Employee()
workers3.name = 'Сергей'
workers3.surname = 'Сидоров'
workers3.cash = 200000

workers4 = Employee()
workers4.name = 'Артем'
workers4.surname = 'Ушаков'
workers4.cash = 90000

workers0.get_full_name()
workers0.get_annual_salary()
workers1.get_full_name()
workers1.get_annual_salary()
workers2.get_full_name()
workers2.get_annual_salary()
workers3.get_full_name()
workers3.get_annual_salary()
workers4.get_full_name()
workers4.get_annual_salary()
"""

#7
"""
class Product:
    name = None
    price = None
    category = None
    lot = None
"""

#8

class Product:
    name = None
    price = None
    category = None
    quantity = None


    def add_stock(self, quantity): # quantity-количество, добавление товара на склад
        self.quantity += quantity
        print('--------------------------------------------------------')
        print(f'Товар добавлен! Категория: {self.category} | Название: {self.name} | Цена: {self.price}| Количество: {self.quantity} | Добавление: {quantity}')
    def sell(self, quantity):# продажа товара (проверять наличие)
        if self.quantity > 0: # self.quantity >= quantity
           # self.quantity -= quantity
            print(f'Товар {self.name}  остаток {self.quantity - quantity}. ')# проверка наличия
        else:
            print(f'Товар закончился')
    def apply_discount(self, percent = 10): # применение скидки
        self.price *= (100 - percent) / 100
        print('--------------------------------------------------------')
        print(f'Cкидка на категорию {self.category} составляет {percent} % итоговая цена: {self.price}')
    def check_availability(self, new_quality):
        print('--------------------------------------------------------')
        #if self.quantity > 0:
        #    print(f'Товар {self.name} в наличии. ')# проверка наличия
        #else:
        #    print(f'Товар закончился')
        if new_quality is None:
            print(f'Товар: {self.name}\nОстаток: {self.quantity}')
        else:
            if self.quantity >= new_quality:
                print('Товар в наличии!')
            else:
                print('Товар закончился!')

    def get_product_value(self):    # расчет общей стоимости товара на складе
        
        print(f'Общая стоимость товара: {self.quantity * self.price}')


product1 = Product()
product1.name = 'Питон от а до я'
product1.price = 1500
product1.category = 'Книги'
product1.quantity = 100

product2 = Product()
product2.name = 'Тайт'
product2.price = 500
product2.category = 'Стиральный порошок'
product2.quantity = 50

product3 = Product()
product3.name = 'CPU-i7-14700k'
product3.price = 150000
product3.category = 'CPU'
product3.quantity = 30


product1.add_stock(100)
product1.sell(5)
product1.apply_discount(30)
product1.check_availability()
product1.get_product_value()


"""
 Три основных принципов ООП:
 1. Наследование
 2. Полиморфизм
 3. Инкапсуляция
"""