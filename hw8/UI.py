#user interface


import oper_file
from oper_file import *
from data_prov import *
import controller
from oper_file import dir_export3


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
            print("print 'new' to import created file \n"
                  "print 'imp' to import imported file")
            wfi = input() #какой файл импортировать?
            if wfi == "new":
                direx = data_prov.con_print(size) # записываем в direx сформированный список
                oper_file.dir_export2(direx) #инициируем фунцию экспорта от списка direx
            elif wfi == "imp":
                direx = oper_file.import_file  # записываем в direx сформированный список
                oper_file.dir_export2(direx)

        elif inp == "4":
            print("print 'new' to search in created file \n"
                  "print 'imp' to search in imported file")
            f_sear = input()
            if f_sear == "imp":
                finder1 = oper_file.import_file
                oper_file.search2(finder1)  #поиск в имопртированном файле
            elif f_sear == "new":
                finder = data_prov.con_print(size) # записываем в direx сформированный список
                oper_file.search(finder) #инициируем фунцию поиска в списке direx
            #для работы со сторонним списком его надо сохранить

        elif inp == "5":
            print("print 'new' to change created file \n"
                  "print 'imp' to change imported file")
            chang = input()
            # выбираем файл для работы
            if chang == "new":
                print("print 'add' to add info\n"
                      "print 'del' to delete info")
                add = input() # выбираем файл для работы
                if add == "add": # доб инфо
                    adder = data_prov.con_print(size)  # добавляем инфу в файл
                    adding(adder)
                if add == "del": # удалить инфо
                    deller = data_prov.con_print(size)
                    deleter(deller)

            if chang == "imp":
                print("print 'add' to add info\n"
                      "print 'del' to delete info")
                add1 = input()  # выбираем файл для работы
                if add1 == "add": # доб инфо
                    adder = oper_file.import_file  # добавляем инфу в файл
                    adding1(adder)
                if add1 == "del": # удалить инфо
                    deller = oper_file.import_file
                    deleter2(deller)


        elif inp == "q": #при вводе q завершаем прогр
            if input("save directory? y/n: ") == "y": # если надо сохраняем
                print("print 'new' to import created file \n"
                      "print 'imp' to import imported file")
                wfi = input()  # какой файл импортировать?
                if wfi == "new":
                    direx = data_prov.con_print(size)  # записываем в direx сформированный список
                    oper_file.dir_export2(direx)  # инициируем фунцию экспорта от списка direx
                elif wfi == "imp":
                    direx = oper_file.import_file  # записываем в direx сформированный список
                    oper_file.dir_export2(direx)

                break
            else:

                print("Goodbye")
                break

        else: print("Try again")

# ***для локального вызова функции***
# print("Hello, press S to continue")
# if input() == "s":
#     view("s") #вызываем функцию отображения выбора


# end