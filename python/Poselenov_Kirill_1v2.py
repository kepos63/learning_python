from tkinter import *
import sqlite3, string

# Создаем / подключаем базу данных
db = sqlite3.connect('DataBases/auth.db')
cursor = db.cursor()

# Создание новой таблицы
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT,
    password TEXT, 
    balance INTEGER 
)""")
db.commit()


def check_pass():
    password = ent_password.get()
    abc = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    password_str = ''
    info = ''
    for el in password:
        if el in abc:
            password_str += str(el)
        else:
            lbl_info['text'] = "Введите пароль на английском языке!"
            info = lbl_info['text']
            return info

    return registration(password_str)


def registration(p):
    # print("Вы нажали на кнопку - Регистрация!")
    login = ent_login.get()
    password = p

    note = cursor.execute("""SELECT * FROM user WHERE login = ?""", [login]).fetchone()
    if note is None and len(password) >= 8 and (
            login != '' or password != ''):  # Проверка на существования пользователя и длинна пароля равна или более 8 символов
        cursor.execute("""INSERT INTO user (login, password, balance) VALUES (?,?,0)""", [login, password])
        db.commit()
        lbl_info['text'] = "Вы зарегистрировались!"
    elif 0 < len(password) < 8:  # Если длинна пароля меньше 8 символов, то вывести данное сообщение
        lbl_info['text'] = "Длинна пароля меньше 8 символов!"
    elif login == '' or password == '':
        lbl_info['text'] = "Вы указали пустые значения! "
    else:  # Если пользователь существует, то вывести данное сообщение.
        # print('Данный пользователь существует! ')
        lbl_info['text'] = "Данный пользователь существует! Авторизуйтесь!"


def authorization():
    login = ent_login.get()
    password = ent_password.get()
    note_login = cursor.execute("""SELECT * FROM user WHERE login = ? """, [login]).fetchone()

    # if note_login  is not  None and note_login[2] == password:
    #    lbl_info['text'] = f"Вы успешно авторизовались!! Баланс: {note_login[3]}"
    # else:
    #    lbl_info['text'] = "Вы успешно  не авторизовались!!"
    if note_login is None:
        lbl_info['text'] = "Пользователь не найден!"
    elif note_login[2] != password:
        lbl_info['text'] = "Пароль не верный!"
    else:
        lbl_info['text'] = f"{note_login[1]}, вы успешно авторизовались!\nБаланс: {note_login[3]} руб"


def show_pass():
    if ent_password['show'] == '*':
        ent_password['show'] = ''
        btn_show_pass['text'] = 'Убрать пароль'
    else:
        btn_show_pass['text'] = 'Показать пароль'
        ent_password['show'] = '*'


# Создание окна

root = Tk()

# Настройка окна
root.title('Авторизация | Регистрация')  # Названия окна
root.geometry('600x450')  # Размер окна (ширина/высота)
root['bg'] = '#4D4D5E'  # цвет фона можно указать hex или red
root.resizable(width=True, height=False)  # Право на изменение размера окна
try:
    root.iconbitmap('img/icon_login.ico')  # Подключение иконки
except TclError:
    pass  # Пустая команда

# Виджеты
lbl = Label(root, text='Промежуточная аттестация №1', bg='#4D4D5E', fg='white', font='Arial 20')
lbl_name_dev = Label(root, text='Разработчик: Поселенов Кирилл Евгеньевич', bg='#4D4D5E', fg='white',
                     font='Arial 15')  # Текстовый виджет (аналог print)
lbl_login = Label(root, text='логин', bg='#4D4D5E', fg='white', font='Consolas 14')
lbl_password = Label(root, text='пароль', bg='#4D4D5E', fg='white', font='Consolas 14')
ent_login = Entry(root, bg='white', fg='black', font='Consolas 14', justify='center',
                  width=40)  # Поле для ввода значения
ent_password = Entry(root, bg='white', fg='black', font='Consolas 14', justify='center', width=40, show='*')
btn_show_pass = Button(root, text='Показать пароль', bg='#D6D6E0', fg='Black', font='Consolas 14', command=show_pass)
btn_reg = Button(root, text='Регистрация', bg='#D6D6E0', fg='Black', font='Consolas 14', command=check_pass)
btn_auth = Button(root, text='Авторизация', bg='#D6D6E0', fg='Black', font='Consolas 14', command=authorization)
lbl_info = Label(root, text='', bg='#4D4D5E', fg='white', font='Consolas 14')
# Упаковщики

lbl.pack(pady=(10, 5))
lbl_name_dev.pack(pady=(5, 5))
lbl_login.pack(pady=(10, 5))
ent_login.pack(pady=(5, 5))
lbl_password.pack(pady=(5, 5))
ent_password.pack(pady=(5, 10))
btn_show_pass.pack()
btn_reg.pack(pady=(10, 5))
btn_auth.pack(pady=(5, 5))
lbl_info.pack()

# Запуск окна
root.mainloop()
