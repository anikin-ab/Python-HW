# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

import random

num = int(input("input list length:"))
new_list = []
for i in range(num):
    new_list.append(round(random.uniform(0, 20), 2))
print(list(new_list))

dot = '.'
m = 0
i_num = 0
str1 = "Empty"
new_list2 = []
for number in new_list:
    str1 = str(number)
    str2 = "Empty"
    for m in range(len(str1)):
        if str1[int(m)] == dot:
            i_num = m
            str2 = str1[i_num + 1:]
            # print(str2)
    new_list2.append(int(str2))
print("список из остатков после . :", list(new_list2))


minN = new_list2[0]
maxN = new_list2[0]
for k in range(len(new_list2)):
    if new_list2[int(k)] > maxN:
        maxN = new_list2[int(k)]
    if new_list2[int(k)] < minN:
        minN = new_list2[int(k)]
print("max = ", maxN)
print("min = ", minN)
print("разница между макс и мин значение дробной части = ", maxN - minN)




