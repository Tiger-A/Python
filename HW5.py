# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".




# my_str = 'Привет участнабвикам соревнованийабв абви зрителям!'.split()
# res = [word for word in my_str if 'абв' not in word]
# print(' '.join([word for word in my_str if 'абв' not in word]))


# my_str = 'Привет участнабвикам соревнованийабв абви зрителям!'
# my_str = list(filter(lambda x: 'абв' not in x, my_str.split()))
# my = " ".join(my_str)  
# print(my)





# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""



# from random import randint
# import os
# os.system('cls')


# def checking_input(name):
#     n = (
#         input(f'\n{name}, введите количество конфет, которое возьмете от 1 до 28: '))
#     while not n.isdigit():
#         n = (
#             input(f'{name}, введите корректное количество конфет: '))
#     n = int(n)
#     os.system('cls')
#     return (n)


# def input_dat(name):
#     x = checking_input(name)
#     while x < 1 or x > 28:
#         x = checking_input(name)
#     return x


# def input_bot(name):
#     if counter1 == 0:
#         k = randint(1, 28)
#     else:
#         k = 29 - includ
#     return k


# def motion_print(name, k, counter, value):
#     print(
#         f'Ходил {name}, он взял {k} конфет, теперь у него {counter} конфет. Осталось на столе {value} конфет.')


# print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
# input('\nДля начала игры нажмите "Ввод"')
# os.system('cls')
# player1 = input('Введите имя первого игрока: ')
# player2 = input(
#     '\nВведите имя второго игрока, или введите Бот для игры с ботом: ')

# if player2 == 'Бот':
#     player3 = player2
# value = int(input('Введите количество конфет на столе(2021): '))
# counter1 = 0
# counter2 = 0
# counter3 = 0
# includ = 0
# print('\nКоличество конфет на столе:', value)
# flag = randint(0, 2)  # флаг очередности
# if flag:
#     print(f'Первый ходит {player1}')
# elif flag and player2 == 'Бот':
#     print(f'Первый ходит {player3}')
# else:
#     print(f'Первый ходит {player2}')

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         includ = k
#         flag = False
#         motion_print(player1, k, counter1, value)
#     elif player2 == 'Бот':
#         k = input_bot(player3)
#         counter3 += k
#         value -= k
#         flag = True
#         motion_print(player3, k, counter3, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         motion_print(player2, k, counter2, value)

# if flag:
#     print(f'Выиграл {player1}')
# else:
#     print(f'Выиграл {player2}')






# Создайте программу для игры в ""Крестики-нолики"".





# def field(moves):
#     y0 = f"    X1    X2   X3  "
#     y1 = f"Y1  {moves['y1']['x1']}  |  {moves['y1']['x2']}  | {moves['y1']['x3']}  "
#     y1_1 = "  -----+-----+-----"
#     y2 = f"Y2  {moves['y2']['x1']}  |  {moves['y2']['x2']}  | {moves['y2']['x3']}  "
#     y1_1 = "  -----+-----+-----"
#     y3 = f"Y3  {moves['y3']['x1']}  |  {moves['y3']['x2']}  | {moves['y3']['x3']}  "
#     print(y0)
#     print(y1)
#     print(y1_1)
#     print(y2)
#     print(y1_1)
#     print(y3)

# def check(move, moves):
#     if len(move) == 4:
#         if move[0].lower() == 'y' and move[2].lower() == 'x':
#             if move[1] in '123' and move[-1] in '123':
#                 if moves[move[:2]][move[-2:]] == ' ':
#                     return True
#                 else:
#                     print('Данная клетка уже занята.')
#             else:
#                 print('Введены недопустимые значения координат.')
#         else:
#             print('Вы ввели не допустимые оси координат')
#     else:
#         print('Введено недопустимое количество символов.')
#     print('Попробуйте ещё раз!')
#     return False

# def wins(moves):
#     if ((moves['y1']['x1'] == moves['y1']['x2'] == moves['y1']['x3']
#             or moves['y1']['x1'] == moves['y2']['x1'] == moves['y3']['x1']
#             or moves['y1']['x1'] == moves['y2']['x2'] == moves['y3']['x3'])
#             and moves['y1']['x1'] != ' '):
#         return moves['y1']['x1']
#     elif ((moves['y2']['x1'] == moves['y2']['x2'] == moves['y2']['x3']
#            or moves['y1']['x2'] == moves['y2']['x2'] == moves['y3']['x2']
#            or moves['y1']['x3'] == moves['y2']['x2'] == moves['y3']['x1'])
#           and moves['y2']['x2'] != ' '):
#         return moves['y2']['x2']
#     elif ((moves['y3']['x1'] == moves['y3']['x2'] == moves['y3']['x3']
#            or moves['y1']['x3'] == moves['y2']['x3'] == moves['y3']['x3'])
#           and moves['y3']['x3'] != ' '):
#         return moves['y3']['x3']
#     return False


# def move(symbol, moves, player):
#     print('Текущий ход y{}x{}'.format(player[1], player[-1]))
#     if player[1] == '1':
#         if player[-1] == '1':
#             moves['y1']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y1']['x2'] = symbol
#         else:
#             moves['y1']['x3'] = symbol
#     elif player[1] == '2':
#         if player[-1] == '1':
#             moves['y2']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y2']['x2'] = symbol
#         else:
#             moves['y2']['x3'] = symbol
#     else:
#         if player[-1] == '1':
#             moves['y3']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y3']['x2'] = symbol
#         else:
#             moves['y3']['x3'] = symbol
#     return moves


# moves_out = {
#     'y1': {'x1': ' ', 'x2': ' ', 'x3': ' '},
#     'y2': {'x1': ' ', 'x2': ' ', 'x3': ' '},
#     'y3': {'x1': ' ', 'x2': ' ', 'x3': ' '}
# }

# field(moves_out)

# number_players = int(input('Введите количество игроков (1/2): '))
# count_move = 0

# if number_players == 2:
#     win = False
#     while not win and count_move < 9:
#         count_move += 1
#         player_out = input('Введите координаты хода(пример - y2x3): ')
#         while not check(player_out, moves_out):
#             player_out = input('Введите координаты хода(пример - y2x3): ')
#         if count_move % 2:
#             symbol_out = 'X'
#         else:
#             symbol_out = 'O'
#         moves_out = move(symbol_out, moves_out, player_out)

#         field(moves_out)
#         win = wins(moves_out)
#     if count_move == 9:   # баг может быть и победа на 9 ходу
#         print('Ничья!')
#     else:
#         print(f'На {count_move} ходу победили "{win}"')









# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.



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
# фунц декод
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
# Вод текста
text = input("Enter a text: ")
# Определение код/декод
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

