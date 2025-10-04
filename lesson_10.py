# Создание новой записи в таблице user (запрос SQL)

def fun1():
    cursor.execute("""INSERT INTO user VALUES (1, "admin", "123")  """)
    db.commit()
    print("Запись создана успешно!")


# Создаем функцию для записи данных пользователя
def add_user_date():
    id_1 = int(input())
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    cursor.execute("""INSERT INTO user (login, password) VALUES (?, ?)""", [login, password])
    db.commit()
    print("Запись создана успешно!")

def output_base():
    print('---------------------------------------------')
    for note in cursor.execute("""SELECT * FROM user"""):
        #print(note)
        print(f'id: {note[0]} | login: {note[1]} | password: {note[2]}')
    print('---------------------------------------------')
#Изменение (обновление) записей в таблицу (запрос SQL)
def update_base():
    cursor.execute("""UPDATE user SET password = "новый пароль" WHERE login = "kepos" """)
    db.commit()
    print('Запись(и) изменены успешно!')
#Удаление записи в таблицу (запрос SQL) WHERE (ГДЕ) - отбор записей по условию!
def delete_note():
    cursor.execute(""" DELETE FROM user WHERE id = 1 """ )
    db.commit()
    print('Запись(и) удалена(ы) успешно!')

def output_column():
    print('---------------------------------------------')
    for note in cursor.execute("""SELECT login, password FROM user WHERE login = "к" AND password = "к" """):
        #print(note)
        print(f'| login: {note[0]} | password: {note[1]}|')
    print('---------------------------------------------')
#boolien SQL
# равно = или ==
# не равно <> или !=
# Больше, меньше >,<
# Меньше либо равно, Больше или равно <= , >=


# SQLite практика
import sqlite3  # Подключение библиотеки по работе с базой данных

db = sqlite3.connect('server.db')  # Подключение / создание базы данных
cursor = db.cursor()  # Переменная для взаимодействия с базой данных

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS user (id INT, login TEXT, password TEXT)
    
   """)
#Типы данных SQLite 3
cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL
#)""")
3
def add_product():
    name_product = input('Введите название: ')
    price = float(input('Введите стоимость товара: '))
    cursor.execute(""" INSERT INTO product (name , price) VALUES (?, ?)""", [name_product, price])
    db.commit()
    print('Товар добавлен!')

    for note in cursor.execute("SELECT * FROM product"):
        print(f'ID: {note[0]} | Название книги: {note[1]} | Стоимость: {note[2]}')



db.commit()  # Подтверждаем создание изменений в БД
print('Таблицы user и product создана успешно!')





#fun1()
#add_user_date()
#update_base()
#delete_note()
#output_base()
#output_column()

add_product()




db.close()  # Закрытие базы данных



