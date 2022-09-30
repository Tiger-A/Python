# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day_week = input('Введите номер дня недели = ')
# while day_week not in ('1', '2', '3', '4', '5', '6', '7'):
#     print('Такого дня недели не существует')
#     day_week = input('Введите номер дня недели = ')
# day_week = int(day_week)                                                   
# if day_week <= 5:
#     print( "Это рабочий день")
# else: 
#     print("Это выходной")    


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.







# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# print("Input X - ")
# while True:
#     try:
#         x = float(input())
#     except ValueError:
#         print("This is not number, try again: ")
#     else:
#         break
# print("Input Y - ")
# while True:
#     try:
#         y = float(input())
#     except ValueError:
#         print("This is not number, try again: ")
#     else:
#         break
# if x > 0:
#     if y > 0:
#         print("Point in I square")
#     else:
#         print(("Point in II square"))     
# else:
#     if y > 0:
#         print("Point in III square")
#     else:
#         print(("Point in IV square"))


# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# quarter = input('Input quarter = ')
# while quarter not in ('1', '2', '3', '4'):
#     print('Input wrong, try again')
#     quarter = input('Input quarter from 1 to 4  ')
# quarter = int(quarter)                                                   
# if quarter == 1:
#      print('X may be from 0 to 999..., Y may be from 0 to 999...')
# elif quarter == 2:    
#     print('X may be from 0 to 999..., Y may be from 0 to -999...')
# elif quarter == 3:    
#     print('X may be from 0 to -999..., Y may be from 0 to -999...')
# else:
#     print('X may be from 0 to -999..., Y may be from 0 to 999...')


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


from math import sqrt
ax = float(input('Input X point A - ')) 
ay = float(input('Input Y point A - '))
bx = float(input('Input X point B - '))
by = float(input('Input Y point B - '))
print('The distance betweуn points A and B -', round(sqrt((bx - ax)**2 + (by - ay)**2), 2))


# def input_float() 
# print("Input number ")
# while True:
#     try:
#         x = float(input())
#     except ValueError:
#         print("This is not number, try again: ")
#     else:
#         return x

