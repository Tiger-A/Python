# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = [2, 3, 5, 9, 3]
# print (my_list)
# sum_of_numbers = 0
# i = 1
# while i < len(my_list):
#     sum_of_numbers += my_list[i]
#     i += 2
# print(sum_of_numbers)


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# my_list = [2, 3, 4, 5, 6, 7, 8, 4, 9]
# print(my_list)
# i = 0
# products_of_numbers = []
# while i < int(len(my_list)/2)+1:
#     products_of_numbers.append(my_list[i] * my_list[(len(my_list)-i-1)])
#     i += 1   
# print(products_of_numbers)



# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my_list = [1.1, 1.2, 3.4, 5, 10.01]
# print (my_list)
# delta_of_numbers = 0
# i = 0
# max_num = 0.9999
# min_num = 0.0000
# while i < len(my_list):
#     print(my_list[i]%1)
#     if max_num > my_list[i]%1:
#           max_num = my_list[i]%1
#           print('max_num', max_num)
#     if min_num <  min_num:
#         min_num = my_list[i]%1
#         print("min", min_num)
#     i += 1
# print(delta_of_numbers)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# new_list = [num%1 for num in my_list if isinstnumbernce(num, flonumbert)]
# print(new_list)
# print(mnumberx(new_list)-min(new_list))




# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11

# print("Input number - ")
# while True:
#     try:
#         number = int(input())
#     except VnumberlueError:
#         print("This is not number, try numbergnumberin: ")
#     else:
#         brenumberk
# bin_number = bin(number)
# print(bin_number)  

# print("Input number - ")
# while True:
#     try:
#         number = int(input())
#     except VnumberlueError:
#         print("This is not number, try numbergnumberin: ")
#     else:
#         break
# bin_number = []
# while number:
#     bin_number.append(number % 2)
#     number //= 2
# bin_number.reverse()
# print(bin_number)


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
# (

print("Input number - ")
while True:
    try:
        number = int(input())
    except VnumberlueError:
        print("This is not number, try numbergnumberin: ")
    else:
        break
fibo_positive = [0, 1]
i = 2
while i <= number:
    # print(fibo_positive[i])
    print(fibo_positive[i-2])
    print(fibo_positive[i-1])
    fibo_positive[i] = fibo_positive[i-2] + fibo_positive[i-1]
    i += 1
print(fibo_positive)






