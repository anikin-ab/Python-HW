# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# осуществляется делением числа на основание новой системы счисления до тех пор,
# пока в остатке не останется число меньшее основания новой системы счис­ления.
# Новое число записывается в виде остатков деления, начиная с последнего.


num = int(input("input num:"))
print(num)
n_bit = 0
newbit = ""
while num > 0:
    n_bit = str(num % 2)
    num = num // 2
    newbit = newbit + n_bit # записываем в строку остаток от деления
print(newbit[::-1]) #выводим реверсную строку

