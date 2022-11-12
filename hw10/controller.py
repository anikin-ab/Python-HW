# -*- coding: utf-8 -*-
# объединяем функции
#  Наверное, это больше UI, а UI - контроллер. судя по выпоняемым функциям

# import ui
from ui import *
# from loging import *
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


def bot_start(application):
    global app
    app = application
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("cd", create_directory))
    app.add_handler(CommandHandler("id", import_directory))
    app.add_handler(CommandHandler("ed", export_directory))
    app.add_handler(CommandHandler("fp", find_person))
    # app.add_handler(CommandHandler("chd", change_directory))


#
# def con():
#     print("Hello, press S to continue")
#     start = input()
#     if start == "s" or start == "S":
#         ui.view() #вызываем функцию отображения выбора
#
# def import_f():
#     ui.dir_import()  # импортируем созданный список (можно сторонний)



# end