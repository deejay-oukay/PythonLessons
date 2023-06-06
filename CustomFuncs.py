# Возвращает число Фибоначии с указанным номером (нумерация от нуля)
def LastFibo(n):
    if n in [0,1]:
        return n
    return LastFibo(n-1) + LastFibo(n-2)

# Если число является простым (делится только на себя и на 1),
# то возвращает "yes", иначе - "no"
def IsSimpleNumber(number):
    counter = 0
    for i in range(2,number+1):
        if number % i == 0:
            counter += 1
        if counter > 2:
            return "no"
    return "yes"

# Формирует список чисел и возращает его обратном порядке
def Reverse(number):
    print(number, end=" ")
    if number > 0:
        Reverse(number-1)

# Возводит число base в степень degree (рекурсивно)
def Exponentiation(base,degree):
    if degree == 0:
        return 1
    return base * Exponentiation(base,degree-1)

# Складывает числа A и B, используя только операции +1 и -1
def SumWithPlusOrMinus(A,B):
    if A == 0:
        return B
    return SumWithPlusOrMinus(A-1,B+1)