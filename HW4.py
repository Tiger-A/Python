# Урок 4. Данные, функции и модули в Python. Продолжение
# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from cmath import sqrt
# import math
# d = input('Input accuracy Pi 10^{-1} ≤ d ≤10^{-10} - ')
# pi_round = round(math.pi, len(d) - 2) 
# print(pi_round)


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# number = int(input('Input natural number - '))
# prime_factors = []
# for i in range(2, int(number/2)+1):
#     while number/i == int(number/i):
#            prime_factors.append(i)
#            number /=i         
    
# print('prime_factors - ', prime_factors)


# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# numbers = [1, 2, 2, 7, 8, 8]
# print(numbers)
# unique = []
# unique =list(set(numbers))
# print(unique)


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0      или x² + 5 = 0 или     10*x² = 0
import random
natural_degree = int(input('Input natural degree - '))

with open('file.txt', 'w') as data:
 data.write('line 1\n')
 data.write('line 2\n')
data.close()

r = random.randint(0,100)



# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.