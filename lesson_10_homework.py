import sqlite3
db = sqlite3.connect('university.db')
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


#add_students()
show_students()
#show_students_age()
#show_students_proger()
#update_age_student()
delete_student()
db.close()