# Функции для Игры
def create_element(x, y, color):
   size = 25
   canvas.create_rectangle((x-0.5) * size, (y-0.5) * size, (x+0.5) * size, (y+0.5) * size, fill=color, width=0)


def create_snakev1():
    global tabel_xv1, tabel_yv1
    i = 0
    while i < len(tabel_xv1):
        create_element(tabel_xv1[i], tabel_yv1[i], color='gold')
        i+=1
def create_snakev2():
    global tabel_xv2, tabel_yv2
    i = 0
    while i < len(tabel_xv2):
        create_element(tabel_xv2[i], tabel_yv2[i], color='silver')
        i+=1

def left1(event):
    global vx1,vy1
    if vx1 != 1:
        vx1 = -1
        vy1 = 0
def right1(event):
    global vx1,vy1
    if vx1 != -1:
        vx1 = 1
        vy1 = 0
def up1(event):
    global vx1,vy1
    if vy1 != 1:
        vx1 = 0
        vy1 = -1
def down1(event):
    global vx1,vy1
    if vy1 != -1:
        vx1 = 0
        vy1 = 1

# вторая змея
def left2(event):
    global vx2,vy2
    if vx2 != 1:
        vx2 = -1
        vy2 = 0
def right2(event):
    global vx2,vy2
    if vx2 != -1:
        vx2 = 1
        vy2 = 0
def up2(event):
    global vx2,vy2
    if vy2 != 1:
        vx2 = 0
        vy2 = -1
def down2(event):
    global vx2,vy2
    if vy2 != -1:
        vx2 = 0
        vy2 = 1

def create_file():
    canvas.create_rectangle(0, 0, 800, 550, fill='#2F4F4F', width=0)
    canvas.create_rectangle(12.5,12.5, 800 - 12.5, 550 - 12.5, fill='#98FB98', width = 0)


# Рисование всех элементов 
def draw_all():
    global xb, yb, text1
    
    canvas.create_text(400, 200, text = text_score, fill='red', font='Consolas 45')
    create_file()
    create_snakev1()
    create_snakev2()
    create_element(xb, yb, 'red') # Рисуем яблоко (бонус)
    canvas.create_text(200, 40, text = text1, fill='#2F4F4F', font='Consolas 30')
    canvas.create_text(600, 40, text = text2, fill='#2F4F4F', font='Consolas 30')
    canvas.create_text(400, 200, text = text_score, fill='#2F4F4F', font='Consolas 30')
    canvas.update()



# Подключение библиотек 
from tkinter import *
import random
import time


# Создания окна
root  = Tk()
# Настройка окна 
root.title('Компьютерная игра "Змейка"')
root.geometry('800x600')
root.resizable(width=False, height=False)
root['bg'] = '#2F4F4F'
try:
    root.iconbitmap('icons/python.ico')
except TclError:
    pass



# Виджиты

canvas = Canvas(root, width=800, height=550, bg='white', highlightthickness=0)
canvas.pack()

lbl_dev = Label(root, text='Разрабочик Поселенов Кирилл', bg='#2F4F4F', fg='white', font='Consolas 18')
lbl_dev.pack()


# Создание переменных для игры
tabel_xv1 =[29, 30, 31, 32]
tabel_yv1 = [10, 10, 10, 10]
tabel_xv2 =[3, 2, 1, 0]
tabel_yv2 = [10, 10, 10, 10]

# Координаты яблока и счетчик съединых яблок

#xb = 16
#yb = 5
xb = 16
yb = 10
win_score = 10
cnt_bonus1 = 0 
cnt_bonus2 = 0 
text_score=''
text1 = f'Игрок №1: {cnt_bonus1}'
text2 = f'Игрок №2: {cnt_bonus2}'
speed_snake = 0.5
# Направление движения змейки
vx1 = -1 
vy1= 0
vx2 = 1 
vy2= 0


# Обрабочтка события 

root.bind('<Left>', left1)
root.bind('<Right>', right1)
root.bind('<Up>', up1)
root.bind('<Down>', down1)

root.bind('<a>', left2)
root.bind('<d>', right2)
root.bind('<w>', up2)
root.bind('<s>', down2)

root.bind('<A>', left2)
root.bind('<D>', right2)
root.bind('<W>', up2)
root.bind('<S>', down2)



# Игровой цикл 
win = True 
while win:
    tabel_xv1 = [tabel_xv1[0] + vx1] + tabel_xv1
    tabel_yv1 = [tabel_yv1[0] + vy1] + tabel_yv1

    if tabel_xv1[0]==xb and tabel_yv1[0] == yb and tabel_xv2[0] + 1 ==xb and tabel_yv2[0] == yb:         # алгоритм работы для бонус
        tabel_xv1 = [tabel_xv1[0] + vx1] + tabel_xv1
        tabel_yv1 = [tabel_yv1[0] + vy1] + tabel_yv1
        tabel_xv2 = [tabel_xv2[0] + vx2] + tabel_xv2
        tabel_yv2 = [tabel_yv2[0] + vy2] + tabel_yv2
        xb = random.randint(1, 31)
        yb = random.randint(1, 21)
        cnt_bonus1 +=1
        cnt_bonus2 +=1
        text1 = f'Игрок №1: {cnt_bonus1}'
        text2 = f'Игрок №2: {cnt_bonus2}'
        speed_snake -= 0.003
    elif tabel_xv1[0]==xb and tabel_yv1[0] == yb and tabel_xv2[0] - 1 ==xb and tabel_yv2[0] == yb:
        tabel_xv1 = [tabel_xv1[0] + vx1] + tabel_xv1
        tabel_yv1 = [tabel_yv1[0] + vy1] + tabel_yv1
        tabel_xv2 = [tabel_xv2[0] + vx2] + tabel_xv2
        tabel_yv2 = [tabel_yv2[0] + vy2] + tabel_yv2
        xb = random.randint(1, 31)
        yb = random.randint(1, 21)
        cnt_bonus1 += 1
        cnt_bonus2 += 1
        text1 = f'Игрок №1: {cnt_bonus1}'
        text2 = f'Игрок №2: {cnt_bonus2}'
        speed_snake -= 0.003
    elif tabel_xv1[0] == xb and tabel_yv1[0] == yb and tabel_xv2[0]  == xb and tabel_yv2[0] + 1== yb:
        tabel_xv1 = [tabel_xv1[0] + vx1] + tabel_xv1
        tabel_yv1 = [tabel_yv1[0] + vy1] + tabel_yv1
        tabel_xv2 = [tabel_xv2[0] + vx2] + tabel_xv2
        tabel_yv2 = [tabel_yv2[0] + vy2] + tabel_yv2
        xb = random.randint(1, 31)
        yb = random.randint(1, 21)
        cnt_bonus1 += 1
        cnt_bonus2 += 1
        text1 = f'Игрок №1: {cnt_bonus1}'
        text2 = f'Игрок №2: {cnt_bonus2}'
        speed_snake -= 0.003
    elif tabel_xv1[0] == xb and tabel_yv1[0] == yb and tabel_xv2[0] == xb and tabel_yv2[0] - 1 == yb:
        tabel_xv1 = [tabel_xv1[0] + vx1] + tabel_xv1
        tabel_yv1 = [tabel_yv1[0] + vy1] + tabel_yv1
        tabel_xv2 = [tabel_xv2[0] + vx2] + tabel_xv2
        tabel_yv2 = [tabel_yv2[0] + vy2] + tabel_yv2
        xb = random.randint(1, 31)
        yb = random.randint(1, 21)
        cnt_bonus1 += 1
        cnt_bonus2 += 1
        text1 = f'Игрок №1: {cnt_bonus1}'
        text2 = f'Игрок №2: {cnt_bonus2}'
        speed_snake -= 0.003


    if tabel_xv1[0] == 0 and vx1 ==-1: tabel_xv1[0]=31
    elif tabel_xv1[0] == 32 and vx1 ==1: tabel_xv1[0]=1
    elif tabel_yv1[0] == 0 and vy1 ==-1: tabel_yv1[0]=21
    elif tabel_yv1[0] == 22 and vy1 ==1: tabel_yv1[0]=1
    if tabel_xv1[0]==xb and tabel_yv1[0] == yb:         # алгоритм работы для бонус
        xb = random.randint(1, 31)
        yb = random.randint(1, 21)
        cnt_bonus1 +=1
        speed_snake -= 0.003
        text1 = f'Игрок №1: {cnt_bonus1}'

        if cnt_bonus1 == win_score:
            win = False
            text1 = f''
            text2 = f''
            text_score = f'Игрок номер №1, ты выиграл!!\n      Твоей результат: {cnt_bonus1}'
    else:    
        tabel_xv1.pop(-1) # Удаление последнего элемента списка
        tabel_yv1.pop(-1)

    i = 1
    while i < len(tabel_xv1):
        if tabel_xv1[0] == tabel_xv1[i] and tabel_yv1[0]== tabel_yv1[i]:
            win =False
            text1 = f''
            text2 = f''
            text_score = f'Игрок номер №1, ты проиграл!!'
        i += 1

    # Вторая змейка 
    tabel_xv2 = [tabel_xv2[0] + vx2] + tabel_xv2
    tabel_yv2 = [tabel_yv2[0] + vy2] + tabel_yv2


    if tabel_xv2[0] == 0 and vx2 ==-1: tabel_xv2[0]=31
    elif tabel_xv2[0] == 32 and vx2 ==1: tabel_xv2[0]=1
    elif tabel_yv2[0] == 0 and vy2 ==-1: tabel_yv2[0]=21
    elif tabel_yv2[0] == 22 and vy2 ==1: tabel_yv2[0]=1
    if tabel_xv2[0]==xb and tabel_yv2[0] == yb:         # алгоритм работы для бонус
        xb = random.randint(1, 31)
        yb = random.randint(1, 21)
        cnt_bonus2 +=1
        text2 = f'Игрок №2: {cnt_bonus1}'
        speed_snake -= 0.003
        if cnt_bonus2 == win_score:
            win = False
            text1 = f''
            text2 = f''
            text_score = f'Игрок номер №2, ты выиграл!!\n Твоей результат: {cnt_bonus2}'
    else:    
        tabel_xv2.pop(-1) # Удаление последнего элемента списка
        tabel_yv2.pop(-1)

    i = 1
    while i < len(tabel_xv2):
        if tabel_xv2[0] == tabel_xv2[i] and tabel_yv2[0]== tabel_yv2[i]:
            win =False
            text1 = ''
            text2 = ''
            text_score = f'Игрок номер №2, ты проиграл!!'
        i += 1

    draw_all()
    time.sleep(speed_snake) # Задержка (скорость змейки)
    canvas.delete('all') # очищение холста (удаление элементов виджита canvas)

draw_all()



# Запуск приложения
root.mainloop()