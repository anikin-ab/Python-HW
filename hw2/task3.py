#Задайте список из n чисел последовательности 
# (1 + 1 / n) ** n и выведите на экран их сумму.

num = int(input("input int n > 0:"))
sumN = 0.0
if num != 0:
    for i in range(1, num + 1):
        sumN = sumN + (1 + 1 / i) ** i
    print("sumN = ", sumN)
else: 
    print("False")
    
