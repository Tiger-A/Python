# a = int(input('Введите а: ')) # 11
# b = int(input('Введите b: ')) # 15
# print(f'S={1/2*a*b}')






# r = int(input('Введите R: ')) 
# g = int(input('Введите G: ')) 
# n = int(input('Введите n: '))
# print(f'Sum='(r+g)*n)




# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90


# a = [10, 2, 34, 4, 5]
# max = a[0]
# for i in a:
#     if i > max:
#         max = i
# print(max)

# list = [1, 4, 8, 7, 5]
# print(reduce(max, list))



# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# a = int(input('Введите число: '))

# for i in range(-a, a+ 1):
#     print(i, end=" ")





# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# n = float(input('Введите число: '))
# print(int(n//1))



# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

n = int(input('Введите число: '))
if n%5==0 and (n%10==0 or n%15==0) and n%30!=0:
    print(True)
else:
    print(False)





if 5<int(input("Введите номер дня недели:"))<8: #если введённая переменная больше 5 и при этом меньше 8, то
        print("да") # да, является
else: # иначе
        print("нет")  # нет, не является


digit = int(input('Введите число от 1 до 7: '))
if digit > 7 or digit < 1:
    print('Число выходит за рамки диапазона! Попробуйте еще раз')
elif 1 <= digit <= 5:
    print(digit, 'Будний день!')
else:
    print(digit, 'Выходной день!')



n = 0

while n < 1 or n > 4:
	n = int(input(‘Input N:’))

if n == 1:
	print(‘X > 0 and Y > 0’)
elif n == 2:
	print(‘X < 0 and Y > 0’)
elif n == 3:
	print(‘X < 0 and Y < 0’)
elif n == 4:
	print(‘X > 0 and Y < 0’)


day = input('Введите номер дня недели = ')

while day not in ('1', '2', '3', '4', '5', '6', '7'):
    print('Такого дня недели не существует')
    day = input('Введите номер дня недели = ')
day = int(day)

if 0<day<6:
    print(day, 'нет', sep=' -> ')
else: 
    print(day, 'да', sep=' -> ')


x = int(input('Введите число X: '))
y = int(input('Введите число Y: '))
z = int(input('Введите число Z: '))
if not (x or y or z) == (not x and not y and not z):
    print(True)
else:
    print(False)


Можно ещё проще
#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input(‘Input X:’))
y = int(input(‘Input Y:’))
z = int(input(‘Input Z:’))

print((~(x | y | z) == ~x & ~y & ~z))


x = int(input('Введите координаты точки по X: '))
y = int(input('Введите координаты точки по Y: '))

\\ while [ is not digit]

if x != 0 and y != 0:
    if x > 0 and y > 0:
        print('1 четверть')
    elif x < 0 and y > 0:
        print('2 четверть')
    elif x < 0 and y < 0:
        print('3 четверть')
    else:
        print('4 четверть')
else:
    print('Введите координаты не равные 0!!!')



x = int(input('Введите коорддинату Х = '))
y = int(input('Введите коорддинату Y = '))
Тут нужна проверка от дурака чере while

if x > 0:
    if y > 0:
        print(' -> 1')
    else:
        print(' -> 4')        
elif x < 0: 
    if y > 0:
        print(' -> 2')
    else:
        print(' -> 3')


from math import sqrt

x_a = int(input('Введите X для точки А: '))
y_a = int(input('Введите Y для точки А: '))
x_b = int(input('Введите X для точки B: '))
y_b = int(input('Введите Y для точки B: '))

print('Расстояние между двумя точками: = ',
      round(sqrt((x_b - x_a)**2 + (y_b - y_a)**2), 2))




      AX = int(input('точка А(X,Y) Введите  координату точки  X =  '))
AY = int(input('точка А(X,Y) Введите  координату точки  Y =  '))
BX = int(input('точка B(X,Y) Введите  координату точки  X =  '))
BY = int(input('точка B(X,Y) Введите  координату точки  Y =  '))
print(f' расстояние между A({AX},{AY}) B({BX},{BY}) равно {(((BX-AX)**2+(BY-AY)**2)**0.5):5.2f}')






1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
    *Пример:*
    
    - Для N = 5: 1, -3, 9, -27, 81
2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
    *Пример:*
    
    - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.


import random

n =  int(input("Введите произвольное целое число: "))
for i in range(n):
    print(random.randint(-100,100))



    pythontutor.com/vizualize.html



dict_numbers = {}   # Создание пустого словаря
n = int(input('Введите число: '))
for i in range(1, n+1): 
  dict_numbers[i] = i*3 + 1
print(dict_numbers)



number = input("Введите число N: ")
result = []
for i in range(1, int(number)+1):
  result.append([i, 3*i + 1])
print(dict(result))


number = input("Введите число N: ")
result = []
for i in range(1, int(number)+1):    
    elem = [i, 3*i + 1]
    result.append(elem)
print(result)
print(dict(result))

number = input("Введите число N: ")
result = dict()
for i in range(1, int(number)+1):    
    result[i] = 3*i + 1
print(result)




Полезные ссылочки:
https://staminaon.com/ru/ - обучение слепой печати
https://klavogonki.ru/ - закрепление навыка на текстах в игровой форме
https://stepik.org/course/58852/syllabus - для тех кто хочет дополнительного материала 1
https://stepik.org/course/68343/syllabus  - для тех кто хочет дополнительного материала 2
https://skillbox.ru/media/base/goryachie_klavishi_v_vscode/ -  горячие клавиши VSC - очень полезная штука)
https://pythontutor.com/ - визуализатор пайтон, очень удобный инструмент

https://docs.python.org/3/library/stdtypes.html?highlight=count#str.count - официальная документация python (англ. яз.) - здесь можно найти всё



str1 = input('Введите первую строку для проверки:')
str2 = input('Введите вторую строку для поиска в первой строке:')

print(f'Вторая строка входит в первую {str1.count(str2)} раз(а).')


