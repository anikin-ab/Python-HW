# генерируем данные для справочника
# тут генерируем справочник
#Предлагаемые поля: id, имя, фамилия, день рождения, место работы,
# номер телефона (может быть несколько). В качестве символа разделителя
# использовать пустую строку (пустой символ).

import random
from oper_file import *
import oper_file


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
contact_list = [["№", "Имя", "Фамилия", "Телефон"]]  #пишем названия столбцов
# contact_list = []


# main variant with list
def con_print(x):
    count = 0
    for i in range(0, x):
        # contact_list.append([str(id(i)), name_gen(i), s_name_gen(i), tel(i)]) # записываем контакты в список
        contact_list.append([str(id(i + 1)), name_gen(i + 1), s_name_gen(i + 1), tel(i + 1)])  # записываем контакты в список
        # можно сразу при формировании списка записывать его в файл
        oper_file.dir_export3(contact_list[i + 1][0], contact_list[i + 1][1], contact_list[i + 1][2], contact_list[i + 1][3])
        spis = ""
        spis += str(str(contact_list[i][0]) + " " + contact_list[i][1]
                    + " " + contact_list[i][2] + " " + contact_list[i][3])
        print(spis) # выводим строкой
        if count == x - 1:
            spis = ""
            spis += str(str(contact_list[i + 1][0]) + " " + contact_list[i + 1][1]
                        + " " + contact_list[i + 1][2] + " " + contact_list[i + 1][3])
            print(spis) #выводим последний элемент
        count += 1
        # print(contact_list[i])  #выводим списком
    # print(contact_list)  # напечатать весь список контактов
    return contact_list

# ДЛЯ ЛОКАЛЬНОй генерации списка отмени коммент
# con_print(int(input("input num of contacts:")))


