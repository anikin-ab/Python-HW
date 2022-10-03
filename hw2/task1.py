# Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр. Пример:

print("input float num: ")
num = float(input())
sumN = 0
while int(num) != num:
    num *= 10
while num % 10 != 0:
    sumN += num % 10 #суммируем остаток от деления
    num //= 10 # находим целое и отрбасываем остаток
print(f"sumN = {sumN}")

