# модуль functions для функции

def divide(dividend: int, divisor: int) -> int:
    """
    Функция divide принимает делимое и делитель в качестве параметров.
    Возвращает целое частное.
    """

    quotient = 0

    while dividend > 0:
        dividend -= divisor
        quotient += 1 
   
    return quotient


def trapezoid_s(a, b, *, h=1):
    return h * (a + b) / 2


def sum_all(*args):
    # args - это кортеж
    total = 0
    for i in args:
        total += i
    return total