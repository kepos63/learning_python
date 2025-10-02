# Sqlite3
"""
import sqlite3
from pickle import GLOBAL
from random import randint

global db  # Объявили глобальную переменную db
global sql  # Объявили глобальную переменную sql

db = sqlite3.connect('test.db')  # Переменная для подключения к базе данных test.db
sql = db.cursor()  # Переменная для взаимодействия с базой данных

sql.execute('''CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT

)''')
# создание таблицы users в базе данных со строками login, password, cash

db.commit()  # Подтверждаем создание таблицы


def reg():
    user_login = input('Login: ')  # Ввод пользователем логина
    user_password = input('Password: ')  # Ввод пользователем пароль

    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')  # Выбрать столбец login в таблице users
    if sql.fetchone() is None:  # Проверка есть ли такая запись в столбце, если есть то выводится сообщение, что "такая запись уже есть"
        sql.execute(f'INSERT INTO users VALUES (?,?,?)',
                    (user_login, user_password, 0))  # Запись в строки в login, password, cash
        db.commit()  # Подтверждаем запись

        print('Вы зарегестрировались!')
    else:
        print('Такая запись уже имеется')

        for value in sql.execute('SELECT * FROM users'):  # Выводим содержимое таблицы users
            print(value)  # Вывод всей таблицы


def delete_db():
    sql.execute(f'DELETE FROM users WHERE login = "{user_login}"')
    db.commit()  # Подтверждаем

    print('Запись удалена!')


def casino():
    global user_login
    user_login = input('Log in: ')
    number = randint(1, 2)
    # в строку cash добавляем выйгрыш
    # Первый вариант
    for i in sql.execute(f'SELECT cash FROM users WHERE login = "{user_login}"'):
        balance = i[0]  # Создаем переменную balance и выбираем индекс 0
    # Второй вариант
    # sql.execute(f'SELECT cash FROM users WHERE login = "{user_login}"')
    # balance = sql.fetchone()  # выбираем первое значение

    # Проверяем есть ли логин в таблице, если его нет, то отправляем в функцию регистрации
    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        print('Такого логина не существует. Зарегистрируйтесь')
        reg()
    else:
        if number == 1:
            sql.execute(
                f'UPDATE users SET cash= {balance + 1000} WHERE login = "{user_login}"')  # Обновить в таблице users столбец cash на 1000, где логин введен пользователем
            db.commit()  # Подтверждаем
        else:
            print('Вы проиграли!')
            delete_db()


def enter():  # Функция вывод которая будет выводить два столбца login и cash
    #for i in sql.execute('SELECT login, cash FROM users'):
        #print(i)
    sql.execute(f'SELECT login, cash FROM users')
    row = sql.fetchall()[0][0]
    print(row)


def main():  # Запускаем все функции поочередно
    casino()
    enter()


main()
"""