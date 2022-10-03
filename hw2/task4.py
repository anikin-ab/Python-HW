# 4. Задайте список из N элементов, заполненных числами
#  из промежутка [-N, N]. Найдите произведение элементов на
#  указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
import random 


num = int(input("input N > 100: "))
list_num = []
for i in range(num):
    list_num.append(random.randint(-num, num + 1))
print(list_num)
print()
if num >= 100:
    mult_num = 1
    path = "file.txt"
    data = open(path, 'r')
    for k in data:
        mult_num = mult_num * (list_num[int(k)])
    print("mult = ", mult_num)
    data.close()
elif num < 11:
    mult_num2 = 1
    path2 = "file2.txt"
    data2 = open(path2, 'r')
    for m in data2:
        mult_num2 = mult_num2 * (list_num[int(m)])
    print("mult = ", mult_num2)
    data2.close()
else:
    print("wrong num")


