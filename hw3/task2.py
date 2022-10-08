# Напишите программу, которая найдёт
# произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.

import random

num = int(input("input list length:"))
new_list = []
for i in range(num):
    new_list.append(random.randint(0, num))
print(list(new_list))

new_list1 = []
mult = 0
for k in range(num):
    while k < (num / 2):
        mult = new_list[k] * new_list[(- k - 1)]
        print(mult)
        k += 1
        new_list1.append(mult)
    if k >= (num / 2):
        break
print(list(new_list1))
