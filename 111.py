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







