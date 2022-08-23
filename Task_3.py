# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
# 0.001 -> 3.142
# 0.00001 -> 3.14159

import math


def find_numbers_of_pi(user_number: str):
    return len(user_number) - 2


print('Программа высчитывает число "pi" с заданной точностью')
number = input('Введите точность расчета в виде вещественного числа: ')
print(f'π = {round(math.pi, find_numbers_of_pi(number))}')
