#user interface

import data_prov
import oper_file
# from oper_file import *
from data_prov import *
# from oper_file import dir_export2
# from oper_file import dir_import
# from oper_file import *
import controller

fwi4 = 0

# функция отображения задач
def view():
    while True:
        print("\npress q to quit")
        print("1: create directory" #предлагаем выбрать действие
              " \n2: import directory"
              " \n3: export directory"
              " \n4: find person"
              " \n5: change directory")
        print()

        size = 0
        inp = input()
        if inp == "1":
            print("Input directory size:")
            size = int(input())
            con_print(size) #вызываем метод фомирования списка из data_prov размером size

        elif inp == "2":
            controller.import_f() # импортируем  список (можно сторонний), но не сохраняем

        elif inp == "3":
            direx = data_prov.con_print(size) # записываем в direx сформированный список
            oper_file.dir_export2(direx) #инициируем фунцию экспорта от списка direx

        elif inp == "4":
            print("print 'new' to search in created file \n"
                  "print 'imp' to search in imported file")
            f_sear = input()
            if f_sear == "imp":
                finder = oper_file.import_file
                oper_file.search(finder)  #поиск в имопртированном файле
            elif f_sear == "new":
                finder = data_prov.con_print(size) # записываем в direx сформированный список
                oper_file.search(finder) #инициируем фунцию поиска в списке direx
            #для работы со сторонним списком его надо сохранить

        elif inp == "5":
            print("print 'new' to change created file \n"
                  "print 'imp' to change imported file")
            chang = input()
            if chang == "new":
                print("print 'new' to change created file \n"
                      "print 'imp' to change imported file")
                adder = data_prov.con_print(size)  # добавляем инфу в файл
                adding(adder)
                print("adder1")
            if chang == "imp":
                adder = oper_file.import_file #добавляем инфу в файл
                adding(adder)
                print("adder2")

        # elif inp == "6":

        elif inp == "q": #при вводе q завершаем прогр
            print("Goodbye")
            break

        else: print("Try again")

# ***для локального вызова функции***
# print("Hello, press S to continue")
# if input() == "s":
#     view("s") #вызываем функцию отображения выбора


