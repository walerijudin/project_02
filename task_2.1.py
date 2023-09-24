# Задача 2.1. 

from datetime import datetime

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!



arr = [[4,6,2,1,9,63,-134,566], [-52, 56, 30, 29, -54, 0, -110], [42, 54, 65, 87, 0], [5]]

def vibor (lst):
    n = len(lst)
    i = 0 
    while i < n - 1:
        m = i
        j = i + 1 
        while j < n:
            if lst[j] < lst[i]:
                m = j
            j += 1
        lst[i], lst[m] = lst[m], lst[i]
        i += 1
    return lst


def bubble_for(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def bubble_while(lst):
    n = len(lst)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j += 1
        i += 1
    return lst

def default(lst):
    lst.sort()
    return lst


def minimum(arr):
    print(' минимальные значения')
    print('сортировка выбором')
    start_time = datetime.now()
    for lst in arr:
        print('минимальльное значение из списка', lst, vibor(lst)[0])
    end_time = datetime.now()
    print('продолжительность: {}' .format(end_time - start_time))

    print('сортировка пузырьком через for')
    start_time = datetime.now()
    for lst in arr:
        print('минимальльное значение из списка', lst, bubble_for(lst)[0])
    end_time = datetime.now()
    print('продолжительность: {}' .format(end_time - start_time))

    print('сортировка пузырьком через while')
    start_time = datetime.now()
    for lst in arr:
        print('минимальльное значение из списка', lst, bubble_while(lst)[0])
    end_time = datetime.now()
    print('продолжительность: {}' .format(end_time - start_time))

    print('сортировка стандартная')
    start_time = datetime.now()
    for lst in arr:
        print('минимальльное значение из списка', lst, default(lst)[0])
    end_time = datetime.now()
    print('продолжительность: {}' .format(end_time - start_time))




def maximum(arr):
    print('максимальные значения')
    print('сортировка выбором')
    start_time = datetime.now()
    for lst in arr:
        print('максимальное значение из списка', lst, vibor(lst)[0])
    end_time = datetime.now()
    print('продолжительность: {}' .format(end_time - start_time))

    print('сортировка пузырьком через for')
    start_time = datetime.now()
    for lst in arr:
        print('максимальное значение из списка', lst, bubble_for(lst)[0])
    end_time = datetime.now()
    print('продолжительность: {}' .format(end_time - start_time))

    print('сортировка пузырьком через while')
    start_time = datetime.now()
    for lst in arr:
        print('максимальное значение из списка', lst, bubble_while(lst)[0])
    end_time = datetime.now()
    print('продолжительность: {}' .format(end_time - start_time))

    print('сортировка стандартная')
    start_time = datetime.now()
    for lst in arr:
        print('максимальное значение из списка', lst, default(lst)[0])
    end_time = datetime.now()
    print('продолжительность: {}' .format(end_time - start_time))


def main ():
    print(minimum(arr))
    print(maximum(arr))

main()

