# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные 

# my_str = 'Привет участнабвикам соревнованийабв абви зрителям!'
# my_str = list(filter(lambda x: 'абв' not in x, my_str.split()))
# my = " ".join(my_str)  
# print(my)


# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# i = '1 2 3 4  5 6'
# result = list(map(int, i.split()))
# print(max(result), min(result))


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Упрощенный
# n = [1,2,3,4,5,6]
# result = list(map(lambda x: x if x%2 == 0 else None, n))
# result = [i for i in result if i!= None]
# result = reduce(lambda x,y: x + y, result)
# print(result)



#Задайте последовательность чисел. 
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# my_list = [i for i in np.random.uniform((10, 10, 6, 7,10, 10))]
# print(my_list)
# result_list = list(map(lambda i: round(i % 1, 2) if i %1 != 0 else None, my_list))
# result_list = [i for i in result_list if i != None]
# print(max(result_list) - min(result_list))