# Задача №9
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 

# n = -1
# while n < 0:
#     n = int(input("Введите целое неотрицательное число: "))
# i = f = 1
# while i <= n:
#     f = int(f) * i
#     i += 1
# print(f"!n = {f}")

# Задача №11.
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# first = 0
# second = 1
# counter = 2 # у нас уже есть два числа
# a = 0
# while a < 2:
#     a = int(input("Введите целое число большее, чем 1: "))
# while a >= (first + second):
#     counter += 1
#     if a == (first + second):
#         print(counter)
#         break
#     temp = first
#     first = second
#     second = temp+first
# else:
#     print(-1)


# Задача №13.
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

n = counterCurrent = counterGlobal = int()
while n < 1 or n > 100:
    n = int(input("Введите целое положительное число от 1 до 100 включительно: "))
for day in range(n):
    temp = int(input(f"Введите среднесуточную температуру в {day+1}-й день: "))
    if temp > 0:
        counterCurrent += 1
    else:
        counterCurrent = 0
    if counterCurrent > counterGlobal:
        counterGlobal = counterCurrent
print(counterGlobal)

# Задача №15.
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# n = min = max = int()
# while n < 1:
#     n = int(input("Введите число арбузов: "))
# i = 1
# while i <= n:
#     x = int(input(f"Введите вес {i}-го арбуза: "))
#     if x > max:
#         max = x
#     elif x < min or min == 0:
#         min = x
#     i += 1
# print(min, max)
