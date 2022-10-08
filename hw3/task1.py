
#1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random

num = int(input("input list length:"))
new_list = []
for i in range(num):
    new_list.append(random.randint(0, num))
print(list(new_list))

sum_k = 0
for k in range(num):
    if k % 2 != 0:
        sum_k += new_list[k]
print("sum of odd index = ", sum_k)
