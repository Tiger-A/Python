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

number = int(input("Input number - "))
set_of_products_of_numbers = []
for i in range (1, number+1):
    
    set_of_products_of_numbers.append(i)

print(set_of_products_of_numbers)






# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.



