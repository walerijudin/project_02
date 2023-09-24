# 1  генератор случайных чисел

import random
x = random.randint(10,50)
print(x)


# 2  выбор случайного значения из списка
import random
x = [0, 10, 25, 40, 100, "test1", "test2", [1, 2, 3]]
print("Случайное число из списка", random.choice(x))


import random
x = random.uniform(2.33, 2.99)
print(x)

# задача 1.
# написать алгоритм, где игральный кубик (6 сторонний) бросается 4 раза. 
# Вывести в результаты выпавшее число. Найти сумму выпавших значений
  
# вариант 1
import random
b1 = random.randint (1, 6)
print(b1)
b2 = random.randint (1, 6)
print(b2)
b3 = random.randint (1, 6)
print(b3)
b4 = random.randint (1, 6)
print(b4)
total = b1 + b2 + b3 + b4
print('Itog', total)

# вариант 2
import random
k = 4
y = []
total = 0
while k !=0:
    x = random.randint(1,6)
    k -= 1
    y.append(x)
    print(y)
total = sum(y)
print('Itog', total)


import random
k = 4
y = []
total = 0
while k !=0:
    x = random.randint(1,6)
    k -= 1
    y.append(x)
    print(y)
for i in y:
    print('i =', i)
    total += i
    print('total = ', total)
print('Itog', total)



# Задача 2
# Написать алгоритм генератора случайных паролей из следующих символов
# +-/*!&$#?=@<>abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQXYZ

import random
chars = '+-/*!&$#?=@<>abcdef=ghijklnmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQXYZ'
length = input('Длина пароля: ')
password = ''

try:
    length = int(length)
    for n in range(length):
        password += random.choice(chars)
    print(password)
except ValueError:
    print('Вы ввели буквы, пожалуйста введите цифры')
finally:
    length = input('Длина пароля: ')
    length = int(length)
    for n in range(length):
        password += random.choice(chars)
    print(password)




