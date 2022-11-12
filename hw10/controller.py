# объединяем функции


import ui
# from UI import *


def con():
    print("Hello, press S to continue")
    start = input()
    if start == "s" or start == "S":
        ui.view() #вызываем функцию отображения выбора

def import_f():
    ui.dir_import()  # импортируем созданный список (можно сторонний)



# end