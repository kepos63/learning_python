from tkinter import *






root = Tk()

# Настройка окна
root.title('Авторизация | Регистрация')  # Названия окна
root.geometry('600x450')  # Размер окна (ширина/высота)
root['bg'] = '#000000'  # цвет фона можно указать hex или red
root.resizable(width=True, height=False)  # Право на изменение размера окна
try:
    root.iconbitmap('img/icon_login.ico')  # Подключение иконки
except TclError:
    pass  # Пустая команда

# Виджеты
lbl_info = Label(root, text='', bg='white', fg='white', font='Arial 20', width=10)
lbl_res = Label(root, text='', bg='red', fg='white', font='Arial 20', width=10)

btn_1 = Button(root, text='1', bg='#2B2B2D', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#727272' )
btn_2 = Button(root, text='2', bg='#2B2B2D', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#727272' )
btn_3 = Button(root, text='3', bg='#2B2B2D', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#727272' )
btn_4 = Button(root, text='4', bg='#2B2B2D', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#727272' )
btn_5 = Button(root, text='5', bg='#2B2B2D', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#727272' )
btn_6 = Button(root, text='6', bg='#2B2B2D', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#727272' )
btn_7 = Button(root, text='7', bg='#2B2B2D', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#727272' )
btn_8 = Button(root, text='8', bg='#2B2B2D', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#727272' )
btn_9 = Button(root, text='9', bg='#2B2B2D', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#727272' )
btn_0 = Button(root, text='0', bg='#2B2B2D', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#727272' )
btn_plus = Button(root, text='+', bg='#FF9F0A', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#FBC78E' )
btn_minus = Button(root, text='-', bg='#FF9F0A', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#FBC78E' )
btn_multiplied = Button(root, text='*', bg='#FF9F0A', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#FBC78E' )
btn_divide  = Button(root, text='/', bg='#FF9F0A', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#FBC78E' )
btn_equal = Button(root, text='=', bg='#FF9F0A', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#FBC78E' )
btn_comma = Button(root, text='.', bg='#2B2B2D', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#727272' )
btn_sing = Button(root, text='+/-', bg='#5C5C5E', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#8C8C8C' )
btn_percent = Button(root, text='%', bg='#5C5C5E', fg='Black', font='Consolas 14', height=1, width=3, activebackground='#8C8C8C')


# Упаковщик
lbl_info.grid(columnspan=6)
lbl_res.grid(row=1, columnspan=6)
#lbl_info.grid(row=0, column=1 )
#lbl_res.grid(row=1, column=1)
btn_1.grid(row=5, column=1, sticky="w")
btn_2.grid(row=5, column=2)
btn_3.grid(row=5, column=3)
btn_4.grid(row=4, column=1)
btn_5.grid(row=4, column=2)
btn_6.grid(row=4, column=3)
btn_7.grid(row=3, column=1)
btn_8.grid(row=3, column=2)
btn_9.grid(row=3, column=3)
btn_0.grid(row=6, column=2)
btn_divide.grid(row=2, column=4)
btn_multiplied.grid(row=3, column=4)
btn_minus.grid(row=4, column=4)
btn_plus.grid(row=5, column=4)
btn_equal.grid(row=6, column=4)
btn_comma.grid(row=6, column=3)
btn_sing.grid(row=2, column=2)
btn_percent.grid(row=2, column=3)



# Запуск окна
root.mainloop()