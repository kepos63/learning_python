class Home:  # Создали класс Home, чтобы отличить от функций, классы пишут с заглавной буквы
    number = None  # Элементы(переменные) внутри класса называются поля.
    address = None
    apartments = None

    # Конструктор __init__(функция будет вызываться в момент создания объекта)
    def __init__(self, number = None,address = None,apartments = None):
        self.number = number
        self.address = address
        self.apartments = apartments
        print('-----------------------------------------------------------')
        print('Вы создали новый объект!')
        print(f'|Номер {self.number}\n{self.address}\n({self.apartments})|')
        print('-----------------------------------------------------------')



    # Функция класса, которая выводит значения полей класса
    def show_info(self):
        print('-----------------------------------------------------------')
        print(f'|Номер {self.number}\n{self.address}\n({self.apartments})|')


    def info(self, number = 1, address = None, apartments = None): # Указали значения по умолчанию для параметров, если они не будут переданы
        self.number = number
        self.address = address
        self.apartments = apartments


# Создаем объект и указываем значения передаваемых параметров для функции __init__
house = Home(1, '40 лет победы, 11а', 125)


class School(Home):
    num_class_room = None
    num_students = None
    __phone_director = '+7 955 563 22 22'
    # Полиморфизм - замена apartments на num_class_room и добавление num_students
    def __init__(self, number = None,address = None, num_class_room = None, num_students = None):
        self.number = number
        self.address = address
        self.num_class_room = num_class_room
        self.num_students = num_students
        print('-----------------------------------------------------------')
        print('Вы создали новый объект!')
        print(f'|Номер {self.number}\n{self.address}\nКоличестве классов: ({self.num_class_room} / учеников:{self.num_students})|')
        print('-----------------------------------------------------------')



# Класс наследник (родитель - класс Home)
class Hospital(Home):
    pass


# Создаем объект и указываем значения передаваемых параметров для функции __init__
school2 = School(2, '40 лет победы, 17а',  50, 1500)
school2.num_class_room = 50
school2.num_students = 1500


