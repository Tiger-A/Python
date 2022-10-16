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


# import random
# natural_degree = int(input('Input natural degree - '))
# rezult = ""
# for i in range(natural_degree, -1, -1):
#     koeficent = str(random.randint(0,100))
#     print(i,koeficent)
#     if koeficent != 0:
#         if i == 1:
#             rezult = rezult + str(koeficent)+ "*X" + "+"  
#         elif i == 0:
#             rezult = rezult + str(koeficent) + "=0"  
#         else: 
#             rezult = rezult + str(koeficent)+ "*X**" + str(i) + "+"
   
#     print(rezult)
# with open('file.txt', 'w') as data:
#  data.write(rezult)
#  data.close()


# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def write_file(name = '', mnogochlen= ""):
    with open(name, 'w') as data:
        data.write(mnogochlen) 
        data.close()

def read_file(name = ''):
    with open(name,'r') as file:
         mn_r = file.readline()
         return mn_r

write_file('file1.txt', '65*X**6+15*X**5+38*X**4+59*X**3+46*X**2+53*X+13=0')
write_file('file2.txt', '69*X**4+94*X**3+97*X**2+65*X+73=0')
mnogoclen1 = read_file('file1.txt')[:-2]
mnogoclen2 = read_file('file2.txt')[:-2]
sum_mnogochlenov = mnogoclen1 + "+" + mnogoclen2 + "=0"
write_file("sum_mnogochlenov.txt", sum_mnogochlenov)


