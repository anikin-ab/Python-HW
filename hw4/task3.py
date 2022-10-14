# Задайте последовательность чисел. Напишите программу,
# которая выведет список
# неповторяющихся элементов исходной последовательности.
import random

num = int(input("input num: "))
list2 = [random.randint(1, 6) for i in range(0, num) if num > 1]
print(list2)

list3 = []
for i in range(num):
    if list2.count(list2[i]) == 1: # если элемент встречается только 1 раз, заносим его в список3
        list3.append(list2[i])
print(list(list3))

