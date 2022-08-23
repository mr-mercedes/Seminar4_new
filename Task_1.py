# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

def get_multipliers(user_number):
    result = []
    cur_number = user_number
    probe = 2
    while cur_number != 1:
        if cur_number % probe != 0:
            probe += 1
        else:
            cur_number /= probe
            result.append(probe)
    return result


number = int(input('Введите число для разложения на простые множители: '))
print(get_multipliers(number))
