#user interface

import data_prov
import oper_file
from oper_file import *
from data_prov import *
# from oper_file import dir_export2
# from oper_file import dir_import
# from oper_file import search
import controller



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
        global fwi4
        fwi4 = 0
        inp = input()
        if inp == "1":
            print("Input directory size:")
            size = int(input())
            con_print(size) #вызываем метод фомирования списка из data_prov размером size

        elif inp == "2":
            print("2", fwi)
            # dir_import(1) # импортируем созданный список (можно сторонний)
            controller.import_f() # импортируем  список (можно сторонний), но не сохраняем

            fwi4 = oper_file.dir_import()
        elif inp == "3":
            direx = data_prov.con_print(size) # записываем в direx сформированный список
            oper_file.dir_export2(direx) #инициируем фунцию экспорта от списка direx

        elif inp == "4":
            print("fwi", fwi)
            print("fwi4", fwi)
            if fwi4 == 1:
                finder = oper_file.import_file
                oper_file.search(finder)
            else:
                finder = data_prov.con_print(size) # записываем в direx2 сформированный список
                oper_file.search(finder) #инициируем фунцию поиска в списке direx2
            #для работы со сторонним списком его надо сохранить

        elif inp == "q": #при вводе q завершаем прогр
            print("Goodbye")
            break

        else: print("Try again")

# print("Hello, press S to continue")
# if input() == "s":
#     view("s") #вызываем функцию отображения выбора


