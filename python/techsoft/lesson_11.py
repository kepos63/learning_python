import sqlite3
db = sqlite3.connect('DataBases/university.db')
sql = db.cursor()

sql.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    age INTEGER,
    speciality TEXT
)""")

def add_students():

    for i in range(5):
        name = input('Введите Имя: ')
        surname = input('Введите Фамилию: ')
        age = int(input('Введите ваш возраст: '))
        speciality = input('Введите вашу профессию: ')

        sql.execute("""INSERT INTO students (name, surname, age, speciality) VALUES (?, ?, ?, ?)""", (name, surname, age, speciality))
        db.commit()
    print('Ваша запись добавлена! ')

def show_students():
    for note in sql.execute('SELECT * FROM students'):
        print(f'Студент | Номер: {note[0]} | Имя: {note[1]} | Фамилия: {note[2]} | Возраст: {note[3]} | Профессия: {note[4]}')


def show_students_age():
    for note in sql.execute("""SELECT id, name, surname, age, speciality FROM students WHERE age >= 35 """):
        print(f'Студент | Номер: {note[0]} | Имя: {note[1]} | Фамилия: {note[2]} | Возраст: {note[3]} | Профессия: {note[4]}')

def show_students_proger():
    for note in sql.execute("""SELECT id, name, surname, age, speciality FROM students WHERE speciality = "Программист" """):
        print(f'Студент | Номер: {note[0]} | Имя: {note[1]} | Фамилия: {note[2]} | Возраст: {note[3]} | Профессия: {note[4]}')

def update_age_student():
    sql.execute(""" UPDATE students SET age = "22" WHERE id = "1" """)
    db.commit()
    print('Запись(и) изменены успешно!')
def delete_student():
    sql.execute("""DELETE FROM students WHERE id = "3" """)
    db.commit()
    print('Запись(и) удалена(ы) успешно!')





def fun7():
    res = sql.execute("""SELECT * FROM students WHERE speciality = "Программист" """).fetchone() # Получить первое значение вернуть,  результат
    print(res)
    #for note in sql.execute("""SELECT * FROM students WHERE speciality = "Программист" """).fetchone():
        #print(note)

def fun8():
    for note in sql.execute("""SELECT name FROM students"""):
        print(note[0])
# Данные функции лучше использовать в цикле
def fun9():

    for note in sql.execute("""SELECT COUNT(*) FROM students"""): # Подсчет записей в таблице
       print(f'количество записей в таблице students: {note[0]}')
    #for note in sql.execute("""SELECT COUNT(name) FROM students"""): # Количество не пустых значений в строке name из таблице students
    #   print(f'количество записей в таблице students: {note[0]}')
    #for note in sql.execute("""SELECT COUNT(DISTINCT speciality) FROM students"""): # Количество уникальных значений в строке speciality из таблицы students
        #print(f'количество записей в таблице students: {note[0]}')
    #for note in sql.execute("""SELECT SUM(id) FROM students"""): # Сумма столбца id в таблице students
        #print(f'количество записей в таблице students: {note[0]}')


def age_studentsv1():
    for note in sql.execute("""SELECT AVG(age) FROM students"""): # Подсчет записей в таблице
       print(f'Средний возраст студентов: {note[0]}')
    for note in sql.execute("""SELECT MIN(age) FROM students"""): # Подсчет записей в таблице
       print(f'Средний возраст студентов: {note[0]}')
    for note in sql.execute("""SELECT MAX(age) FROM students"""): # Подсчет записей в таблице
       print(f'Средний возраст студентов: {note[0]}')
def age_studentsv2():

    avg_students = sql.execute("""SELECT avg(age) FROM students""").fetchone()[0]
    #print(avg_students[0])
    print(avg_students)
    min_students = sql.execute("""SELECT MIN(age), surname FROM students""").fetchone()
    print(f'Возраст самого молодого студента: {min_students[0]} - {min_students[1]}')
    for note in sql.execute("""SELECT * FROM students """):
        print(note)




sql.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    balance INTEGER
    
)""")

def add_user_teachersv1():

    for i in range(5):
        user = input('Введите имя: ')
        balance = int(input('Введите баланс: '))
        sql.execute("""INSERT INTO teachers (user, balance) VALUES (?,?)""", [user, balance])
        db.commit()
        print('Запись добавлена!')
def update_balance_reduce():
    for res in sql.execute("""SELECT balance FROM teachers WHERE user = "Алиса" """):
        #print(res[0])
        sql.execute(f' UPDATE teachers SET balance = {res[0] - 100}  WHERE user = "Алиса" ')
        db.commit()
        print('Баланс уменьшен! ')
def update_balance_increase():
    for res in sql.execute("""SELECT balance FROM teachers WHERE user = "Иван" """):
        #print(res[0])
        sql.execute(f' UPDATE teachers SET balance = {res[0] + 100}  WHERE user = "Иван" ')
        db.commit()
        print('Баланс увеличен! ')

def check_balancev1():
    for res in sql.execute("""SELECT balance FROM teachers WHERE user = "Алиса" """):
        if res[0] > 500:
            print('Денежные средства достаточно для снятия')
        else:
            print('Денежные средств не достаточно для снятия')




def check_balancev2():
    cash = sql.execute("""SELECT balance FROM teachers WHERE user = "Алиса" """).fetchone()
    cash_out = int(input("Введи сумму которую хотите снять: "))
    if cash[0] >= cash_out:
        sql.execute(f' UPDATE teachers SET balance = {cash[0] - cash_out}  WHERE user = "Алиса" ')
        db.commit()
        print(f'Денежные средства достаточно для снятия! Остаток баланса:{cash[0]}')
        #print(cash[0])
    else:
        print(f'Денежные средств не достаточно для снятия, доступный баланс равен: {cash[0]}')

def red():
    x = int(input("Введите число, насколько изменить баланс: "))
    y = input("Введите имя пользователя: ")
    sql.execute("""UPDATE teachers SET balance = balance + ? WHERE user = ? """, (x, y))
    db.commit()
    print('Баланс изменен успешно')

#age_studentsv2()
#check_balancev2()
#check_balancev1()
#update_balance_uppers()
#add_user_teachers()
# age_students()
# add_students()
# show_students()
# show_students_age()
# show_students_proger()
# update_age_student()
# delete_student()
# fun9()
while True:
    command = input("Введите команду: ")
    if command == 'добавить 5 записей':
        add_user_teachersv1()
    else:
        print('Вы ввели неверную команду!')
        break


db.close()
# Подключение module и использование функции module и переменных
#from module import *
"""
import module
module.hello()
print(module.name)
print(module.url)

# Подключение пакета
import modules.modules as modules
modules.hello()
print(modules.name)
print(modules.url)
"""