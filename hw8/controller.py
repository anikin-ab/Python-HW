# объединяем функции


import UI
# from UI import *


def con():
    print("Hello, press S to continue")
    start = input()
    if start == "s" or start == "S":
        UI.view() #вызываем функцию отображения выбора

def import_f():
    UI.dir_import()  # импортируем созданный список (можно сторонний)



# end