"""

Вычисление сложности алгоритмов (О-нотация): Это способ описать, как время выполнения или объем памяти алгоритма растут с увеличением объема входных данных (n).
O(1) – Константная: Время выполнения не зависит от n (например, доступ к элементу списка по индексу).
O(log n) – Логарифмическая: Время растет медленно (например, бинарный поиск).
O(n) – Линейная: Время растет пропорционально n (например, поиск в неотсортированном списке).
O(n log n) – Линейно-логарифмическая: Характерна для эффективных алгоритмов сортировки (например, Timsort в Python).
O(n²) – Квадратичная: Время растет пропорционально квадрату n (например, два вложенных цикла, пузырьковая сортировка).
O(2^n) – Экспоненциальная: Время растет очень быстро, такие алгоритмы практически неприменимы для больших n.

"""
"""
import time
import  random
# Генерация случайного списка
data = random.sample(range(1,200000), 100000) # 1000 уникальных чисел [2,4,7,1,....5]
data_copy = data.copy()

# O(n^2) - Сортировка пузырьком (неоптимальная)
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# O(n log n) - Встроенная сортировка Python (оптимальная)
def optimal_sort(lst):
    return sorted(lst)

# Замер времени для пузырьковой сортировки
start = time.time()
bubble_sorted = bubble_sort(data)
end = time.time()
print(f'Сортировка пузырьком: {end - start:.9f} секунд')

# Замер времени для пузырьковой сортировки
start = time.time()
optimal_sorted = optimal_sort(data)
end = time.time()
print(f'Оптимальная сортировка: {end - start:.9f} секунд')

# Проверка, что оба алгоритма дают одинаковый результат
print('Корректность сортировок: ', bubble_sorted==optimal_sorted)
"""
from tkinter import *
import random
"""
def elements():
    canvas.create_line(10, 10, 90, 90, fill='red', width=3)
    canvas.create_rectangle(110, 10, 190, 90, fill='blue', width=3,
                            outline='blue')  # прямоугольник, fill - цвет тела, width- толщина линии, outline - цвет рамки
    canvas.create_oval(210, 10, 290, 90, fill='yellow', width=0)  # Рисование окружности (без рамки)
    canvas.create_polygon(310, 90, 350, 10, 390, 90, fill='green', width=5, outline='black')  # Фигура полигон
    canvas.create_line(410, 50, 450, 10, 490, 50, 450, 90, 410, 50, fill='brown', width=3)  # Ромб с помощью линии
    canvas.create_text(250, 200, text='hello world!', fill='blue', font='Consolas 30')  # Текст конвас


    
# tkinter - canvas, змейка
from tkinter import *

root = Tk()
root.title("Виджет Canvas")
root.geometry("600x600")  # Размеры окна(ширина, высота)
root["bg"] = "#FFEBCD"  # Цвет фона
root.resizable(width=True, height=True)  # Возможность изменять размеры окна
try:
    root.iconbitmap("icons/icon.ico")  # Иконка
except TclError:
    pass

# виджет Canvas (холст для рисования)
canvas = Canvas(root, width=600, height=600, bg="white")
# упаковщик
canvas.pack()
elements()
root.mainloop()

"""
"""
def canvas_home():

    canvas.create_rectangle(3, 597, 597, 347, fill='green', width=5) # Трава
    canvas.create_oval(25, 25, 120, 120, fill='yellow', width=0) # Солнце
    canvas.create_rectangle(175, 175, 450, 450, fill='orange', width=5)  # Стены дома
    canvas.create_polygon(173,173,305,50,450,173, fill='red', width=5) # Крыша
    canvas.create_line(175,175,305,50,450,175, fill='black', width=5) # Крыша
    canvas.create_rectangle(250, 250, 380, 380, fill='blue', width=5, outline='white')



root = Tk()
root.title("Виджет Canvas")
root.geometry("600x600")  # Размеры окна(ширина, высота)
root["bg"] = "#FFEBCD"  # Цвет фона
root.resizable(width=True, height=True)  # Возможность изменять размеры окна
try:
    root.iconbitmap("icons/icon.ico")  # Иконка
except TclError:
    pass

# виджет Canvas (холст для рисования)
canvas = Canvas(root, width=600, height=600, bg="lightblue")
# упаковщик
canvas.pack()
canvas_home()
root.mainloop()
"""
"""
def draw_rec(x,y,r):
    canvas.create_rectangle(x,y,(x+r),(y+r), fill='white', width=3, outline='orange')

root = Tk()
root.title("Виджет Canvas")
root.geometry("600x600")  # Размеры окна(ширина, высота)
root["bg"] = "#FFEBCD"  # Цвет фона
root.resizable(width=True, height=True)  # Возможность изменять размеры окна
try:
    root.iconbitmap("icons/icon.ico")  # Иконка
except TclError:
    pass

# виджет Canvas (холст для рисования)
canvas = Canvas(root, width=600, height=600, bg="lightblue")
# упаковщик
canvas.pack()
draw_rec(200,100,150)
root.mainloop()
"""

def stars():
    for i in range(100):
        x = random.randrange(1,600)
        r = random.randint(1, 5)
        y = random.randrange(1, 600)
        canvas.create_oval(x+r, y+r, x, y, fill='yellow', width=0)




root = Tk()
root.title("Виджет Canvas")
root.geometry("600x600")  # Размеры окна(ширина, высота)
root["bg"] = "#FFEBCD"  # Цвет фона
root.resizable(width=True, height=True)  # Возможность изменять размеры окна
try:
    root.iconbitmap("icons/icon.ico")  # Иконка
except TclError:
    pass

# виджет Canvas (холст для рисования)
canvas = Canvas(root, width=600, height=600, bg="blue")
# упаковщик
canvas.pack()
stars()
root.mainloop()