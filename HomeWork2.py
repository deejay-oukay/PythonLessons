# Задача 10:
# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# n = -1
# while (n < 0):    # корректно работает и при нуле монет :-)
#     n = int(input("Введите корректное число монет: "))
# print("Если орёл, введите \"0\". Если решка, введите \"1\"...")
# eagles = int()
# if n > 1:    # оптимизация для работы с одной монетой :-)
#     for coin in range(n):
#         coin = int(input(f"Для {(coin+1)}-й монеты: "))
#         if coin == 1:
#             eagles += 1
#         # проверки на равенство 0 нет
# print('Нужно перевернуть монет:', (n-eagles, eagles)[eagles < (n-eagles)])

# Задача 12:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# S = P = 0
# while (S < 2):    # не может быть меньше 2 (1+1)
#     S = int(input("Петя, чему равна сумма чисел? "))
# while (P < 1):    # не может быть меньше 1 (1*1)
#     P = int(input("Петя, чему равно произведение чисел? "))
# # аналогично можно найти и сумму, но Катя решила, что произведение так найдётся быстрее
# for i in range(1,int(P/2)+1):
#     for j in range(1,S-i+1):
#         print(f"Катя проверяет {i} и {j}")
#         if ((P/i) == j) and ((S-j) == i):
#             print("Катя нашла верный ответ :)")
#             # не уверен, что это корректное принудительное завершение программы
#             import sys
#             sys.exit()
# else:
#     print("Петя где-то ошибся :(")

# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

N = int()
while (N < 1):
    N = int(input("Введите число N: "))
if N == 1:
    print(1,2)
else:
    for k in range(int(N**0.5)+1):
        if (2 ** k) <= N:   # при небольших числах работает без этой проверки
            print(2 ** k)
        
