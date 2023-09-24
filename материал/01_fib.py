# Задача 1: последовательность Фибоначчи

# Чему равен 100 элемент?
# Вариан 1 - через while

fib1, fib2 = 1, 1

n = input('Номер элемента ряда Фибоначчи: ')
i = int(n) - 2

while i > 0:
    print(fib2)
    fib1, fib2 = fib2, fib1 + fib2
    i -= 1 

print('Значение этого элемента:', fib2)

# Вариан 2 - через for
for i in range(2, int(n)):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2)
