# # a = int(input('Введите а: ')) # 11
# # b = int(input('Введите b: ')) # 15
# # print(f'S={1/2*a*b}')






# # r = int(input('Введите R: ')) 
# # g = int(input('Введите G: ')) 
# # n = int(input('Введите n: '))
# # print(f'Sum='(r+g)*n)




# # 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# # Примеры:

# # - 1, 4, 8, 7, 5 -> 8
# # - 78, 55, 36, 90, 2 -> 90


# # a = [10, 2, 34, 4, 5]
# # max = a[0]
# # for i in a:
# #     if i > max:
# #         max = i
# # print(max)

# # list = [1, 4, 8, 7, 5]
# # print(reduce(max, list))



# # Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# # a = int(input('Введите число: '))

# # for i in range(-a, a+ 1):
# #     print(i, end=" ")





# # Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# # Примеры:*

# # - 6,78 -> 7
# # - 5 -> нет
# # - 0,34 -> 3

# # n = float(input('Введите число: '))
# # print(int(n//1))



# # Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# from secrets import choice


# n = int(input('Введите число: '))
# if n%5==0 and (n%10==0 or n%15==0) and n%30!=0:
#     print(True)
# else:
#     print(False)





# if 5<int(input("Введите номер дня недели:"))<8: #если введённая переменная больше 5 и при этом меньше 8, то
#         print("да") # да, является
# else: # иначе
#         print("нет")  # нет, не является


# digit = int(input('Введите число от 1 до 7: '))
# if digit > 7 or digit < 1:
#     print('Число выходит за рамки диапазона! Попробуйте еще раз')
# elif 1 <= digit <= 5:
#     print(digit, 'Будний день!')
# else:
#     print(digit, 'Выходной день!')



# n = 0

# while n < 1 or n > 4:
# 	n = int(input(‘Input N:’))

# if n == 1:
# 	print(‘X > 0 and Y > 0’)
# elif n == 2:
# 	print(‘X < 0 and Y > 0’)
# elif n == 3:
# 	print(‘X < 0 and Y < 0’)
# elif n == 4:
# 	print(‘X > 0 and Y < 0’)


# day = input('Введите номер дня недели = ')

# while day not in ('1', '2', '3', '4', '5', '6', '7'):
#     print('Такого дня недели не существует')
#     day = input('Введите номер дня недели = ')
# day = int(day)

# if 0<day<6:
#     print(day, 'нет', sep=' -> ')
# else: 
#     print(day, 'да', sep=' -> ')


# x = int(input('Введите число X: '))
# y = int(input('Введите число Y: '))
# z = int(input('Введите число Z: '))
# if not (x or y or z) == (not x and not y and not z):
#     print(True)
# else:
#     print(False)


# Можно ещё проще
# #Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# x = int(input(‘Input X:’))
# y = int(input(‘Input Y:’))
# z = int(input(‘Input Z:’))

# print((~(x | y | z) == ~x & ~y & ~z))


# x = int(input('Введите координаты точки по X: '))
# y = int(input('Введите координаты точки по Y: '))

# \\ while [ is not digit]

# if x != 0 and y != 0:
#     if x > 0 and y > 0:
#         print('1 четверть')
#     elif x < 0 and y > 0:
#         print('2 четверть')
#     elif x < 0 and y < 0:
#         print('3 четверть')
#     else:
#         print('4 четверть')
# else:
#     print('Введите координаты не равные 0!!!')



# x = int(input('Введите коорддинату Х = '))
# y = int(input('Введите коорддинату Y = '))
# Тут нужна проверка от дурака чере while

# if x > 0:
#     if y > 0:
#         print(' -> 1')
#     else:
#         print(' -> 4')        
# elif x < 0: 
#     if y > 0:
#         print(' -> 2')
#     else:
#         print(' -> 3')


# from math import sqrt

# x_a = int(input('Введите X для точки А: '))
# y_a = int(input('Введите Y для точки А: '))
# x_b = int(input('Введите X для точки B: '))
# y_b = int(input('Введите Y для точки B: '))

# print('Расстояние между двумя точками: = ',
#       round(sqrt((x_b - x_a)**2 + (y_b - y_a)**2), 2))




#       AX = int(input('точка А(X,Y) Введите  координату точки  X =  '))
# AY = int(input('точка А(X,Y) Введите  координату точки  Y =  '))
# BX = int(input('точка B(X,Y) Введите  координату точки  X =  '))
# BY = int(input('точка B(X,Y) Введите  координату точки  Y =  '))
# print(f' расстояние между A({AX},{AY}) B({BX},{BY}) равно {(((BX-AX)**2+(BY-AY)**2)**0.5):5.2f}')






# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81
# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.


# import random

# n =  int(input("Введите произвольное целое число: "))
# for i in range(n):
#     print(random.randint(-100,100))



#     pythontutor.com/vizualize.html



# dict_numbers = {}   # Создание пустого словаря
# n = int(input('Введите число: '))
# for i in range(1, n+1): 
#   dict_numbers[i] = i*3 + 1
# print(dict_numbers)



# number = input("Введите число N: ")
# result = []
# for i in range(1, int(number)+1):
#   result.append([i, 3*i + 1])
# print(dict(result))


# number = input("Введите число N: ")
# result = []
# for i in range(1, int(number)+1):    
#     elem = [i, 3*i + 1]
#     result.append(elem)
# print(result)
# print(dict(result))

# number = input("Введите число N: ")
# result = dict()
# for i in range(1, int(number)+1):    
#     result[i] = 3*i + 1
# print(result)




# Полезные ссылочки:
# https://staminaon.com/ru/ - обучение слепой печати
# https://klavogonki.ru/ - закрепление навыка на текстах в игровой форме
# https://stepik.org/course/58852/syllabus - для тех кто хочет дополнительного материала 1
# https://stepik.org/course/68343/syllabus  - для тех кто хочет дополнительного материала 2
# https://skillbox.ru/media/base/goryachie_klavishi_v_vscode/ -  горячие клавиши VSC - очень полезная штука)
# https://pythontutor.com/ - визуализатор пайтон, очень удобный инструмент

# https://docs.python.org/3/library/stdtypes.html?highlight=count#str.count - официальная документация python (англ. яз.) - здесь можно найти всё



# str1 = input('Введите первую строку для проверки:')
# str2 = input('Введите вторую строку для поиска в первой строке:')

# print(f'Вторая строка входит в первую {str1.count(str2)} раз(а).')





# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    
#     *Пример:*
    
#     - 6782 -> 23
#     - 0,56 -> 11


# x = input('Введите число ')

# def summa(x):                            
#     if float(x) < 0:                          
#         x = float(x) * (-1)
#             number = 0

#     for i in str(x):
#         if i != '.':
#             number += int(i)
#     return number
   
# print(f'Сумма чисел равна {summa(x)}')









# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    
#     *Пример:*
    
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)



# # N = int(input('Введите число '))

# # f = 1
# # for i in range(N):
# #     i = i + 1 f = i * f
    
# print(f, end=" ")
# N = int(input('Введите число '))
# f = 1
# for i in range(N):
#   i = i + 1
#   f = i * f
# print(f, end=" ")




# можно вообще вот так
# for i in range(2, n+1):
#     lst.append(lst[i-2] * i)



# N = int(input("Ввведите число: ")) # создаём переменную N и присваем ей целочисленные значения в соответствии с вводимым через клавиатуру пользователя числом. 
# def factorial(N): # задаём функцию факториала переменной N
#     a = 1 # создаём переменную a и присваем ей значение 1, исходя из условий задачи
#     numbers = [] # cоздаём числовую переменную, где полученные значения будут отображаться в квадратных скобках
#     for i in range (1, N+1): # пока переменная i находится в диапозоне от 1 до N+1, то
#      a = a * i # создаём переменную а и присваем ей произведение предыдущей переменной а * на переменную i
#     numbers.append(a) # к числовой переменной добавляем переменную а
#     return numbers # делаем повтор числовой переменной
# print(f'набор произведений чисел от 1 до N {factorial(N)}') # Выводим результат решения задачи








# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
    

# # Задайте список из n чисел последовательности (1 + 1/n)**n
# # и выведите на экран их сумму.



#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}    пример с ошибкой !!!!

# n = int(input('Введите количество чисел в списке '))

# def numbers(n):
#     summ = 0
#     for i in range(n):
#         a = int(input(f'Введи число {i + 1}: '))
#         a = (1+1/a)**a
#         summ = a + summ
#         i += 1
#     return summ

# print('Сумма чисел равна',round((numbers(n)), 2))






# def input_int(msg):
#     while True:
#         try:
#             result = int(input(msg))
#         except ValueError:
#             print("Ошибка, повторите ввод: ")
#         else:
#             return result


# def generate_list(n):
#     result = []
#     for i in range(1, n+1):
#         result.append(round((1 + 1/i)**i))
#     return result


# n = input_int("Введите целое число: ")
# number_list = generate_list(n)


# print(f"Для n = {n}: {number_list} -> {sum(number_list)}")

# нужно было сделать  ключ : значение

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.



# from random import randint

# with open('17_Mult_task.txt', 'w') as data:
#     data.write('0\n')
#     data.write('1\n')
#     data.write('5\n')
#     data.write('8\n')
#     data.write('10\n')

# def get_numbers(n):
#     return [randint(-n/2, n) for i in range(-n, n + 1)]

# def get_data_from_file(path):
#     data = open(path, 'r')
#     dlist = [int(line.strip()) for line in data]
#     data.close()
#     return dlist

# def get_mult(numbers, datalist):
#     mult = 1
#     for i in datalist:
#         mult *= numbers[i]
#     return mult

# path = '17_Mult_task.txt'
# n = 10 
# datalist = get_data_from_file(path)
# numbers = get_numbers(n)

# print(numbers)
# print(datalist)
# print(get_mult(numbers, datalist))






# from random import Random, randint

# N = int(input('Введите число '))
# numbers = []
# for i in range(N):
#     numbers.append(randint(-N,N+1))
# print(numbers)

# def smes(numbers):
#     list = numbers[:]
#     numbers_length = len(list)
#     for i in range(numbers_length):
#         index = randint(0, numbers_length - 1)
#         temp = list[i]
#         list[i] = list[index]
#         list[index] = temp
#     return list
# print(smes(numbers))


# надо  было сделать словарем

# number = int(input('Ведите число: '))
# list = []
# for i in range(1, number+1):
#     part = [i,round((1+1/i)**i)]
#     list.append(part)
# my_dict = dict(list)
# my_sum = sum(my_dict.values())
# print(f'Сумма последовательсности из {number} элементов {my_dict} равна: {my_sum}')


# def is_int(number):
#     return number.isdigit()

# number = None

# while not is_int(str(number)):
#     number = input("Input number:")

# number = int(number)

# result = dict()
# for i in range(1, number+1):
#     result[i] = round((1 + 1 / i) ** i)

# my_sum = 0
# for i in result: 
#     my_sum += result[i]

# print(result, '->', my_sum)







# 5. Реализуйте алгоритм перемешивания списка



# # алгоритм перетасовки Фишера–Йейтса
# lst = [1, 2, 3, 4, 5]
# print ('Исходный список :', lst)

# for i in range(len(lst)-1, 0, -1):
#     j = random.randint(0, i + 1)   # Берем случайный индекс  от 0 до i
#     lst[i], lst[j] = lst[j], lst[i] # Меняем arr[i] с элементом случайеого индекса
     
# print ('перемешаный список : ', lst)


# Можно использовать метод choice
# random import choice





# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

# from time import time
# print(f'Случайное число от 0 до 999 = {int(time() % 1 * 1000)}')

# from time import time
# my_time = time()
# my_time %= 1
# print(my_time)
# # print(int((my_time % 1)*100))





# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# my_list = ["123","234", "12333", "567", "123"]
# number = "123"
# for i in my_list:
#     if number in i: 
#         print(i)
#         print(my_list.index(i))


# my_list = ["123","234", "12333", "567", "123"]
# number = "123"
# nul = 0
# for elem in my_list:
#     if number in elem: 
#         print(elem)
#         print(my_list.index(elem, nul))
#         nul = my_list.index(elem, nul) + 1
        
# my_list = ["123","234", "12333", "567", "123"]
# number = "123"

# for i, elem in enumerate(my_list):
#     if number in elem: 
#         print(elem)
#         print(i)





# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


# my_list = ["123","234", "12333", "567", "123"]
# number = "123"
# n = 0
# for i, elem in enumerate(my_list):
#     if number == elem and n > 0:
#         n += n
#         print(n)
#         print(i)






#         my_list = ["123","234", "12333", "567", "123"]
# number = my_list[0]
# for i, elem in enumerate(my_list):
#     if number == elem and i != 0:
#         print(elem)
#         print(i)

# my_list = ["123","234", "12333", "567", "123"]
# number = my_list[0]
# for i in range(1, len(my_list)):
#     if number == my_list[i]:
#         print(i)

# my_list = ["123","234", "12333", "567", "123"]
# number = my_list[0]
# print(my_list.index(number, 1))



# my_list = ["123","234", "12333", "567", "123"]
# number = my_list[0]
# print(my_list.index(number, 1))


# Семинар4


def is_int(number):
    return number.isdigit()

number = None

while not is_int(str(number)):
    number = input(«Input number:»)
функция для ввода целого числа


def get_digit(text):
    result = text
    if result[0] == ‘-‘:
        result = result[1:]
    
    return result.replace(‘.’, ‘’, 1)

def is_float(number):   
    return get_digit(number).isdigit()


import random
num=int(input('Введите число '))
num_list=[]
for i in range(num):
   num_list.append(random.randint(1,10))
print(num_list)
print(sum(num_list[::2]))


new_lst = [round(i%1,2) for i in lst if i%1 != 0]

# 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.


my_list = [1.1, 1.2, 3.1, 5, 10.01] 
new_list = [(num % 1) for num in my_list if isinstance(num, float)]   
#  isinstance(num, float)] = #type(num) == float
print(new_list)
max_num = max(new_list)
min_num = min(new_list)
print(max_num - min_num)

new_list = [(num)%1 for num in my_list if isinstance (num, float)]   # if isinstance (num, float)]  если num вещественное

в двоичное

numb = int(input('Введите целое число: ')) 
x = ''
while numb != 0:
    x += str(numb % 2)
    numb = numb // 2
print(f'Двоичное представление числа: {x}')


вот с бином чистый 
numb = int(input('Введите целое число: ')) 
print(bin(numb))

print(f'{bin(n)[2:]}')

numb = int(input('Введите целое число: ')) 
print(bin(numb))






rom math import pow

def is_int(number):
    return number.isdigit()

def function(number):
    if number in (1, 2): 
        return 1
    
    return function(number - 1) + function(number - 2)

number = None

while not is_int(str(number)):
    number = input(«Input number:»)

number = int(number)

result = list()
for i in range(-number, number + 1):
    if i != 0: 
        result.append(int(pow(i / abs(i), i + 1) * function(abs(i))))
    else:
        result.append(0)

print(result)





def fibonacci(n):
    first, second = 0, 1
    fibonacci_num = 0
    for i in range(n):
        fibonacci_num = first + second
        second = first
        first = fibonacci_num
    return fibonacci_num


def negative_fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


set_number = (input("Введите число: "))
while not set_number.isdigit():
    set_number = (input("Введите еще раз: "))
set_number = int(set_number)
list = [0]
for i in range(1, set_number + 1):
    list.append(fibonacci(i))
    list.insert(0, negative_fibonacci(i))
print(list)

С рекурсией фибоначи
# # рекурсия тормозит нещадно после 40
# def fibonacci(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


k = int(input('Введите число: '))
print(k)
nego = [1,-1]
fibo = [1,1]
for i in range(2,k):
    lst_fibo = fibo[i-1]+fibo[i-2]
    fibo.append(lst_fibo)
for x, elem in enumerate(fibo, 2):
    if x % 2 != 0:
        lst_nego = elem * -1
        nego.append(lst_nego)
    else:
        nego.append(elem)
nego.reverse()
nego.append(0)
print(nego+fibo)






1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.



i = '1 2 3 4  5 6'
result = list(map(int, i.split()))
print(max(result), min(result))

nums = '2 54 6  7 8  89 56 5 3'
my_list = [int(num) for num in nums.split()]
print(min(my_list), max(my_list))


2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
    1) с помощью математических формул нахождения корней квадратного уравнения
    
    2) с помощью дополнительных библиотек Python

a = -3
b = 2
c = 1
dis = b**2 - 4 * a * c # дискриминант
if a == 0:
    x = -c /b
    print(x)
elif dis > 0:
    x1 = (-b - dis**0.5) / (2 * a)
    x2 = (-b + dis**0.5) / (2 * a)
    print(x1, x2)
elif not dis:
    x = -b/(2 * a) 
    print(x)
else: print("нет корней")










    
3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

nums




a, b = 6, 8
i = min(a, b)
while True:
    if i%a==0 and i%b==0:
        break
    i += 1
print(i)



a, b = 4, 12
nok = max(a, b)
while not (nok%a==0 and nok%b==0): # while nok%a !=0 or nok%b !=0:
    nok += max(a,b)
print(nok)


# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


n= 235423.2345345 # input('введите вещественное число')
#235423.2345345.is_integer() - False
#235423.0.is_integer() - True
while not float(n).is_integer():
    n *= 10
    print(n)

фибоначи

# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
num = 8
my_list = [1, 0, 1]
for _ in range(1, num):
    # print(my_list[0], my_list[1] - my_list[0] )
    # print(my_list[-1], my_list[-2] + my_list[-1])
    my_list.append(my_list[-2] + my_list[-1])
    my_list.insert(0, my_list[1] - my_list[0])




. Вычислить число c заданной точностью *d*
    
    *Пример:* 
    
    - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

    *Пример:* 
    
    - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

34. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


from __future__ import annotations
from math import pi

d =  input('Введите число для заданной точности числа Пи: ')
d = len(str(d).split('.')[1])
print(f'число Пи с заданной точностью "{d} знак" равно {round(pi, d)}')



number = float(number)
print('pi->', round(int(pi / number) * number, 10)) 


n = int(input('Введите число: '))
lst = []
for i in range(2,n + 1):
    if n % i == 0:
        count = 1
        for j in range(2,(i//2 + 1)):
            if(i % j == 0):
                count = 0
                break
        if(count == 1):
            lst.append(i)
print(lst)








n = int(input('Введите число: '))
lst = []
for i in range(2,n**0.5):
    if n % i == 0:
        count = 1
        for j in range(2,(i//2 + 1)):
            if(i % j == 0):
                count = 0
                break
        if(count == 1):
            lst.append(i)
print(lst)



3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.



# Первый вариант, через множество
numbers = [1, 2, 2, 3, 3, 4, 4, 5, 5]
unikum_numbers = list(set(numbers))
print(unikum_numbers)


# Второй вариант, с сохранением того же порядка 
import numpy
numbers = [1, 2, 2, 3, 3, 4, 4, 5, 5]
res = numpy.array(numbers)
unikum_numbers = numpy.unique(res)
print(unikum_numbers)
From Tolik to Everyone 10:04 PM
enum_number = list(map(int, input("input list:").split()))

enum_unique = list(filter(lambda item: enum_number.count(item) == 1, enum_number))

print(enum_number, '->', enum_unique)







4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
    






k=int(input("введите   k:"))
res=open("rezout.txt","w")
for i in range(3): # в файл повторить так 3 раза...
  rezstr=""# пустая строка для строки в файл.
  for j in range(0,k): # строим многочлен
    koef=randint(0,10)
    if koef>0: # т.е. множитель не равен 0
      #собираем строку согласно "правописанию"
      if j==0: # это на тот случай если степень равна 0
          rezstr=str(koef)
      elif j==1:#когда степень равна 1
          if koef>1:
            rezstr=str(koef)+"*x" +rezstr
          else:
            rezstr="x" +rezstr
      else:#в остальных случаях
          if koef>1:
             rezstr=str(koef)+"*x**"+str(j)+rezstr
          else:
             rezstr="x**"+str(j)+rezstr
      rezstr="+"+rezstr
      # в принципе этот фрагмент можно было положить в функцию, но слишком эта простая ...
  if rezstr[0]=="+":#убираем слева плюс в строке
        rezstr=rezstr[1:]
  res.writelines(rezstr+"\n");     print(rezstr)
res.close



import random


def generate_superscript(x, n):
    if n == 0:
        return str(x)
    if n == 1:
        return str(x)+"x"
    superscript = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
    result = str(x)
    if x != 0:
        result += "x"
    for i in str(n):
        result += superscript[int(i)]
    return result

def generate_polynomial(k):
    result = []
    for i in range(k, -1, -1):
        coefficient = random.randint(0, 100)
        if coefficient != 0:
            result.append(generate_superscript(coefficient, i))
    return "+".join(result)


print(generate_polynomial(10))














with open('rez01.txt', 'w') as file:
    file.write('3*x**8+9*x**7+3*x**6+3*x**5+8*x**4+3*x**3+10*x**2+2*x+4')
with open('rez02.txt', 'w') as file:
    file.write('6*x**8+10*x**7+7*x**5+10*x**4+7*x**3+5*x**2+10')
with open('rez01.txt','r') as file:
    o_1 = file.readline()
    l_1 = o_1.split()
with open('rez02.txt','r') as file:
    o_2 = file.readline()
    l_2 = o_2.split()
print(f'{l_1} + {l_2}')
sum_poly = l_1 + l_2
with open('sum_rez.txt', 'w') as file:
    file.write(f'{l_1} + {l_2}')


o_1 =  '3*x**8+9*x**7+3*x**6+3*x**5+8*x**4+3*x**3+10*x**2+2*x+4'.split('+')

o_2 = '6*x**8+10*x**7+7*x**5+10*x**4+7*x**3+5*x**2+10'.split('+')

print(o_1 + o_2)



35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

1. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
    
    *Пример:* 
    
    [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
    


A = [1, 2, 3, 4, 6, 7]
for i in range(1, len(A)):
    if A[i]-1 != A[i-1]:
        print(A[i-1]+1)
Ответ: 5


if A[i]-A[i-1] != 1: так более нагляднее






my_str = '1 2 3 4 5 6 8 9'
my_list = list(map(int, my_str.split()))
print(my_list)
for item in range(1, len(my_list)):
    if my_list[item] - 1 != my_list[item-1]:
        print(my_list[item-1]+1)







num = [11, 5, 2, 3, 4, 6, 1, 7, 9, 8, 10]

def nextmax(listt):    
    max = listt[0]
    res = [listt[0]]
    for i in range(len(listt)):
        if listt[i] > max:
            max = listt[i]
            res.append(max)
    if len(res) < 3:
        res = nextmax(listt[1:])
    return res

print(nextmax(num))





num = [1, 5, 2, 3, 4, 6, 1, 7, 9, 8, 10]

def nextmax(listt):    
    max = listt[0]
    res = [listt[0]]
    for i in range(len(listt)):
        if listt[i] > max:
            max = listt[i]
            res.append(max)
        
    return res

print(nextmax(num))





38. Напишите программу, удаляющую из текста все слова, содержащие "абв".




my_list = [1, 2, 4, 5, 6, 8, 9, 11]

res = [(my_list[i] - 1) for i in range(1, len(my_list)) if (my_list[i] - 1) != my_list[i - 1]]
print(res)

res = [my_list[0]]
[res.append(item) for item in my_list if item > res[-1]]
print()


print(' '.join(filter(lambda x: not 'абв' in x,'Мы неабв очень любим Питон иабв Джавуабв!'.split())))

my_str = 'Мы неабв очень любим Питон иабв Джавуабв!'.split()
res = [word for word in my_str if 'абв' not in word]
print(' '.join([word for word in my_str if 'абв' not in word]))

Ответ: Мы очень любим Питон



<<<<<<< HEAD
my_list = ["123","234", "12333", "567", "123"]
number = my_list[0]
print(my_list.index(number, 1))



Sergey, [10/4/2022 1:54 PM]
[In reply to Илья Буржуй]
Вы указываете значение d в формате 0,00001, и округляете второе число до значения d

ᅠ ᅠ, [10/4/2022 2:19 PM]
from distutils.command.clean import clean

clean
import random

# запись в файл
def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)

# создание случайного числа от 0 до 100
def rnd():
    return random.randint(0,101)

# создание коэффициентов многочлена
def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    
# создание многочлена в виде строки 
def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

# получение степени многочлена
def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# получение коэффицента члена многочлена
def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбор многочлена и получение его коэффициентов
def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 # степень
    ii = l-1 # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst

# создание двух файлов

k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file("file_1.txt", create_str(koef1))
write_file("file_2.txt", create_str(koef2))

# нахождение суммы многочлена

with open('file_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])
write_file("file_res.txt", create_str(lst_new))
with open('file_res.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")
=======
text_my = 'Напишите программуабв, удаляющуюабв из текста все словаабв, содержащие "абв"'

text_my = list(filter(lambda x: 'абв' not in x, text_my.split()))
my = " ".join(text_my)  сделаем строку
print(my)


>>>>>>> refs/remotes/origin/main


Семинар 6


# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 
    
#     *Пример:* 
    
#     2+2 => 4; 
    
#     1+2*3 => 7; 
    
#     1-2*3 => -5;
    
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
        
#         *Пример:* 
        
#         1+2*3 => 7; 
        
#         (1+2)*3 => 9;
        

# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# *Пример:* 

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]



def split_expression(expr):
    buffer = ""
    result = []
    for digit in expr:
        if digit.isdigit():
            buffer += digit
        else:
            result.append(int(buffer))
            result.append(digit)
            buffer = ""
    result.append(int(buffer))
    return result

my_text = '1-2*3*4*2+8/4+9-3+7'
my_list = list(my_text)
print(my_list)

my_list1 = eval(my_text) # Не рекомендованная функция
print(my_list1)
# exec(f'print({my_text})') # Не рекомендованная функция

i = 1

while '*' in my_list or '/' in my_list:
    if my_list[i] == '*':
        my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
        del my_list[i+1]
        del my_list[i]
    elif my_list[i] == '/':
        my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
        del my_list[i+1]
        del my_list[i]
    else: i += 1    

i = 1

while '+' in my_list or '-' in my_list:
    if my_list[i] == '+':
        my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
        del my_list[i+1]
        del my_list[i]
    elif my_list[i] == '-':
        my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
        del my_list[i+1]
        del my_list[i]
    else: i += 1   
print(my_list)








Исправленный Итоговый вариант:
def calc(my_list):
    i = 1

    while '*' in my_list or '/' in my_list:
        if my_list[i] == '*':
            my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
            del my_list[i+1]
            del my_list[i]
        elif my_list[i] == '/':
            my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
            del my_list[i+1]
            del my_list[i]
        else: i += 1    

    i = 1

    while '+' in my_list or '-' in my_list:
        if my_list[i] == '+':
            my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
            del my_list[i+1]
            del my_list[i]
        elif my_list[i] == '-':
            my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
            del my_list[i+1]
            del my_list[i]
        else: i += 1
    print('Выводим из функции результат:', my_list)
    return my_list

my_text = '1-2*3*4*(2+8*2)/4+9-3+7'
my_list_out = list(my_text)
print(my_list_out)

while '(' in my_list_out:
    bracket_left = my_list_out.index('(')
    bracket_right = my_list_out.index(')')
    my_list_out = my_list_out[:bracket_left] + calc(my_list_out[bracket_left + 1 : bracket_right]) + my_list_out[bracket_right + 1 :]

print(my_text + '=>' + str(calc(my_list_out)[0]))



43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

*Пример:* 

[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
From Сергей to Everyone 11:03 PM
my_list = [1, 2, 3, 5, 1, 5, 3, 10]
new_list = []
for i in range(0,len(my_list)):
    if my_list.count(my_list[i]) == 1:
        new_list.append(my_list[i])
print(new_list)






#Задайте последовательность чисел. 
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
enum_number = list(map(int, input("input list:").split()))

enum_unique = list(filter(lambda item: enum_number.count(item) == 1, enum_number))

print(enum_number, '->', enum_unique)


lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")
From Сергей to Everyone 11:10 PM
my_list = [1, 2, 3, 5, 1, 5, 3, 10]
new_list = []
for i in range(len(my_list)):
    if my_list.count(my_list[i]) == 1:
        new_list.append(my_list[i])
print(my_list, '=>' , new_list)


enum_number = [1, 2, 3, 5, 1, 5, 3, 10]

enum_unique = list(filter(lambda item: enum_number.count(item) == 1, enum_number))

print(enum_number, '->', enum_unique)

filter_unique = filter(lambda item: enum_number.count(item) == 1, enum_number)
print(filter_unique)
print(list(filter_unique))
print(tuple(filter_unique))
for i in filter_unique:
    print(i)


my_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(list(range(8,-4, -1)))
for i in range(len(my_list) - 1,-1, -1):
    if my_list.count(my_list[i]) != 1:
        del my_list[i]


https://github.com/BlackStoneShadow/Python/blob/main/Lesson5/Task2/Task2.py


# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
my_text = 'Скажика дядя ведь не даромабв Москва спалеабвнная пажаром французам отдана'
print(my_text)

my_list = my_text.split()
print(my_list)

for item in  my_list:
    if 'абв' in item:
        my_list.remove(item)

print(my_list)
From Sacred Sliver to Everyone 11:46 PM
вот 3 строчки
text_my = filter(lambda x: 'абв' not in x, text_my.split())
my = " ".join(text_my)
print(my)

HW

# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
import random
# generate random words from syllables
syllables = ["ма", "за", "ба", "ка", "ша", "бв"]
print(random.sample(syllables,2))
text = list(map(lambda x: "".join(random.sample(syllables,3)), range(random.randint(12,15))))
print(f' TEXT : {" ".join(text)}')
print(*text)
# search for syllable "абв" and delete it with whole word
parsed_text = list(x for x in text if "абв" not in x)
print(f'PARSED: {" ".join(parsed_text)}')





import random
# Function checks man to take rules quantity max and min candies
def man_quantity(min, max):
    candy = int(input("How many candies you takes?: "))
    while candy > max or candy < min: 
        print ("You could take more than 0 and no more than 28 candies!")
        candy = int(input("How many candies you takes?: "))
    return candy
# Function bot take random candies
def bot_quantity(min, max):
    candy = random.randint(min, max)
    print(f"{bot}, takes {candy} candies")
    return candy
# Print rules of the game
text = "On the desk is 2021 candies.\n\
2 players make move one by one.\n\
Who is first player decides the lot.\n\
With on movie player could take no more than 28 candies\n\
Winner is player with last move.\n\
How many candies must take first player to win?"
print(text)
# Games VARS, could be changed
candies = 221
max = 28
min = 1
bot = "Bot"
##############################
man = input("Enter your name: ")
# First player random choice
lot = random.choice([man, bot])
if lot == bot:
    print(f'First player is {lot}')
else:
    print(f"{man}, you're first player")
# Game core
while candies > 1:
    if lot == bot:
        candies -= bot_quantity(min, max)
        if candies < 0:
            break
        print(f'{candies} candies left')
        lot = man
    else:
        candies -= man_quantity(min, max)
        if candies < 0:
            break
        print(f'{candies} candies left')
        lot = bot

# Who is looser :))
print(f"{lot}, is lost, {candies} candies!")





# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint, random

n = 2021
m = 28

def my_game(who, how_many, part):
    game_count = 1
    if who == 0:
        right_move = how_many % (part+1)
        how_many = how_many - right_move
        print(f'ХОД({game_count}) Bot: я возьму {right_move} конфет')
        print(f'Остаток конфет: {how_many}')
        game_count += 1
        while how_many > 0:
            while True and how_many>0:
                move_player  = int(input(f'ХОД({game_count}) {player}, введите сколько конфет вы хотите взять: ')) 
                if move_player > part:
                    print(f'{player}, количество конфет должно быть меньше {part}')
                    break
                move_bot = part+1-move_player
                how_many = how_many - move_player
                print(f'Остаток конфет: {how_many}')
                game_count += 1
                print(f'ХОД({game_count}) Bot: а я возьму {move_bot}')
                how_many = how_many - move_bot                
                print(f'Остаток конфет: {how_many}')
        print('Bot: я сделал последний ход и победил! Не переживай, повезет в другой раз!')
    else:
        while how_many >0:
            while True and how_many>0:
                move_player  = int(input(f'ХОД({game_count}) {player} введите сколько конфет вы хотите взять: ')) 
                if move_player > part:
                    print(f'{player}, количество конфет должно быть меньше {part}')
                    break
                how_many = how_many - move_player
                print(f'Остаток конфет: {how_many}')
                if how_many == 0: 
                    print(f'{player}, ты победил, конфеты твои!!!')
                    game_count += 1    
                else:
                    if 0 < how_many <= part:
                        move_bot = how_many
                    else:
                        move_bot = randint(1, 28)
                    print(f'ХОД({game_count}) Bot: а я возьму {move_bot}')
                    how_many = how_many - move_bot
                    print(f'Остаток конфет: {how_many}')
                    if how_many == 0: 
                        print('Bot: я сделал последний ход и победил! Не переживай, повезет в другой раз!')
                    game_count += 1

user_answer = input('Хотите сыграть в игру? "да"/"нет"?: ')
if user_answer == 'да':
    player = input('Введите свое имя: ')
    print('Хорошо! Поехали! А вот и условие. \n На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
    my_cho = int(randint(0,1))
    if my_cho == 1:
        print(f'{player}, Ты ходишь первый!')
    else:
        print('Я хожу первый!')
        print('Поехали!')
    my_game(my_cho, n, m)
else:
    print('Ну и не надо =(')


https://github.com/sacredsliver/Python/tree/master/DZ5





from random import randint
import os
os.system('cls')


def checking_input(name):
    n = (
        input(f'\n{name}, введите количество конфет, которое возьмете от 1 до 28: '))
    while not n.isdigit():
        n = (
            input(f'{name}, введите корректное количество конфет: '))
    n = int(n)
    os.system('cls')
    return (n)


def input_dat(name):
    x = checking_input(name)
    while x < 1 or x > 28:
        x = checking_input(name)
    return x


def input_bot(name):
    if counter1 == 0:
        k = randint(1, 28)
    else:
        k = 29 - includ
    return k


def motion_print(name, k, counter, value):
    print(
        f'Ходил {name}, он взял {k} конфет, теперь у него {counter} конфет. Осталось на столе {value} конфет.')


print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
input('\nДля начала игры нажмите "Ввод"')
os.system('cls')
player1 = input('Введите имя первого игрока: ')
player2 = input(
    '\nВведите имя второго игрока, или введите Бот для игры с ботом: ')

if player2 == 'Бот':
    player3 = player2
value = int(input('Введите количество конфет на столе(2021): '))
counter1 = 0
counter2 = 0
counter3 = 0
includ = 0
print('\nКоличество конфет на столе:', value)
flag = randint(0, 2)  # флаг очередности
if flag:
    print(f'Первый ходит {player1}')
elif flag and player2 == 'Бот':
    print(f'Первый ходит {player3}')
else:
    print(f'Первый ходит {player2}')

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        includ = k
        flag = False
        motion_print(player1, k, counter1, value)
    elif player2 == 'Бот':
        k = input_bot(player3)
        counter3 += k
        value -= k
        flag = True
        motion_print(player3, k, counter3, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        motion_print(player2, k, counter2, value)

if flag:
    print(f'Выиграл {player1}')
else:
    print(f'Выиграл {player2}')




from random import randint
import os
os.system('cls')


def checking_input(name):
    n = (
        input(f'\n{name}, введите количество конфет, которое возьмете от 1 до 28: '))
    while not n.isdigit():
        n = (
            input(f'{name}, введите корректное количество конфет: '))
    n = int(n)
    os.system('cls')
    return (n)


def input_dat(name):
    x = checking_input(name)
    while x < 1 or x > 28:
        x = checking_input(name)
    return x


def input_bot(name):
    if counter1 == 0:
        k = randint(1, 28)
    else:
        k = 29 - includ
    return k


def motion_print(name, k, counter, value):
    print(
        f'Ходил {name}, он взял {k} конфет, теперь у него {counter} конфет. Осталось на столе {value} конфет.')


print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
input('\nДля начала игры нажмите "Ввод"')
os.system('cls')
player1 = input('Введите имя первого игрока: ')
player2 = input(
    '\nВведите имя второго игрока, или введите Бот для игры с ботом: ')

if player2 == 'Бот':
    player3 = player2
value = int(input('Введите количество конфет на столе(2021): '))
counter1 = 0
counter2 = 0
counter3 = 0
includ = 0
print('\nКоличество конфет на столе:', value)
flag = randint(0, 2)  # флаг очередности
if flag:
    print(f'Первый ходит {player1}')
elif flag and player2 == 'Бот':
    print(f'Первый ходит {player3}')
else:
    print(f'Первый ходит {player2}')

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        includ = k
        flag = False
        motion_print(player1, k, counter1, value)
    elif player2 == 'Бот':
        k = input_bot(player3)
        counter3 += k
        value -= k
        flag = True
        motion_print(player3, k, counter3, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        motion_print(player2, k, counter2, value)

if flag:
    print(f'Выиграл {player1}')
else:
    print(f'Выиграл {player2}')




def field(moves):
    y0 = f"    X1    X2   X3  "
    y1 = f"Y1  {moves['y1']['x1']}  |  {moves['y1']['x2']}  | {moves['y1']['x3']}  "
    y1_1 = "  -----+-----+-----"
    y2 = f"Y2  {moves['y2']['x1']}  |  {moves['y2']['x2']}  | {moves['y2']['x3']}  "
    y1_1 = "  -----+-----+-----"
    y3 = f"Y3  {moves['y3']['x1']}  |  {moves['y3']['x2']}  | {moves['y3']['x3']}  "
    print(y0)
    print(y1)
    print(y1_1)
    print(y2)
    print(y1_1)
    print(y3)

def check(move, moves):
    if len(move) == 4:
        if move[0].lower() == 'y' and move[2].lower() == 'x':
            if move[1] in '123' and move[-1] in '123':
                if moves[move[:2]][move[-2:]] == ' ':
                    return True
                else:
                    print('Данная клетка уже занята.')
            else:
                print('Введены недопустимые значения координат.')
        else:
            print('Вы ввели не допустимые оси координат')
    else:
        print('Введено недопустимое количество символов.')
    print('Попробуйте ещё раз!')
    return False

def wins(moves):
    if ((moves['y1']['x1'] == moves['y1']['x2'] == moves['y1']['x3']
            or moves['y1']['x1'] == moves['y2']['x1'] == moves['y3']['x1']
            or moves['y1']['x1'] == moves['y2']['x2'] == moves['y3']['x3'])
            and moves['y1']['x1'] != ' '):
        return moves['y1']['x1']
    elif ((moves['y2']['x1'] == moves['y2']['x2'] == moves['y2']['x3']
           or moves['y1']['x2'] == moves['y2']['x2'] == moves['y3']['x2']
           or moves['y1']['x3'] == moves['y2']['x2'] == moves['y3']['x1'])
          and moves['y2']['x2'] != ' '):
        return moves['y2']['x2']
    elif ((moves['y3']['x1'] == moves['y3']['x2'] == moves['y3']['x3']
           or moves['y1']['x3'] == moves['y2']['x3'] == moves['y3']['x3'])
          and moves['y3']['x3'] != ' '):
        return moves['y3']['x3']
    return False


def move(symbol, moves, player):
    print('Текущий ход y{}x{}'.format(player[1], player[-1]))
    if player[1] == '1':
        if player[-1] == '1':
            moves['y1']['x1'] = symbol
        elif player[-1] == '2':
            moves['y1']['x2'] = symbol
        else:
            moves['y1']['x3'] = symbol
    elif player[1] == '2':
        if player[-1] == '1':
            moves['y2']['x1'] = symbol
        elif player[-1] == '2':
            moves['y2']['x2'] = symbol
        else:
            moves['y2']['x3'] = symbol
    else:
        if player[-1] == '1':
            moves['y3']['x1'] = symbol
        elif player[-1] == '2':
            moves['y3']['x2'] = symbol
        else:
            moves['y3']['x3'] = symbol
    return moves


moves_out = {
    'y1': {'x1': ' ', 'x2': ' ', 'x3': ' '},
    'y2': {'x1': ' ', 'x2': ' ', 'x3': ' '},
    'y3': {'x1': ' ', 'x2': ' ', 'x3': ' '}
}

field(moves_out)

number_players = int(input('Введите количество игроков (1/2): '))
count_move = 0

if number_players == 2:
    win = False
    while not win and count_move < 9:
        count_move += 1
        player_out = input('Введите координаты хода(пример - y2x3): ')
        while not check(player_out, moves_out):
            player_out = input('Введите координаты хода(пример - y2x3): ')
        if count_move % 2:
            symbol_out = 'X'
        else:
            symbol_out = 'O'
        moves_out = move(symbol_out, moves_out, player_out)

        field(moves_out)
        win = wins(moves_out)
    if count_move == 9:   # баг может быть и победа на 9 ходу
        print('Ничья!')
    else:
        print(f'На {count_move} ходу победили "{win}"')







Николай Мануилов, [10/11/2022 1:18 AM]
def field(moves):
    y0 = f"    X1    X2   X3  "
    y1 = f"Y1  {moves['y1']['x1']}  |  {moves['y1']['x2']}  | {moves['y1']['x3']}  "
    y1_1 = "  -----+-----+-----"
    y2 = f"Y2  {moves['y2']['x1']}  |  {moves['y2']['x2']}  | {moves['y2']['x3']}  "
    y1_1 = "  -----+-----+-----"
    y3 = f"Y3  {moves['y3']['x1']}  |  {moves['y3']['x2']}  | {moves['y3']['x3']}  "
    print(y0)
    print(y1)
    print(y1_1)
    print(y2)
    print(y1_1)
    print(y3)

def check(move, moves):
    if len(move) == 4:
        if move[0].lower() == 'y' and move[2].lower() == 'x':
            if move[1] in '123' and move[-1] in '123':
                if moves[move[:2]][move[-2:]] == ' ':
                    return True
                else:
                    print('Данная клетка уже занята.')
            else:
                print('Введены недопустимые значения координат.')
        else:
            print('Вы ввели не допустимые оси координат')
    else:
        print('Введено недопустимое количество символов.')
    print('Попробуйте ещё раз!')
    return False

def wins(moves):
    if ((moves['y1']['x1'] == moves['y1']['x2'] == moves['y1']['x3']
            or moves['y1']['x1'] == moves['y2']['x1'] == moves['y3']['x1']
            or moves['y1']['x1'] == moves['y2']['x2'] == moves['y3']['x3'])
            and moves['y1']['x1'] != ' '):
        return moves['y1']['x1']
    elif ((moves['y2']['x1'] == moves['y2']['x2'] == moves['y2']['x3']
           or moves['y1']['x2'] == moves['y2']['x2'] == moves['y3']['x2']
           or moves['y1']['x3'] == moves['y2']['x2'] == moves['y3']['x1'])
          and moves['y2']['x2'] != ' '):
        return moves['y2']['x2']
    elif ((moves['y3']['x1'] == moves['y3']['x2'] == moves['y3']['x3']
           or moves['y1']['x3'] == moves['y2']['x3'] == moves['y3']['x3'])
          and moves['y3']['x3'] != ' '):
        return moves['y3']['x3']
    return False


def move(symbol, moves, player):
    print('Текущий ход y{}x{}'.format(player[1], player[-1]))
    if player[1] == '1':
        if player[-1] == '1':
            moves['y1']['x1'] = symbol
        elif player[-1] == '2':
            moves['y1']['x2'] = symbol
        else:
            moves['y1']['x3'] = symbol
    elif player[1] == '2':
        if player[-1] == '1':
            moves['y2']['x1'] = symbol
        elif player[-1] == '2':
            moves['y2']['x2'] = symbol
        else:
            moves['y2']['x3'] = symbol
    else:
        if player[-1] == '1':
            moves['y3']['x1'] = symbol
        elif player[-1] == '2':
            moves['y3']['x2'] = symbol
        else:
            moves['y3']['x3'] = symbol
    return moves


moves_out = {
    'y1': {'x1': ' ', 'x2': ' ', 'x3': ' '},
    'y2': {'x1': ' ', 'x2': ' ', 'x3': ' '},
    'y3': {'x1': ' ', 'x2': ' ', 'x3': ' '}
}

field(moves_out)

number_players = int(input('Введите количество игроков (1/2): '))
count_move = 0

if number_players == 2:
    win = False
    while not win and count_move < 9:
        count_move += 1
        player_out = input('Введите координаты хода(пример - y2x3): ')
        while not check(player_out, moves_out):
            player_out = input('Введите координаты хода(пример - y2x3): ')
        if count_move % 2:
            symbol_out = 'X'
        else:
            symbol_out = 'O'
        moves_out = move(symbol_out, moves_out, player_out)

        field(moves_out)
        win = wins(moves_out)
    if count_move == 9:
        print('Ничья!')
    else:
        print(f'На {count_move} ходу победили "{win}"')

Slava, [10/11/2022 1:25 AM]
def encoding(text):
    code_text = ""
    count = 0
    repetitions = 1
    while count < len(text):
        try:
            if text[count] == text[count+1]:
                repetitions += 1
            elif repetitions == 1:
                code_text += text[count]
            elif repetitions > 1:
                code_text += str(repetitions) + text[count]
                repetitions = 1
        except IndexError:
            if repetitions == 1:
                code_text += text[count]
            elif repetitions > 1:
                code_text += str(repetitions) + text[count]
        count += 1
    return code_text
# Function to decode given cipher
def decoding(cipher):
    decoded_text = ""
    count = 0
    repetitions = 0
    while count < len(cipher):
        if str(cipher[count]).isdigit():
            repetitions = int(cipher[count])
        elif repetitions > 0:
            for x in range(repetitions):
                decoded_text += cipher[count]
                repetitions = 0
        elif repetitions == 0:
            decoded_text += cipher[count]
        count +=1
    return decoded_text
# Text input  
text = input("Enter a text: ")
# Decides encode or decode
numbers_in_text = 0
for num in text:
    if num.isdigit():
        numbers_in_text += 1
# If any digits exists it mean coded text, decoding
if numbers_in_text > 0:
    print(f"Decoding: {decoding(text)}")
# If no digits exists it mean pure text, encoding
else:
    print(f"Encoding: {encoding(text)}")




my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)



бот
  def input_bot(name):
    if counter1 == 0 and value % 29 != 0:
        k = int(value % 29)
    elif counter1 == 0 and value % 29 == 0:
        k = 1
    else:
        k = 29 - includ
    return k







def check_win(check):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8))
    for each in win_coord:
        if check[each[0]] == check[each[1]] == check[each[2]]:
            return check[each[0]]
    return False




print(id("x"),id("х"),id("x"))




 Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.  


import pickle
# Сжимает файл по алгоритму RLE и сохраняет его в бинарном формате
# сохраняется два списка (1-список символов 2-сколько раз этот символ подряд повторяется)
def compression_rle (in_file: str,  out_file: str):
    with open(in_file, 'r') as file_read_bin, open(out_file, 'wb') as file_write_bin:
        not_compress_file = file_read_bin.readlines()
        compress_file_list = []
        repeat_char_list= []
        for i in range(len(not_compress_file)):
            repeat_char_index = 0
            count_repeat_char = 0
            for j in range(len(not_compress_file[i])):            
                if not_compress_file[i][repeat_char_index] == not_compress_file[i][j]:
                    count_repeat_char += 1
                else:
                    compress_file_list.append(not_compress_file[i][repeat_char_index])
                    repeat_char_list.append(count_repeat_char)
                    repeat_char_index = j
                    count_repeat_char = 1
            else:
                compress_file_list.append(not_compress_file[i][repeat_char_index])
                repeat_char_list.append(count_repeat_char)
        pickle.dump(compress_file_list, file_write_bin)
        pickle.dump(repeat_char_list, file_write_bin)

# Распаковывает файл по алгоритму RLE и сохраняет его в оригинальном виде
# распаковывается два списка (1-список символов 2-сколько раз этот символ подряд повторяется)
def extract_rle (in_file: str, out_file: str):
    with open(in_file, "rb") as file_read_bin, open(out_file, 'w') as file_write:
        compress_list = pickle.load(file_read_bin)
        repeat_list = pickle.load(file_read_bin)
        result_str = ''
        for i in range(len(compress_list)):
            if repeat_list[i] != '\n':
                for j in range(int(repeat_list[i])):
                    result_str += compress_list[i]
            else:
                result_str += '\n'
        file_write.writelines(result_str)


# Заполняем тестовый файл записями 
with open("original.txt", "w") as file:
    file.write('TEST                                                        ' + '\n')
    file.write('     TEST                                                   ' + '\n')
    file.write('          TEST                                              ' + '\n')
    file.write('               TEST                                         ' + '\n')
    file.write('                    TEST                                    ' + '\n')
    file.write('                         TEST                               ' + '\n')
    file.write('WWWWWWWWWWWWWWWWWWWWWWWWW00000000000000000000000000000000000' + '\n')
    file.write('SSSSSSSSSSSSSSSSSS111111111111111111111111TTTTTTTTTTTTTTTTTT' + '\n')
    file.write('444444444444444444444444433333333333333333333333333333333333' + '\n')
    file.write('999999999999999988888888888888888888888877777777777777777777' + '\n')
    file.write('5555555          666666666666             777777777777777777' + '\n')


# Сжимаем файл по алгоритму RLE
compression_rle('original.txt', 'compress.bin')
# Восстанавливаем файл по алгоритму RLE
extract_rle('compress.bin', 'extract.txt')

# Результатом работы программы являются 3 файла: original.txt, compress.bin, extract.txt





Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
Sample Input 1:
6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n
Sample Output 1:
1 2 3
Sample Input 2:
9
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton
Sample Output 2:
1 2 7 8


n = int(input())
list1 = []
for i in range(n):
    a = input()
    if 'a' in a:
        a = a[a.find('a'):]
        if 'n' in a:
            a = a[a.find('n'):]
            if 't' in a:
                a = a[a.find('t'):]
                if 'o' in a:
                    a = a[a.find('o'):]
                    if 'n' in a:
                        list1.append(i + 1)                   
print(*list1)




for i in range(int(input())):
    s, virus, x  = input(), 'anton', 0
    for sym in s:
        if sym == virus[x]:
            x += 1
        if x == 5:
            print(i + 1, end=' ')
            break





n = int(input())
list1 = []
for i in range(n):
    a = input()
    if 'a' in a:
        a = a[a.find('a'):]
        if 'n' in a:
            a = a[a.find('n'):]
            if 't' in a:
                a = a[a.find('t'):]
                if 'o' in a:
                    a = a[a.find('o'):]
                    if 'n' in a:
                        list1.append(i + 1)                   
print(*list1)






**Задание в группах:** Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. 

- *под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, пустая строка - разделитель
    
   

 *Фамилия_1*
    
    *Имя_1*
    
    *Телефон_1*
    
    *Описание_1*
    
    *Фамилия_2*
    
    *Имя_2*
    
    *Телефон_2*
    
    *Описание_2*
    
    *и т.д.в файле на одной строке хранится все записи, символ разделитель - ;
    
    *Фамилия_1,Имя_1,Телефон_1,Описание_1*
    
    *Фамилия_2,Имя_2,Телефон_2,Описание_2*






def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice




def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)


**Задача:** Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.

В рамках этого обсуждения студентам надо нарисовать “архитектуру” (например, в виде блок-схемы) для работы данного приложения.


Комплексные числа
Комплексные числа
сложение : 4 + 4i + 3 + 5i = 7 + 9i
разница 5 + 4i - (7 + 2i) = -2 + 2i
умножение (4 + 2i) * (3 + 5i) = 12 + 20i + 6i + 10i^2 = 12 + 26i + 10 *(-1) = 12 + 26i - 10 = 2 + 26i



Встроенная функция complex()
Встроенная функция complex(real[, imag]) позволяет создать комплексное число на основе значений его действительной и мнимой частей:
>>> complex(1)    #  аргумент imag не обязателен
(1+0j)
>>> 
>>> complex(1, 2e-2)
(1+0.02j)
Приятным сюрпризом данной функции, является то что она может создавать комплексное число из строки. Но с небольшой оговоркой, эта строка должна быть допустимым литералом комплексного числа:


телефон справ
https://github.com/sacredsliver/Python/tree/master/DZ7


**Задание в группах:** Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. 

- *под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, пустая строка - разделитель*
    
    *Фамилия_1*
    
    *Имя_1*
    
    *Телефон_1*
    
    *Описание_1*
    
    *Фамилия_2*
    
    *Имя_2*
    
    *Телефон_2*
    
    *Описание_2*
    
    *и т.д.в файле на одной строке хранится все записи, символ разделитель - **;***
    
    *Фамилия_1,Имя_1,Телефон_1,Описание_1*
    
    *Фамилия_2,Имя_2,Телефон_2,Описание_2*
    
    *и т.д.*

https://github.com/tr4k87/DZ7.git

https://github.com/tr4k87/DZ7.git





## Групповая работа [2]






**Задача:** Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

**Задача:** Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы

*(прямая отсылка [к первому семинару “введение в базы данных”](https://www.notion.so/ada887424df04be6b876ee8734aabcf1))*

<aside>
❗ Решение каждой задачи начинается с обсуждения, только после этого пишется код.

</aside>


model.py


BASE = "base.csv"

def edit(id, data):
    res = []
    with open(BASE, "r") as file:
        base = file.read().split('\n') 
        for item in base:
            line = item.split(';')
            if line[0] == id:
                line = data
                res.append(line)
            else:
                res.append(line)
    with open(BASE, "w") as file:
        file.write(res)
    return "Success"

def upload(file):
    with open(BASE, "a") as file:
        file.writelines(f'{data[0]};{data[1]};{data[2]};{data[3]};{data[4]};{data[5]};{data[6]};{data[7]}\n')
    return "Запись сохранена"

def add(data):
    with open(BASE, "a") as file:
        file.writelines(f'{data[0]};{data[1]};{data[2]};{data[3]};{data[4]};{data[5]};{data[6]};{data[7]}\n')
    return "Запись сохранена"

def find(data):
    res = []
    with open(BASE, "r") as file:
        base = file.read().split('\n') 
        for item in base:
            line = item.split(';')
            lists = list(filter(None, data))
            if set(lists).issubset(line) and len(line) > 1:
                res.append(line)
    return res

def delete(data):
    res = []
    with open(BASE, "r") as file:
        base = file.read().split('\n') 
        for item in base:
            line = item.split(';')
            lists = list(filter(None, data))
            if not set(lists).issubset(line) and len(line) > 1:
                res.append(line)



работа со словарями



my_dict = {3:'Иванов', 1: 'Васльев', 4:'Петров'}


for elem in sorted(my_dict):
    print(elem)
    print(elem, my_dict[elem])
    
for key, value in sorted(my_dict.items()):
    print(key, value)

print(my_dict)
print(sorted(my_dict))
print(my_dict.items())
print(type(my_dict.items()))
print(sorted(my_dict.items()))
print(my_dict.keys())
print(sorted(my_dict.keys()))
print(my_dict.values())
print(sorted(my_dict.values()))

my_list = [(1, 'a', True),(2, 'b', False),(3, 'x', True)]
for first, second, third in my_list:
    print(first)
    print(second)
    print(third)
    print()
    print('Следующй цилк')






def find_by_number(data: list, phone_number: str) -> str:
    for el in data:
        if el.get("Телефон") == phone_number:
            return f'{el.get("Фамилия")}, {el.get("Имя")}'
    return "Такой абонент отсутвует"






РЕШЕНИЕ ДЛЯ WINDOWS - В Windows при установке Python необходимо было установить галочку для установки pip, установить путь Python в папку с:\Program Files, а не в User, и обязательно поставить галочку add PATH

pip install -r requirements.txt



/start
From Igor to Everyone 10:25 PM
это есть в лекции
From Сергей Сердюк to Everyone 10:26 PM
/newbot


сайт pythonanywhere

https://www.pythonanywhere.com/



## Групповая работа [2]

Учимся настраивать виртуальное окружение и работать с [PIP](https://pypi.org/)

В качестве пробы библиотек к программам предыдущего модуля подключить работу с XML \ JSON

> Для тренировки можно создания телеграм-бота полезные ссылки:
> 
> 
> [https://core.telegram.org/bots](https://core.telegram.org/bots)
> 
> [https://github.com/python-telegram-bot/python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
> 
> [https://core.telegram.org/bots/api#authorizing-your-bot](https://core.telegram.org/bots/api#authorizing-your-bot)
> 
> [https://core.telegram.org/bots/api#available-methods](https://core.telegram.org/bots/api#available-methods)
> 
> [https://core.telegram.org/bots/api#user](https://core.telegram.org/bots/api#user)
>
**Задача:** при помощи виртуального окружения и PIP реализовать решение задач с прошлых семинаров:

1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
2. Создайте программу для игры с конфетами человек против человека.
    
    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
    
    a) Добавьте игру против бота
    
    b) Подумайте как наделить бота "интеллектом"









from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def abc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    msg = filter(lambda x: 'ов' not in x, msg.split())
    my = " ".join(msg)
    await update.message.reply_text(my)

app = ApplicationBuilder().token("Указать свой токен").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("abc", abc))
app.run_polling()


бот конфет

def bot_quantity(candies):
    if candies > 28:
        candy = candies%(29)
    else:
        candy = candies
    # candy = random.randint(min, max)
    print(f"{bot}, takes {candy} candies")
    return candy










    from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def abc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    msg = filter(lambda x: 'ов' not in x, msg.split())
    my = " ".join(msg)
    await update.message.reply_text(my)

app = ApplicationBuilder().token("Указать свой токен").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("abc", abc))
app.run_polling()



pip install python-telegram-bot --pre






SacredSliver, [10/20/2022 11:02 PM]
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def abc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    msg = filter(lambda x: 'ов' not in x, msg.split())
    my = " ".join(msg)
    await update.message.reply_text(my)

app = ApplicationBuilder().token("Указать свой токен").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("abc", abc))
app.run_polling()

Olga D, [10/20/2022 11:27 PM]
[In reply to Николай Мануилов]
Больше похоже на то, что ГБ отмазывается от нас, чем на правду - типа с начала лета оптимизация, однако в сентябре они мне подтверждают, что у меня программа 2 года ,  буквально через пару дней - год - и то об этом узнаешь чисто случайно.  А сообщить-то не судьба? Говорят, что "мы не смогли уместить больше на 2035, но у вас будет "все" и гораздо больше" . А по факту, что мы имеем? Вот вам  - Курсы по компьютерной грамотности - ибо это , наверное, главное в ИИ

Dmitry, [10/21/2022 12:50 AM]
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes



def bot_quantity():
    global candies
    if candies > 28:
        candy = candies % 29
    else:
        candy = candies
    # candy = random.randint(min, max)
    # print(f"{bot}, takes {candy} candies")
    return candy

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def new_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global candies
    candies = 100

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global candies
    
    msg = update.message.text
    msg = msg.split()[1]    
    msg_number = int(msg)
    candies -= msg_number
    await update.message.reply_text(f'Осталось конфет {candies}')
    bot_candy = bot_quantity()
    await update.message.reply_text(f'Бот {bot_candy} конфет')
    candies -= bot_candy
    await update.message.reply_text(f'Осталось конфет {candies}')

async def abc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    msg = filter(lambda x: 'ов' not in x, msg.split())
    my = " ".join(msg)
    await update.message.reply_text(my)
    
candies = 100

app = ApplicationBuilder().token('Ваш Токен').build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("abc", abc))
app.add_handler(CommandHandler("new_game", new_game))
app.add_handler(CommandHandler("game", game))
app.run_polling()

 



from config import TOKEN
import requests
import logging
APScheduler==3.6.3
cachetools==4.2.2
certifi==2022.9.24
charset-normalizer==2.1.1
idna==3.4
isOdd==0.1.2
python-telegram-bot==13.12
pytz==2022.4
pytz-deprecation-shim==0.1.0.post0
requests==2.28.1
six==1.16.0
tornado==6.2
tzdata==2022.4
tzlocal==4.2
urllib3==1.26.12



pip install -r requirements.txt



import requests
import logging
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


# from dotenv import 
# load_dotenv, find_dotenv
# load_dotenv(find_dotenv())  другой способ хранения ключа не в программе папка .env добавляется в gitignor



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
update.message.text)

logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
if __name__ == '__main__':



# Определяем константы этапов разговора
CHOICE, RATIONAL_ONE, RATIONAL, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, COMPLEX_TWO = range(8)
    

# функция обратного вызова точки входа в разговор

API_URL = 'https://7015.deeppavlov.ai/model'



# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')



# app.add_handler(CommandHandler("start", help))


dispatcher = updater.dispatcher
dispatcher.add_handler(conversation_handler)




# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from telegram import Update   другие библиотеки

pip install python-telegram-bot --pre

python-telegram-bot==20.0a4

pip install python-telegram-bot --upgrade

app = ApplicationBuilder().token(TOKEN).build()







import requests
import logging
from config import TOKEN
# from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update


from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)

CHOICE, RATIONAL_ONE, RATIONAL, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, COMPLEX_TWO = range(8)
API_URL = 'https://7015.deeppavlov.ai/model'

def start():
    print('hello')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    
async def ask_wikipedia_question(question):
    API_URL = 'https://7012.deeppavlov.ai/model'
    data = {'question_raw':  [question]}
    res = requests.post(API_URL, json=data, verify=False).json()
    return res[0][0]

async def request_sentiment(message):
    data = {'x': [message]}
    res = requests.post(API_URL, json=data).json()
    santiment = res[0][0]
    # return santiment
    await Update.message.reply_text(santiment)

app = ApplicationBuilder().token(TOKEN).build()



app.add_handler(CommandHandler("start", help))
app.add_handler(CommandHandler("sentiment", request_sentiment))
app.run_polling()

# dispatcher = updater.dispatcher
# dispatcher.add_handler(conversation_handler)


# if __name__ == '__main__':





# Создайте программу для игры в ""Крестики-нолики"".

import telebot
from telebot import types

TOKEN = "5501756584:AAEw3bT6QibRgjGBP1enKb5diEZXmRVMfmU"
bot = telebot.TeleBot(TOKEN)

pole = list(range(1, 10))
player = 'X'
win_komb = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

@bot.message_handler(commands=['start'])
def bot_pole(message):
    bot.send_message(message.chat.id, draw_pole() )
    
    

@bot.message_handler(content_types=['text'])
def bot_message(message, pole=pole):
    global player
    hod = message.text
    if  hod not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        bot.send_message(message.chat.id,'Введите верный номер клеточки для хода')
    else:
        hod = int(hod)
        if str(pole[hod-1]) in 'XO':
            bot.send_message(message.chat.id, 'Клетка занята, выберите другую')
        else:
            pole[hod-1] = player
            bot.send_message(message.chat.id, draw_pole() )
            if player == 'X':
                player = 'O'
            else:
                player = 'X'


def draw_pole(): # функция отрисовки игрового поля
    new_pole = '-------------\n'
    for i in range(3):
        new_pole += '| ' + str(pole[0 + i*3]) + ' | ' +  str(pole[1 + i*3]) + ' | ' + str(pole[2 + i*3]) + ' |\n'
    new_pole +='-------------'
    return new_pole

def take_hod(hod, pole=pole): # фукнция хода игрока
    while True:
        # hod = input('Куда поставить ' + player + ' ? ')
        if  hod not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # print('Введите вереый номер клеточки для хода')
            continue
        hod = int(hod)
        if str(pole[hod-1]) in 'XO':
            # print('Клетка занята, выберите другую')
            continue
        pole[hod-1] = player
        break
    


def check_win(): # функция проверка на выигрыш
    for elem in win_komb:
        if pole[elem[0]] == pole[elem[1]] == pole[elem[2]]:
            return pole[elem[0]]
    else:
        return False

# def game(): # функция самой игры и смены ходов
#     a = 0
#     while True:
#         if a % 2 == 0: 
#             bot_message()
#             take_hod('X')
#         else:
#             take_hod('O')
#         if a > 3:
#             win = check_win()
#             if win:
#                 # os.system('cls')
#                 draw_pole()
#                 print(win, 'Выиграл!!!')
#                 break
#         a += 1
#         if a > 8:
#             # os.system('cls')
#             draw_pole()
#             print('Ничья!!')
#             break
# game()

bot.polling()




https://github.com/BlackStoneShadow/Python/tree/main/Lesson10/Task1





import telebot
from telebot import types

TOKEN = " "
bot = telebot.TeleBot(TOKEN)

value = ''
old_value = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
             telebot.types.InlineKeyboardButton('C', callback_data='C'),
             telebot.types.InlineKeyboardButton('<=', callback_data='<='),
             telebot.types.InlineKeyboardButton('/', callback_data='/'))
keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('*', callback_data='*'))
keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5', callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),
             telebot.types.InlineKeyboardButton('-', callback_data='-'))
keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton('+', callback_data='+'))
keyboard.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
             telebot.types.InlineKeyboardButton('0', callback_data='0'),
             telebot.types.InlineKeyboardButton(',', callback_data='.'),
             telebot.types.InlineKeyboardButton('=', callback_data='='))


@bot.message_handler(commands=['calc'])
def getMessage(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id,
                         '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id,
                         value, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data
    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value)-1]
    elif data == '=':
        value = str(eval(value))
    else:
        value += data
    if value != old_value:
        if value == '':
            bot.edit_message_text(
                chat_id=query.message.chat.id, message_id=query.message.id, text='0', reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id,
                                  message_id=query.message.id, text=value, reply_markup=keyboard)
        old_value = value


bot.polling()

