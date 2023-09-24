# импорт имен
# модуль app.py - стартовый запуск скрипта

# терминология:
# модуль - файл, в коором мы работаем и создаём. Модуль рассматривается, как самостоятельный объект в Python.
# пакет - папка с модулями, которая содержит __init__
# библиотека - набор пакетов и модулей. Например, Python Standart Library
# фреймворк

# импорт имён
# 1 просто импорт модуля
# практические примеры: import os, import sys
import functions

print(functions.sum_all(100, 20, 300))

# импорт с синонимом
# практические примеры: import pandas as pd, import numpy as np
import functions as f
print(f.sum_all(100, 20, 300))


# 3 импорт конкретного имени (осторожно, можно перекрыть имя)
# практический пример: from flask import Flask
from functions import sum_all

print(sum_all(100, 20, 300))




# импорт из пакета
# 1 просто импорт из пакета
# import my_package.module_2
# my_package.module_2.foo_2()

# 2 импорт с синонимом
# практический пример: import matplotlib.pyplot as plt

import my_package.module_2 as m2
m2.foo_2()


# 3 импорт напрямую из пакета
import my_package.subpackage as sp
sp.foo_3




# Что такое __name__?
print(__name__)   #__main__
print(f.__name__) # functions
#если модуль называется __main__, то он является исполняемым

# Запуск скрипта по имени модуля
if __name__ == "__main__":
    print("Запуск скрипта")
    print(f.sum_all(10, 20, 30))




#структура модуля
# 1 импорты (import os)
# 2 константы (PATH = "C:\Users\") -- лучше без них
# 3 функции (def func(par):)
# 4 классы (class Person:)
# 5 тело цикла-условия 
# переменные в модуле лучше не объявлять.
# переменные-свойства фиксируются в классах