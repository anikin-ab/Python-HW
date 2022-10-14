# Задана натуральная степень k. Сформировать случайным
# образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

num = int(input("input num: "))
list2 = [random.randint(0, 10) for i in range(0, num + 1) if num > 1]
print(list2)

k = [i for i in range(1, num + 1) if num > 1]
# print((k[::-1]))
b = (k[::-1]) # преобразуем обратную последовательность элементов
# print(" ".join(map(str, b))) #преобразуем список в строку

eql = "" # уравнение
for i in range(num + 1):
    if list2[i] == 0:
        continue
    elif i < (num):
            eql = eql + " " + str(list2[i]) + "x" + "^" + str(b[i]) + " " "+"
    elif i == (num):
        eql = eql + " " + str(list2[i])
print(f"{eql} = 0")


new_file = open("eql.txt", "w+")
new_file.write(f"{eql} = 0")
new_file.close()

# eql = "" # уравнение
# for i in range(num + 1):
#     if list2[i] == 0:
#         continue
#     if i < (num - 1):
#             eql = eql + " " + str(list2[i]) + "x" + "^" + str(b[i]) + " " "+"
#     elif i == (num - 1):
#         eql = eql + " " + str(list2[i])
# print(f"{eql} = 0")

# new_file = open("mnogochlen.txt", "w+")
# new_file.write(f"{eql} = 0")
# new_file.close()

# new_file = open("mnogochlen.txt", "r+")
# read_f = new_file.read()
# print(f" Данные из файла {read_f}")
# print(read_f)
