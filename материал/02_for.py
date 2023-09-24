# Оператор цикла for
# приминение break, continue
room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]
for price in room_prices:
    if price == max(room_prices):
        continue

    if price == min(room_prices):
        print('Минимальная цена:', price)
        break
    print('Текущая цена:', price)

print('До свидания!')

# использование pass - пропустить ( когда не знаем, что писать внутри конструкции)
x = 4
if x > 0:
    pass
elif x < 4:
    pass
else:
    pass


# Задача 2
# Напишите код, который принимает список из чисел и возвращает сумму только положительных чисел в нём.

# Например, 
# [1, -4, 7, 12] -> 1 + 7 + 12 = 20

# Примечание:
# Если положительных чисел в списке нет, то сумма равна 0.

primes =[1, -4, 7, 12]

# Вариант 1 c while

# i = 0
# total = 0
# while i < len(primes):
#     if primes[i] >= 0:
#         total += primes[i]
#     i += 1
# print(total)

# # Вариант 2 c for

# total = 0
# for i in primes:
#     if i >= 0:
#         total += i
# print(total)

# # Вариант 3  индексы c for

# print (list(range(10)))

# # генерация последовательности чисел
# # print (list(range(1000, 10000)))

# total = 0
# for ind in range(len(primes)):
#     if primes[ind] >= 0:
#         total += primes[ind]
# print(total)


# Вариан 4 - функция enumerate()
total = 0
for ind, elem in enumerate(primes):
    print("Позиция элемента:", ind, "Элемент:", elem)
    if elem >= 0:
        total += elem
print(total)



