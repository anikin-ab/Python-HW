# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in list1:
#     print(i)
# print()
#
# # for i in range(0, 3):
# #     print(list1[i])
#
# num = int(input("ставь крестик на цифре №:"))
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         if list1[i][j] == num:
#             list1[i][j] = "X"
#         print(list1[i][j], end=" ")
#     print()
#
# num = int(input("ставь крестик на цифре №:"))
#
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         if list1[i][j] == num:
#             list1[i][j] = "O"
#         print(list1[i][j], end=" ")
#     print()

X = "X"

win_listX = []
win_list0 = []
win_listXi = []
win_listOi = []
win_listXj = []
win_listOj = []

list1 = [[0, 0, X], [X, 0, X], [X, X, 0]]


list2 = [[X, X, X], [X, 0, X], [0, 0, 0]]
list3 = [[0, 0, 0], [X, X, X], [X, 0, X]]
list4 = [[X, 0, X], [0, 0, 0], [X, X, X]]

# list5 = [[0, 0, X], [X, 0, X], [X, 0, X]]
# list6 = [[0, 0, X], [X, 0, X], [X, 0, X]]
# list7 = [[0, 0, X], [X, 0, X], [X, 0, X]]
# list8 = [[0, 0, X], [X, 0, X], [X, 0, X]]
# list9 = [[0, 0, X], [X, 0, X], [X, 0, X]]


# list3 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# list4 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# list5 = [[X, 0, 0], [X, X, 0], [X, 0, X]]

# for i in range(len(list1)):
#     if list1[i] == list3[i]:
#         print("yes")
count_X = 0
count_0 = 0
win_listX = []
win_list0 = []
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if (list1[i][j] == list2[i][j] == "X"
                or list1[i][j] == list3[i][j] == "X"
                or list1[i][j] == list4[i][j] == "X"):
            win_listX.append(j)

            print(f" X is {i}, {j}")
        if (list1[i][j] == list2[i][j] == 0
                or list1[i][j] == list3[i][j] == 0
                or list1[i][j] == list4[i][j] == 0):
            win_list0.append(j)
            print(f"\n 0 is {i}, {j}")
print(win_listX)
print(win_list0)


for k in range(0, 3):
    if win_listX.count(k) >= 3:
        print("you win")
for k in range(0, 3):
    if win_list0.count(k) >= 3:
        print("you win2")
