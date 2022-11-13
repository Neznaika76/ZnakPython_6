# Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!


# def izmenen1(x):
#     izm = " ".join(map(str, x))
#     izm = '"' + izm[0] + '0' + izm[2:] + '"'
#     print(izm)
#     return izm
#
# def izmenen2(x):
#     izm = "".join(map(str, x))
#     izm = '"' + izm[0:] + '"'
#     print(izm)
#     return izm
#
#
# array = ['+1', 'в', '5,1', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов', '-1']
# print(array)
# for a in range(len(array)):
#     for k in ',':
#         if k not in array[a]:
#             j = 0
#             for s in '0123456789':
#                 if s in array[a]:
#                     j += 1
#             if j == 1:
#                 array[a] = izmenen1(array[a])
#             elif j == 2:
#                 array[a] = izmenen2(array[a])
#
# print(array)

# Дан список, содержащий искажённые данные с должностями и именами
# сотрудников: ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
#               'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на
# экран фразы вида: 'Привет, Игорь!' Подумать, как получить имена сотрудников из
# элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?


def izmenen1(x):
    new = "Привет,  !"
    izm = "".join(map(str, x))
    izm = izm.lower()
    i = len(izm)-1
    j = 0
    while izm[i] != ' ':
        if izm[i-1] != ' ':
            new = new[0] + new[1] + new[2] + new[3] + new[4] + new[5] + new[6] + new[7] + new[8] + izm[i] + new[9:]
        else:
            new = new[:8] + izm[i].upper() + new[9:]
        i -= 1
        j += 1
    print(new)
    return izm


array = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(array)
for a in range(len(array)):
    array[a] = izmenen1(array[a])

