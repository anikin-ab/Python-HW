# Задайте число.
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

num = int(input("input Num:"))

def fibo(numb):
    if numb == 0:
        return numb
    elif numb == 1:
        return numb
    else:
        return (fibo(numb - 1) + fibo(numb - 2))

def fibo2(numb):
    if numb == 0:
        return numb
    elif numb == 1:
        return numb
    else:
        return (fibo2(numb + 2) - fibo2(numb + 1))

new_list = []
for i in range(1, num + 1):
    new_list.append(fibo(i))
# print(list(new_list))
new_list2 = []
for j in range(num + 1):
    new_list2.insert(- j - 1, fibo2(- j))
# print(list(new_list2))


print(new_list2 + new_list) # объединяем списки

# чужое решение
n = int(input("input Num:"))
def fib(n):
if not n:
return 0 # n
if n < 0:
return (-1) ** (-n + 1) * fib(-n)
if n in (1, 2):
return 1
return fib(n - 1) + fib(n - 2)


neg_fib = []
for i in range(-N, N + 1):
neg_fib.append(fib(i))

print(neg_fib)

