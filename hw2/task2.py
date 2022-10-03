# 2. Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.

num = int(input("input N:"))
list_num = [] #задаем пустой список
def fact(num): #пишем метод вычисления факториала
    if num == 1:
        return num
    return num * fact(num -1)

for i in range(1, num +1): 
    list_num.append(fact(i)) #заполняем список значениями функции
print(list_num)

