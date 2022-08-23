# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# 5x^2 + 3x
# 3x^2 + x + 8
# 8x^2 + 4x + 8


def read_file(track):
    with open(track, 'r') as file:
        data = file.read().split()
        data = list(map(str, data))
    return data


def parse_item(object_from_list):
    tmp = []
    for item in object_from_list:
        for i in range(len(item)):
            if item[i] == 'x' and not item[i - 1].isdigit():
                tmp.append("1")
                tmp.append(item[i])
            else:
                tmp.append(item[i])
    return tmp


def sum_of_multi(date1, date2):
    while len(date1) != len(date2):
        if len(date1) > len(date2):
            date2.append("0")
        else:
            date1.append("0")

    answer = ''
    for i in range(len(date1)):
        if date1[i].isdigit() and date2[i].isdigit() and date1[i - 1] != '^':
            answer += str(int(date1[i]) + int(date2[i]))
        elif date1[i].isdigit() and date1[i - 1] == '^':
            answer += date1[i]
        elif date1[i] == '0' or date2[i] == '0':
            if date1[i] == '0':
                answer += date2[i]
            elif date2[i] == '0':
                answer += date1[i]
        else:
            answer += date1[i]

    return answer


def write_file(data):
    with open('answer.txt', 'a', encoding='utf-8') as file:
        file.write(f"Сумма многочленов = {data}")


track_to_file1 = 'File1_to_Task5'
track_to_file2 = 'File2_to_Task5'
result = sum_of_multi(parse_item(read_file(track_to_file1)), parse_item(read_file(track_to_file2)))
write_file(result)
print(f"Сумма многочленов = {result}")
