# Задача 2. В первой строке файла находится информация об ассортименте мороженного,
# во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»


def read_file():
    data_assortment = []
    data_stock = []
    with open('assortment.txt', 'r', encoding='utf-8') as file:
        data_assortment = file.readlines(1)
        data_stock = file.readlines(2)

    return data_assortment, data_stock


def convert_to_set(data):
    tmp = []
    for item in data:
        if '\n' in item:
            item = item.replace('\n', '')
            tmp += item.split(', ')
        else:
            tmp += item.split(', ')

    data = set(tmp)
    return data


assortment, stock = read_file()
assortment = convert_to_set(assortment)
stock = convert_to_set(stock)
result = assortment.difference(stock)
print(result)
