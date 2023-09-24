# сортировка выбором


from random import randint
n = 10
data = []
for i in range (n):
    data.append(randint(1, 99))
print(data)


# def vibor (lst):
#     n = len(lst)
#     i = 0 
#     while i < n - 1:
#         m = i
#         j = i + 1 
#         while j < n:
#             if lst[j] < lst[i]:
#                 m = j
#             j += 1
#         lst[i], lst[m] = lst[m], lst[i]
#         i += 1
#     return lst

# vibor(data)



# сортировка пузырьком
# 1 вариант

# from random import randint
# n = 10
# data = []
# for i in range (n):
#     data.append(randint(1, 99))
# print(data)

# def bubble_for(lst):
#     n = len(lst)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst
# bubble_for(data)

# 2 вариант

# from random import randint
# n = 10
# data = []
# for i in range (n):
#     data.append(randint(1, 99))
# print(data)

# def bubble_while(lst):
#     n = len(lst)
#     i = 0
#     while i < n - 1:
#         j = 0
#         while j < n - i - 1:
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#             j += 1
#         i += 1
#     return lst

# bubble_while(data)
                
# стандартная сортировка

# from random import randint
# n = 10
# data = []
# for i in range (n):
#     data.append(randint(1, 99))
# print(data)

# def default(lst):
#     lst.sort()
#     return lst
# default(data)

# from random import randint
# n = 10
# data = []
# for i in range (n):
#     data.append(randint(1, 99))
# print(data)

# def default(lst):
#     lst.sort()
#     return lst
# default(data)

# сортировка вставкой



def insertion(lst):
    for i in range(len(lst)):
        j = i - 1
        key = lst[i]
        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst
insertion(data)





