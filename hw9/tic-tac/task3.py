# Создайте программу для игры в ""Крестики-нолики"".

import random

print("игроки P1 and P2:")
print()


# sweets = int(input("напишите количество конфет: ")) #всего конфет
# max_sweets = 28 #сколько можно взять за раз
count = 0
FirstP = random.randint(0, 1) #определяем, кто первый ходит
print(f"жребий = {FirstP}")
SecondP = 0
if FirstP == 0:
    print(f"первым ходит P1")
    SecondP = 1
    count = 1
else:
    print(f"Первым ходит P2")

P1 = FirstP + 1
P2 = SecondP + 1

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j], end=" ")
    print()

go_count = 0
X = "X"
O = "O"
win_listXi = []
win_listOi = []
win_listXj = []
win_listOj = []

list2 = [[X, X, X], [X, 0, X], [0, 0, 0]]
list3 = [[0, 0, 0], [X, X, X], [X, 0, X]]
list4 = [[X, 0, X], [0, 0, 0], [X, X, X]]

while go_count != 7:
    if count % 2 == 0:
        num = int(input(f" P{P1} ставь X на цифре №:"))# подставляем первого игрока
        for i in range(len(list1)):
            for j in range(len(list1[i])):
                if list1[i][j] == num:
                    list1[i][j] = "X"
                print(list1[i][j], end=" ")
            print()
    else:
        num = int(input(f" P{P1} ставь O на цифре №:"))# подставляем second игрока
        for i in range(len(list1)):
            for j in range(len(list1[i])):
                if list1[i][j] == num:
                    list1[i][j] = "O"
                print(list1[i][j], end=" ")
            print()
    # чередуем игроков
    if count % 2 == 0:
        P1 = 1
    else:
        P1 = 2
    count += 1

    go_count += 1

for i in list1:
    print(i)

# определяем победителя

for i in range(len(list1)):
    for j in range(len(list1[i])):

        if (list1[i][j] == list2[i][j] == "X"
                or list1[i][j] == list3[i][j] == "X"
                or list1[i][j] == list4[i][j] == "X"):
            win_listXj.append(j)
            win_listXi.append(i)
            print(f" X is {i}, {j}")
            # count_X += 1
# НЕ РАБОТАЕТ ЭТОТ МОДУЛЬ, в task3-1 он работает
        elif (list1[i][j] == list2[i][j] == "O"
                or list1[i][j] == list3[i][j] == "O"
                or list1[i][j] == list4[i][j] == "O"):
            win_listOj.append(j)
            win_listOi.append(i)
            print(f" 0 is {i}, {j}")

        # else:
        #     if (list1[i][j] == list2[i][j] == "O"
        #         or list1[i][j] == list3[i][j] == "O"
        #         or list1[i][j] == list4[i][j] == "O"):
        #         win_listOj.append(j)
        #         win_listOi.append(i)
        #         print(f" 0 is {i}, {j}")
        #     # count_0 += 1
print("win list all:")
print(win_listXi)
print(win_listXj)
print(win_listOi)
print(win_listOj)
# print(win_list0)

a = 0
b = 0
a1 = 0
b1 = 0
# count(x) Возвращает количество элементов со значением x
for k in range(0, 3):
    if win_listXi.count(k) >= 3 or win_listXj.count(k) >= 3:
        print("X true")
        a = win_listXi.count(k)
        b = win_listXj.count(k)
print(f"win X {a}, {b}")

for k in range(0, 3):
    if win_listOi.count(k) >= 3 or win_listOj.count(k) >= 3:
        print("O true")
        a1 = win_listOi.count(k)
        b2 = win_listOj.count(k)
print(f"win O {a1}, {b1}")

# for k in range(0, 3):
#     if win_list0.count(k) >= 3:
#         print("you win2 0")

    # # go_count += 1
    # if go_count == 9:
    #     print(f"\n*** выиграл игрок №{P1} ***")
