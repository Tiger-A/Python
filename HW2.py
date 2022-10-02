# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input("Input number - ")
# if float(number) < 0:
#     number = float(number) * (-1)  
# sum_digit_in_number = 0
# for i in str(number):
#     if i != '.':
#         sum_digit_in_number += int(i)
# print("Sum_digit_in_number - ", sum_digit_in_number)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input("Input number - "))
# set_of_products_of_numbers = []
# a = 1
# for i in range (1, number+1):
#     a = a * i
#     set_of_products_of_numbers.append(a)
# print(set_of_products_of_numbers)

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# print("Input N - ")
# while True:
#     try:
#         n = int(input())
#     except ValueError:
#         print("This is not number, try again: ")
#     else:
#         break
# numbers = {}
# for i in range (1,n+1):
#      numbers[i] = round((1 + 1/i)**i) 
# print(numbers)    

# sum_of_numbers = 0
# for item in numbers:
#     sum_of_numbers += numbers[item] 

# print('Sum_of_numbers', sum_of_numbers)


# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

import random

print("Input N - ")
while True:
    try:
        n = int(input())
    except ValueError:
        print("This is not number, try again: ")
    else:
        break

set_of_numbers = []
for i in range (-n, n+1):
 
    set_of_numbers.append(i)
print(set_of_numbers)

print("Input first position - ")
while True:
    try:
        first_position = input()
    except ValueError:
        print("This is not number, try again: ")
    else:
        break

print("Input second position - ")
while True:
    try:
        second_position = input()
    except ValueError:
        print("This is not number, try again: ")
    else:
        break

with open('file.txt', 'w') as data:
    data.write(first_position)
    data.write("\n")
    data.write(second_position)
  
data = open('file.txt', 'r')
data_list = [int(line.strip()) for line in data]
data.close()
print(data_list)
product_of_numbers = set_of_numbers[data_list[0]] * set_of_numbers[data_list[1]]
print("Product of numbers in positions = ", product_of_numbers)

random.shuffle(set_of_numbers)
print("Mixed set", set_of_numbers)