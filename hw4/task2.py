# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

num = int(input("input Num > 1:"))
simpl_n = [1, 3, 5, 7]
spis = ""
num2 = num
number = "1"
for i in range(2, num + 1):
    if num2 % i == 0:
        while num2 % i == 0:
            # print(f"для {i} =  {num2}")
            spis = spis + str(i) + " "
            num2 = num2 / i
        # if i < num:
        #     print(f"список простых множителей = {spis}")
        if i == num:
            print(f"{i} это простое число")
print(f"список простых множителей числа {num} = {spis}")

