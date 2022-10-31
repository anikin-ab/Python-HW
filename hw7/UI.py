#user interface

import data_prov
import oper_file
from data_prov import *
from oper_file import dir_export2
from oper_file import dir_import



# функция отображения задач
def view(start):
    while True:
        print("\npress q to quit")
        print("1: create directory" #предлагаем выбрать действие
              " \n2: import directory"
              " \n3: export directory"
              " \n4: find person")
        print()
        size = 0
        inp = input()
        if inp == "1":
            print("Input directory size:")
            size = int(input())
            con_print(size) #вызываем метод фомирования списка из data_prov размером size

        elif inp == "2":
            dir_import(1) # импортируем созданный список (можно сторонний)

        elif inp == "3":
            # global direx
            direx = data_prov.con_print(size) # записываем в direx сформированный список
            oper_file.dir_export2(direx) #инициируем фунцию экспорта от списка direx

        elif inp == "4":
            # print("search by:\nID"
            #       "\nName"
            #       "\ns_Name"
            #       "\ntel")
            # s_per = input()
            # oper_file.search(direx)
            direx2 = data_prov.con_print(size)
            oper_file.search(direx2)
            # oper_file.search(con_print(size))
            # oper_file.search.con_print(size)
            # print("person found")

        elif inp == "q": #при вводе q завершаем прогр
            print("Goodbye")
            break

print("Hello, press S to continue")
if input() == "s":
    view("s") #вызываем функцию отображения выбора


