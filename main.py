# Case-study #6
# Developers:   Grishaev G. (30%),
#               Abrarova V. (40%),
#               Zlobinskaya L. (60%)

from turtle import *


def square(size):
    '''Function draws square'''
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)


def fr(n, size):
    '''Function draws square fractal'''
    while n >= 0:
        square(size)
        penup()
        forward(size * 0.15)
        right(15)
        pendown()
        size = size * 0.8
        n = n - 1


def tree(n, size):
    '''function draws tree'''
    if n == 0:
        forward(size)
        left(40)
        forward(size * 0.6)
        right(180)
        forward(size * 0.6)
        right(180)
        right(80)
        forward(size * 0.6)
        right(180)
        forward(size * 0.6)
        left(180)
        right(140)
        forward(size)
        left(180)

    else:
        forward(size)
        left(40)
        forward(size * 0.3)
        tree(n - 1, size * 0.3)
        right(180)
        forward(size * 0.3)
        right(180)
        right(80)
        forward(size * 0.3)
        tree(n - 1, size * 0.3)
        right(180)
        forward(size * 0.3)
        left(180)
        right(140)
        forward(size)
        left(180)


def koch(order, size):
    '''function takes part in koch stuff'''
    if order == 0:
        forward(size)
    else:
        koch(order - 1, size / 3)
        left(60)
        koch(order - 1, size / 3)
        right(120)
        koch(order - 1, size / 3)
        left(60)
        koch(order - 1, size / 3)


def snow():
    '''drwas snowlake'''
    up()
    goto(-100, 0)
    down()
    n = int(input('Введите глубину рекурсии: '))
    s = float(input('Введите длинну: '))
    koch(n, s)
    right(120)
    koch(n, s)
    right(120)
    koch(n, s)
    right(120)


def krivaya():
    '''Draws curva of Koch'''
    n = int(input('Введите глубину рекурсии: '))
    s = float(input('Введите длинну: '))
    up()
    goto(-100, 0)
    down()
    koch(n, s)


def mainKoch():
    up()
    goto(-100, 0)
    down()
    n = int(input('Введите глубину рекурсии: '))
    s = float(input('Введите длинну: '))
    koch(n, s)
    right(120)
    koch(n, s)
    right(120)
    koch(n, s)
    right(120)


def Minkovsiy(n, size):
    '''Draws Minkovskiy'''
    if n == 0:
        forward(size * 4)
    else:
        Minkovsiy(n - 1, size / 4)
        left(90)
        Minkovsiy(n - 1, size / 4)
        right(90)
        Minkovsiy(n - 1, size / 4)
        right(90)
        Minkovsiy(n - 1, size / 4)
        Minkovsiy(n - 1, size / 4)
        left(90)
        Minkovsiy(n - 1, size / 4)
        left(90)
        Minkovsiy(n - 1, size / 4)
        right(90)
        Minkovsiy(n - 1, size / 4)


def Frozen_1(n, size):
    '''Draws Frozen 1'''
    if n == 0:
        forward(size)
    else:
        Frozen_1(n - 1, size / 2)
        left(90)
        Frozen_1(n - 1, size / 4)
        right(180)
        Frozen_1(n - 1, size / 4)
        left(90)
        Frozen_1(n - 1, size / 2)


def Frozen_2(n, size):
    '''Draws frozen 2'''
    if n == 0:
        forward(size)
    else:
        Frozen_2(n - 1, size / 2)
        left(120)
        Frozen_2(n - 1, size / 4)
        left(180)
        Frozen_2(n - 1, size / 4)
        left(120)
        Frozen_2(n - 1, size / 4)
        left(180)
        Frozen_2(n - 1, size / 4)
        left(120)
        Frozen_2(n - 1, size / 2)


def dragon(order, size):
    '''Draws dragon'''
    speed(6)
    if order == 0:
        forward(size)
    else:
        left(45)
        dragon(order - 1, size / 2 ** 0.5)
        right(90)
        up()
        forward(size / 2 ** 0.5)
        down()
        left(180)
        dragon(order - 1, size / 2 ** 0.5)
        left(180)
        up()
        forward(size / 2 ** 0.5)
        down()
        left(45)


def Levi(order, size):
    '''Draws Levis fractal'''
    speed(6)

    if order == 1:

        left(45)
        forward(size / 2 ** 0.5)
        right(90)
        forward(size / 2 ** 0.5)

    else:
        left(45)

        Levi(order - 1, size / 2 ** 0.5)
        right(45)
        Levi(order - 1, size / 2 ** 0.5)
        left(45)


def check():
    '''Checks number from menu'''
    num = int(input('Выберите пункт меню:'))
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    c = list.count(num)
    while c <= 0:
        num = int(input('Выберите пункт меню:'))
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        c = list.count(num)

    choose(num)


def branch(n, size):
    '''Draws branch'''
    if n == 0:
        left(180)
        return

    x = size / (n + 1)
    for i in range(n):
        forward(x)
        left(45)
        branch(n - i - 1, 0.5 * x * (n - i - 1))
        left(90)
        branch(n - i - 1, 0.5 * x * (n - i - 1))
        right(135)

    forward(x)
    left(180)
    forward(size)


def My_frctal(n, size):
    '''Draws own created one'''
    if n == 0:
        forward(size)
    else:
        forward(size / 4)
        left(120)
        My_frctal(n - 1, size / 4)
        left(180)
        forward(size / 4)
        My_frctal(n - 1, size / 4)
        left(180)
        forward(size / 4)
        right(60)
        My_frctal(n - 1, size / 4)
        left(180)
        forward(size / 4)
        My_frctal(n - 1, size / 4)
        left(180)
        forward(size / 4)
        right(60)  # first snow
        forward(size / 4)
        left(90)
        My_frctal(n - 1, size / 4)
        left(180)
        forward(size / 4)
        My_frctal(n - 1, size / 4)
        left(180)
        forward(size / 4)
        right(90)
        forward(size / 4)  # sec
        left(120)
        My_frctal(n - 1, size / 4)
        left(180)
        forward(size / 4)
        My_frctal(n - 1, size / 4)
        left(180)
        forward(size / 4)
        right(60)
        My_frctal(n - 1, size / 4)
        left(180)
        forward(size / 4)
        My_frctal(n - 1, size / 4)
        left(180)
        forward(size / 4)
        right(60)
        forward(size / 4)


def choose(num):
    '''Calls recursion that we need'''
    n = int(input('Введите глубину рекурсии: '))
    s = float(input('Введите длинну: '))
    if num == 1:
        fr(n, s)
    if num == 2:
        tree(n, s)
    if num == 3:
        branch(n, s)
    if num == 4:
        krivaya()
    if num == 5:
        snow()
    if num == 6:
        Minkovsiy(n, s)
    if num == 7:
        Frozen_1(n, s)
    if num == 8:
        Frozen_2(n, s)
    if num == 9:
        Levi(n, s)
    if num == 10:
        dragon(n, s)
    if num == 11:
        My_frctal(n, s)


print(
    'Выберите фрактал:\n1. Квадрат\n2. Дерево\n3. Ветка\n4. Кривая Коха\n5. Снежинка Коха\n6. Кривая Минковского\n7. Ледяной фрактал 1\n8. Ледяной фрактал 2\n9. Кривая Леви\n10. Фрактал Дракон Хартера-Хейтуэя\n11. Придуманный фрактал')
check()