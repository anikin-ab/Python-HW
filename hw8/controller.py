# объединяем функции


import UI
# from UI import *


def con():
    print("Hello, press S to continue")
    if input() == "s":
        UI.view("s") #вызываем функцию отображения выбора

def import_f():
    UI.dir_import(0)  # импортируем созданный список (можно сторонний)

# есть ли смысл сюда перекидывать функции из UI??

