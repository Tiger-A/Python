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

from secrets import choice


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





1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    
    *Пример:*
    
    - 6782 -> 23
    - 0,56 -> 11


x = input('Введите число ')

def summa(x):                            
    if float(x) < 0:                          
        x = float(x) * (-1)
            number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number
   
print(f'Сумма чисел равна {summa(x)}')









2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    
    *Пример:*
    
    - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)



# N = int(input('Введите число '))

# f = 1
# for i in range(N):
#     i = i + 1 f = i * f
    
print(f, end=" ")
N = int(input('Введите число '))
f = 1
for i in range(N):
  i = i + 1
  f = i * f
print(f, end=" ")




можно вообще вот так
for i in range(2, n+1):
    lst.append(lst[i-2] * i)



N = int(input("Ввведите число: ")) # создаём переменную N и присваем ей целочисленные значения в соответствии с вводимым через клавиатуру пользователя числом. 
def factorial(N): # задаём функцию факториала переменной N
    a = 1 # создаём переменную a и присваем ей значение 1, исходя из условий задачи
    numbers = [] # cоздаём числовую переменную, где полученные значения будут отображаться в квадратных скобках
    for i in range (1, N+1): # пока переменная i находится в диапозоне от 1 до N+1, то
     a = a * i # создаём переменную а и присваем ей произведение предыдущей переменной а * на переменную i
    numbers.append(a) # к числовой переменной добавляем переменную а
    return numbers # делаем повтор числовой переменной
print(f'набор произведений чисел от 1 до N {factorial(N)}') # Выводим результат решения задачи








3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
    

# Задайте список из n чисел последовательности (1 + 1/n)**n
# и выведите на экран их сумму.



    *Пример:*
    
    - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}    пример с ошибкой !!!!

n = int(input('Введите количество чисел в списке '))

def numbers(n):
    summ = 0
    for i in range(n):
        a = int(input(f'Введи число {i + 1}: '))
        a = (1+1/a)**a
        summ = a + summ
        i += 1
    return summ

print('Сумма чисел равна',round((numbers(n)), 2))






def input_int(msg):
    while True:
        try:
            result = int(input(msg))
        except ValueError:
            print("Ошибка, повторите ввод: ")
        else:
            return result


def generate_list(n):
    result = []
    for i in range(1, n+1):
        result.append(round((1 + 1/i)**i))
    return result


n = input_int("Введите целое число: ")
number_list = generate_list(n)


print(f"Для n = {n}: {number_list} -> {sum(number_list)}")

нужно было сделать  ключ : значение

4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.



from random import randint

with open('17_Mult_task.txt', 'w') as data:
    data.write('0\n')
    data.write('1\n')
    data.write('5\n')
    data.write('8\n')
    data.write('10\n')

def get_numbers(n):
    return [randint(-n/2, n) for i in range(-n, n + 1)]

def get_data_from_file(path):
    data = open(path, 'r')
    dlist = [int(line.strip()) for line in data]
    data.close()
    return dlist

def get_mult(numbers, datalist):
    mult = 1
    for i in datalist:
        mult *= numbers[i]
    return mult

path = '17_Mult_task.txt'
n = 10 
datalist = get_data_from_file(path)
numbers = get_numbers(n)

print(numbers)
print(datalist)
print(get_mult(numbers, datalist))






from random import Random, randint

N = int(input('Введите число '))
numbers = []
for i in range(N):
    numbers.append(randint(-N,N+1))
print(numbers)

def smes(numbers):
    list = numbers[:]
    numbers_length = len(list)
    for i in range(numbers_length):
        index = randint(0, numbers_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list
print(smes(numbers))


надо  было сделать словарем

number = int(input('Ведите число: '))
list = []
for i in range(1, number+1):
    part = [i,round((1+1/i)**i)]
    list.append(part)
my_dict = dict(list)
my_sum = sum(my_dict.values())
print(f'Сумма последовательсности из {number} элементов {my_dict} равна: {my_sum}')


def is_int(number):
    return number.isdigit()

number = None

while not is_int(str(number)):
    number = input("Input number:")

number = int(number)

result = dict()
for i in range(1, number+1):
    result[i] = round((1 + 1 / i) ** i)

my_sum = 0
for i in result: 
    my_sum += result[i]

print(result, '->', my_sum)







5. Реализуйте алгоритм перемешивания списка



# алгоритм перетасовки Фишера–Йейтса
lst = [1, 2, 3, 4, 5]
print ('Исходный список :', lst)

for i in range(len(lst)-1, 0, -1):
    j = random.randint(0, i + 1)   # Берем случайный индекс  от 0 до i
    lst[i], lst[j] = lst[j], lst[i] # Меняем arr[i] с элементом случайеого индекса
     
print ('перемешаный список : ', lst)


Можно использовать метод choice
random import choice





1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

from time import time
print(f'Случайное число от 0 до 999 = {int(time() % 1 * 1000)}')

from time import time
my_time = time()
my_time %= 1
print(my_time)
# print(int((my_time % 1)*100))





2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

my_list = ["123","234", "12333", "567", "123"]
number = "123"
for i in my_list:
    if number in i: 
        print(i)
        print(my_list.index(i))


my_list = ["123","234", "12333", "567", "123"]
number = "123"
nul = 0
for elem in my_list:
    if number in elem: 
        print(elem)
        print(my_list.index(elem, nul))
        nul = my_list.index(elem, nul) + 1
        
my_list = ["123","234", "12333", "567", "123"]
number = "123"

for i, elem in enumerate(my_list):
    if number in elem: 
        print(elem)
        print(i)





3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

*Пример:*

- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1


my_list = ["123","234", "12333", "567", "123"]
number = "123"
n = 0
for i, elem in enumerate(my_list):
    if number == elem and n > 0:
        n += n
        print(n)
        print(i)






        my_list = ["123","234", "12333", "567", "123"]
number = my_list[0]
for i, elem in enumerate(my_list):
    if number == elem and i != 0:
        print(elem)
        print(i)

my_list = ["123","234", "12333", "567", "123"]
number = my_list[0]
for i in range(1, len(my_list)):
    if number == my_list[i]:
        print(i)

my_list = ["123","234", "12333", "567", "123"]
number = my_list[0]
print(my_list.index(number, 1))



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