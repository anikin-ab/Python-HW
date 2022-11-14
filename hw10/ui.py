# -*- coding: utf-8 -*-
# UI
from telegram import Update
from telegram.ext import ContextTypes
from loging import *


import oper_file
from oper_file import *
from data_prov import *
from oper_file import dir_export3
import controller

# start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # вызываем функц log и туда запис два объекта
    await update.message.reply_text(f"print commands: \n/HELP\n"
                                    f"\n/cd (create_directory)"
                                    f" \n/id (import_directory)"
                                    f" \n/ed (export_directory)"
                                    f" \n/fp (find_person)")
                                    # f" \n/chd (change_directory)"

# help

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # вызываем функц log и туда запис два объекта
    await update.message.reply_text(f"Вводи команды, слова через пробелы:\n/cd 'size' (например: /cd 5)\n Больше 10 не советую"
                                    f" \n/id 'directory_name' (например: /id new.csv)"
                                    f" \n/ed 'new' or 'imp' 'file_name' (например: /ed new new2.csv)"
                                    f" \n/fp 'new' of 'imp' 'person info' (например: /fp imp 3)"
                                    # f" \n/chd (change_directory) to change directory"
                                    f" \n/help")

size = 0
# создание справочника
async def create_directory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # вызываем функц log и туда запис два объекта
    global size
    global direx
    msg = update.message.text
    print(msg)
    size = msg.split("/cd")[-1]  # задаем размер справочника
    direx = con_print(int(size))  # список созданного справочника
    await update.message.reply_text(f'Создаю справочник, размером {size} строк')
    for i in contact_list:
        await update.message.reply_text(f'\n{i} ')  # выводим новым предложением
    # await update.message.reply_text(f'new {contact_list} ')  # выводим списком

# экспорт справочника
async def export_directory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # вызываем функц log и туда запис два объекта
    global size
    global direx
    msg = update.message.text
    print(msg)
    # print("ed", size)   # Для отладки
    wfi = msg.split(" ")[-2]
    d_name = msg.split(" ")[-1]
    # print("wfi", type(wfi), {wfi})  # Для отладки
    # print("d_name", type(d_name), {d_name})   # Для отладки
    if wfi == "new":
        # direx = data_prov.con_print(size)  # записываем в direx сформированный список
        oper_file.dir_export2(direx, d_name)  # инициируем фунцию экспорта от списка direx
    elif wfi == "imp":
        direx = oper_file.import_file  # записываем в direx импортированный список
        oper_file.dir_export2(direx, d_name)
    await update.message.reply_text(f'{wfi} справочник с названием {d_name} экспортирован')

#импорт справочника
async def import_directory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # вызываем функц log и туда запис два объекта
    global size
    global direx
    msg = update.message.text
    print(msg)
    # print("ed", size)   # Для отладки
    new_name = msg.split("/id ")[-1]
    # print("wfi", type(wfi), {wfi})   # Для отладки
    res = dir_import(new_name) # возвращаем результат импорта
    await update.message.reply_text(f'{res}')


# поиск по справочнику
async def find_person(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # вызываем функц log и туда запис два объекта

    global size
    global finder
    print("fp", size)
    msg = update.message.text
    print(msg)
    print(size)
    # f_sear = msg.split("/id ")[-1]
    f_sear = msg.split(" ")[-2]
    p_name = msg.split(" ")[-1]

    if f_sear == "imp":
        finder1 = oper_file.import_file
        oper_file.search2(finder1, p_name)  # поиск в имопртированном файле

        spis = oper_file.search(finder1, p_name)  # инициируем фунцию поиска в списке direx
        if p_name == "all":
            await update.message.reply_text(f'Находим:\n  ')
            for i in finder1:
                await update.message.reply_text(f'{i} ')
        else:
            await update.message.reply_text(f'Находим:\n {spis} ')

    elif f_sear == "new":
        finder = direx
        oper_file.search(finder, p_name)  # инициируем фунцию поиска в списке direx
    # для работы со сторонним списком его надо сохранить
        spis = oper_file.search(finder, p_name)  # инициируем фунцию поиска в списке direx
        if p_name == "all":
            await update.message.reply_text(f'Находим:\n  ')
            for i in finder:
                await update.message.reply_text(f'{i} ')
        else:
            await update.message.reply_text(f'Находим:\n {spis} ')


## СВЕРНУТЬ, В БОТЕ НЕ НУЖНА
# # функция отображения задач
# def view():
#     while True:
#         print("\npress q to quit")
#         print("1: create directory" #предлагаем выбрать действие
#               " \n2: import directory"
#               " \n3: export directory"
#               " \n4: find person"
#               " \n5: change directory")
#         print()
#
#         global size
#         size = 0
#         inp = input()
#         if inp == "1":
#             print("Input directory size:")
#             size = int(input())
#             con_print(size) #вызываем метод фомирования списка из data_prov размером size
#
#         elif inp == "2":
#             controller.import_f() # импортируем  список (можно сторонний), но не сохраняем
#             # dir_import()
#
#         elif inp == "3":
#             print("print 'new' to export created file \n"
#                   "print 'imp' to export imported file")
#             wfi = input() #какой файл импортировать?
#             if wfi == "new":
#                 direx = data_prov.con_print(size) # записываем в direx сформированный список
#                 oper_file.dir_export2(direx) #инициируем фунцию экспорта от списка direx
#             elif wfi == "imp":
#                 direx = oper_file.import_file  # записываем в direx импортированный список
#                 oper_file.dir_export2(direx)
#
#         elif inp == "4":
#             print("print 'new' to search in created file \n"
#                   "print 'imp' to search in imported file")
#             f_sear = input()
#             if f_sear == "imp":
#                 finder1 = oper_file.import_file
#                 oper_file.search2(finder1)  #поиск в имопртированном файле
#             elif f_sear == "new":
#                 finder = data_prov.con_print(size) # записываем в direx сформированный список
#                 oper_file.search(finder) #инициируем фунцию поиска в списке direx
#             #для работы со сторонним списком его надо сохранить
#
#         elif inp == "5":
#             print("print 'new' to change created file \n"
#                   "print 'imp' to change imported file")
#             chang = input()
#             # выбираем файл для работы
#             if chang == "new":
#                 print("print 'add' to add info\n"
#                       "print 'del' to delete info")
#                 add = input() # выбираем файл для работы
#                 if add == "add": # доб инфо
#                     adder = data_prov.con_print(size)  # добавляем инфу в файл
#                     adding(adder)
#                 if add == "del": # удалить инфо
#                     deller = data_prov.con_print(size)
#                     deleter(deller)
#
#             if chang == "imp":
#                 print("print 'add' to add info\n"
#                       "print 'del' to delete info")
#                 add1 = input()  # выбираем файл для работы
#                 if add1 == "add": # доб инфо
#                     adder = oper_file.import_file  # добавляем инфу в файл
#                     adding1(adder)
#                 if add1 == "del": # удалить инфо
#                     deller = oper_file.import_file
#                     deleter2(deller)
#
#
#         elif inp == "q": #при вводе q завершаем прогр
#             if input("save directory? print y/n (yes/no): ") == "y": # если надо сохраняем
#                 print("print 'new' to import created file \n"
#                       "print 'imp' to import imported file")
#                 wfi = input()  # какой файл импортировать?
#                 if wfi == "new":
#                     direx = data_prov.con_print(size)  # записываем в direx сформированный список
#                     oper_file.dir_export2(direx)  # инициируем фунцию экспорта от списка direx
#                 elif wfi == "imp":
#                     direx = oper_file.import_file  # записываем в direx сформированный список
#                     oper_file.dir_export2(direx)
#
#                 break
#             else:
#
#                 print("Goodbye")
#                 break
#
#         else: print("Try again")

# ***для локального вызова функции***
# print("Hello, press S to continue")
# if input() == "s":
#     view("s") #вызываем функцию отображения выбора


# end