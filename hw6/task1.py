# 1 – Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#
# Пример:
#
# 2+2 => 4;
import numpy as np
import numexpr as ne



formula = input("input formula:")
print(formula)
formula = "".join(formula.split())

#вариант с numpy
res = ne.evaluate(formula)
print(f" res c numpy = {res}")

#ручной вариант без скобок

a = 0
b = 0
c = 0
d = 0
form = []
form_l = ""
count = 0


#если у нас число больше 10 то фомируем его как целое число из неск цифр
for i in formula:
    if i.isdigit():
        form_l += i
        count += 1
        if count == len(formula):
            form.append(form_l)
    else:
        form.append(form_l)
        form.append(i)
        form_l = ""
        count += 1

print(f" фомируем список {form}")
leng = len(form)

form2 = []

#печатаю формулы print(form) расчета для наглядности
# сначала считаем приоритетные выражения

#поиск скобок
sk1 = '('
sk2 = ")"


def mul_del(num):
    for i in range(0, leng):
        if form[i] == "*" or form[i] == "/":
            if form[i] == "*":
                c = int(form[i - 1]) * int(form[i + 1])
                print(f" {form[i - 1]} * {form[i + 1]} = {c}")
                form[i - 1] = 0
                form[i] = 0
                form[i + 1] = c
                print(form)

            elif form[i] == "/":
                d = int(form[i - 1]) / int(form[i + 1])
                print(f" {form[i - 1]} / {form[i + 1]} = {d}")
                form[i - 1] = 0
                form[i] = 0
                form[i + 1] = d
                print(form)


#печатаю формулы print(form2) расчета для наглядности
#считаем "упрощенный список"

def sum_dev(num2):
    for i in range(0, len(form2)):
        if form2[i] == "+":
            a = int(form2[i - 1]) + int(form2[i + 1])
            print(f" {form2[i - 1]} + {form2[i + 1]} = {a}")
            form2[i - 1] = 0
            form2[i] = 0
            form2[i + 1] = a
            print(form2)
        elif form2[i] == "-":
            b = int(form2[i - 1]) - int(form2[i + 1])
            print(f" {form2[i - 1]} - {form2[i + 1]} = {b}")
            form2[i - 1] = 0
            form2[i] = 0
            form2[i + 1] = b
            print(form2)

# sum_dev(form2)
# # добавляем скобки
# for i in formula:
#     if sk1 in i:
#         print("sk1")
#         mul_del(form)
#     elif sk2 in i:
#         print("sk2")
#         sum_dev(form2)

mul_del(form)
#из посчитанных формируем новый список без * и /
form2 = [form[i] for i in range(leng) if form[i] != 0]
print(f" form2  = {form2}")
sum_dev(form2)
print(f"результат = {sum(form2)}")



#### код ниже не актуалеn ####


# def numeric(equation): if
#
#
# '+' in equation: y = equation.split('+')
# x = int(y[0]) + int(y[1]) elif '-' in equation: y = equation.split('-')
# x = int(y[0]) - int(y[1])
# return x

# for i in range(0, leng):
#     if form[i] == "*" or form[i] == "/":
#         if form[i] == "*":
#             c = int(form[i - 1]) * int(form[i + 1])
#             print(f" {form[i - 1]} * {form[i + 1]} = {c}")
#             form[i - 1] = 0
#             form[i] = 0
#             form[i + 1] = c
#             print(form)
#
#         elif form[i] == "/":
#             d = int(form[i - 1]) / int(form[i + 1])
#             print(f" {form[i - 1]} / {form[i + 1]} = {d}")
#             form[i - 1] = 0
#             form[i] = 0
#             form[i + 1] = d
#             print(form)
#
# #из посчитанных формируем новый список без * и /
# form2 = [form[i] for i in range(leng) if form[i] != 0]
# print(f" form2  = {form2}")
#
# #печатаю формулы print(form2) расчета для наглядности
# #считаем "упрощенный список"
# for i in range(0, len(form2)):
#     if form2[i] == "+":
#         a = int(form2[i - 1]) + int(form2[i + 1])
#         print(f" {form2[i - 1]} + {form2[i + 1]} = {a}")
#         form2[i - 1] = 0
#         form2[i] = 0
#         form2[i + 1] = a
#         print(form2)
#     elif form2[i] == "-":
#         b = int(form2[i - 1]) - int(form2[i + 1])
#         print(f" {form2[i - 1]} - {form2[i + 1]} = {b}")
#         form2[i - 1] = 0
#         form2[i] = 0
#         form2[i + 1] = b
#         print(form2)
#
# print(f"результат = {sum(form2)}")



#Код ниже не актуален

# for i in range(0, len(form)):
#     if form[i] == "+":
#         a = int(form[i - 1]) + int(form[i + 1])
#         print(f" {form[i - 1]} + {form[i + 1]} = {a}")
#         form[i - 1] = 0
#         form[i] = 0
#         form[i + 1] = a
#         print(form)
#     elif form[i] == "-":
#         if form[i+1] == 0 and form[i +2] == 0:
#             form[i+1] = form[i+3]
#             form[i+3] = 0
#         b = int(form[i - 1]) - int(form[i + 1])
#         print(f" {form[i - 1]} - {form[i + 1]} = {b}")
#         form[i - 1] = 0
#         form[i] = 0
#         form[i + 1] = b
#         print(form)

# print(f"результат1 = {sum(form)}")

#Код ниже не актуален


# for i in range(0, leng):
#     if form[i] == "*" or form[i] == "/":
#         print(len(form))
#         if form[i] == "*":
#             c = int(form[i - 1]) * int(form[i + 1])
#             print(f" {form[i - 1]} * {form[i + 1]} = {c}")
#             form[i - 1] = 0
#             form[i] = 0
#             form[i + 1] = c
#             print(form)
#         elif form[i] == "/":
#             d = int(form[i - 1]) / int(form[i + 1])
#             print(f" {form[i - 1]} / {form[i + 1]} = {d}")
#             form[i - 1] = 0
#             form[i] = 0
#             form[i + 1] = d
#             print(form)
#
# for i in range(0, leng):
#         if form[i] == "+":
#             a = int(form[i - 1]) + int(form[i + 1])
#             print(f" {form[i - 1]} + {form[i + 1]} = {a}")
#             form[i - 1] = 0
#             form[i] = 0
#             form[i + 1] = a
#             print(form)
#         elif form[i] == 0: continue
#         elif form[i] == "-":


            # b = int(form[i - 1]) - int(form[i + 1])
            # print(f" {form[i - 1]} - {form[i + 1]} = {b}")
            # form[i - 1] = 0
            # form[i] = 0
            # form[i + 1] = b
            # print(form)

# print(f"сумма  = {sum(form)}")

# for i in form:
#     if i == "*" or i == "/":
#         if form[int(i)] == "*":
#             c += int(form[i - 1]) * int(form[i + 1])
#             print(f" {form[i - 1]} * {form[i + 1]} = {c}")
#             form[i - 1: i + 2] = [c]
#             print(form)
#
#         elif form[i] == "/":
#             d += int(form[i - 1]) / int(form[i + 1])
#             print(f" {form[i - 1]} / {form[i + 1]} = {d}")
#             form[i - 1: i + 2] = [d]
#             print(form)
#
#
# for i in range(1, len(form) - 1):
#
#     if form[i] == "*" or form[i] == "/":
#         if form[i] == "*":
#             c += int(form[i - 1]) * int(form[i + 1])
#             print(f" {form[i - 1]} * {form[i + 1]} = {c}")
#             form[i - 1: i + 2] = [c]
#             print(form)
#
#         elif form[i] == "/":
#             d += int(form[i - 1]) / int(form[i + 1])
#             print(f" {form[i - 1]} / {form[i + 1]} = {d}")
#             form[i - 1: i + 2] = [d]
#             print(form)
# #

# for i in range(0, len(form) - 1):
#     if form[i] == "*" or form[i] == "/":
#         print(len(form))
#         if form[i] == "*":
#             c += int(form[i - 1]) * int(form[i + 1])
#             print(f" {form[i - 1]} * {form[i + 1]} = {c}")
#             form[i - 1: i + 2] = [c]
#             print(form)
#         elif form[i] == "/":
#             d += int(form[i - 1]) / int(form[i + 1])
#             print(f" {form[i - 1]} / {form[i + 1]} = {d}")
#             form[i - 1: i + 2] = [d]
#             print(form)
#     else:
#         if form[i] == "+":
#             a += int(form[i - 1]) + int(form[i + 1])
#             print(f" {form[i - 1]} + {form[i + 1]} = {a}")
#             print(form)
#         elif form[i] == "-":
#             b += int(form[i - 1]) - int(form[i + 1])
#             print(f" {form[i - 1]} - {form[i + 1]} = {b}")
#             print(form)
#
# leng = len(form)
#
# for i in range(0, leng):
#     if form[i] == "*" or form[i] == "/":
#         if form[i] == "*":
#             c = int(form[i - 1]) * int(form[i + 1])
#             print(f" {form[i - 1]} * {form[i + 1]} = {c}")
#             form[i - 1] = 0
#             form[i] = 0
#             form[i + 1] = c
#             print(form)
#
#         elif form[i] == "/":
#             d = int(form[i - 1]) / int(form[i + 1])
#             print(f" {form[i - 1]} / {form[i + 1]} = {d}")
#             form[i - 1] = 0
#             form[i] = 0
#             form[i + 1] = d
#             print(form)
#
#
# for i in range(0, len(form)):
#     if form[i] == "+":
#         a = int(form[i - 1]) + int(form[i + 1])
#         print(f" {form[i - 1]} + {form[i + 1]} = {a}")
#         form[i - 1] = 0
#         form[i] = 0
#         form[i + 1] = a
#         print(form)
#     elif form[i] == "-":
#         if form[i+1] == 0 and form[i +2] == 0:
#             form[i+1] = form[i+3]
#             form[i+3] = 0
#         b = int(form[i - 1]) - int(form[i + 1])
#         print(f" {form[i - 1]} - {form[i + 1]} = {b}")
#         form[i - 1] = 0
#         form[i] = 0
#         form[i + 1] = b
#         print(form)
#
# print(f"результат1 = {sum(form)}")
# formS = a + b + c + d
# print(f"результат2 = {formS}")



# print(type(formula))

# for k in formula:
#     if operations in set(formula):
#         print("yes")


# def count(op, a, b):
#     print(f"{a}, {b} = {op(a, b)}")
# count(lambda x, y: x * 2 + y, 3, 7)
#
# count(lambda x, y: x * (2 + y), 3, 7)
#
# count(lambda x, y: x ** (2 + y), 5, 2)

