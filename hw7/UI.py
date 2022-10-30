#user interface
from data_prov import con_print2
from data_prov import name_gen
from data_prov import s_name_gen
from data_prov import tel
import data_prov
import oper_file
from data_prov import con_print
from oper_file import dir_export
import oper_file as o_f
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
            print("importing in progress\n")
            dir_import(1)

        elif inp == "3":

            # idx = data_prov.id(size)
            # name = data_prov.name_gen(size)
            # s_name_gen = data_prov.s_name_gen(size)
            # tel = data_prov.tel(size)
            # oper_file.dir_export3(idx, name, s_name_gen, tel)

            direx = data_prov.con_print(size)
            oper_file.dir_export(direx)

            # def create_dir(size):
            #     direx = data_prov.con_print2(size)
            #     oper_file.dir_export(direx)
            #     return direx
            # create_dir(size)
            # continue

        elif inp == "4":
            print("person found")

        elif inp == "q": #при вводе q завершаем прогр
            print("Goodbye")
            break

print("Hello, press S to continue")
if input() == "s":
    view("s") #вызываем функцию отображения выбора


