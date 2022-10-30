# генерируем данные для справочника
import random
import string
from datetime import datetime as dt
from time import time

#формируем нумерацию
def id(x):
    return x

#формируем имена
def name_gen(x):
    return random.choice(name_list)

#формируем фамилии
def s_name_gen(x):
    return random.choice(sec_name_list)

#формируем телефоны
def tel(x):
    a = "8927"
    b = random.randint(1000000, 9999999)
    full_tel = a + str(b)
    return str(full_tel)


#список имен и фамилий

name_list = ["Василий", "Алексей", "Эдуард", "Светлана",
             "Марина", "Ольга", "Кирилл", "Олег"]
sec_name_list = ["Петров(а)", "Иванов(а)", "Гоголь", "Шпак",
                 "Мичурин(а)", "Малахов(а)", "Чернов(а)", "Лопатин(а)"]

print()



#генерируем список контактов
contact_list = []
con_spis = []

# main variant with list
def con_print(x):
    for i in range(0, x):
        contact_list.append([id(i), name_gen(i), s_name_gen(i), tel(i)]) # записываем контакты в словарь
        # можно сразу при формировании списка записывать его в файл
        # dir_export3(contact_list[i][0], contact_list[i][1], contact_list[i][2], contact_list[i][3])
        print(contact_list[i])
    # print(contact_list) # напечатать весь список контактов
    return contact_list


#second var with return
# NOT USED
def con_print2(x):
    print("#ID Name S_name #Tel")
    for i in range(0, x):
        spis = ""
        spis += str(id(i)) + ";" + name_gen(i) + ";" + s_name_gen(i) + ";" + tel(i)
        con_spis.append(spis)
        print(spis)
    print(con_spis)
    # return spis
    return con_spis
        # return (id(i), name_gen(i), s_name_gen(i), tel(i)) # записываем контакты в словарь
        # print(spis)

# print(con_print2(2))



# ДЛЯ ЛОКАЛЬНОй генерации списка отмени коммент
# con_print(int(input("input num of contacts:")))
# con_print2(int(input("input num of contacts:")))
