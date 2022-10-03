# 5. Реализуйте алгоритм перемешивания списка.

import random 


num = int(input("input N: "))
list_num = []
for i in range(num):
    list_num.append(random.randint(-num, num + 1))
print(list_num)

def new_list(list_num): # тоже не возвращает значение, пишет None
    new_list1 = random.shuffle(list_num)
    return new_list1
print(new_list(list_num)) #пишет None

# all done