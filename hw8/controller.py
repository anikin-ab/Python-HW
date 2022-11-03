# объединяем функции


import UI
# from UI import *


def con():
    print("Hello, press S to continue")
    start = input()
    if start == "s" or start == "S":
        UI.view() #вызываем функцию отображения выбора

def import_f():
    UI.dir_import(0)  # импортируем созданный список (можно сторонний)

# есть ли смысл сюда перекидывать функции из UI??

