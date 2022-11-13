# coding: utf8
# Создать прототип интерактивной базы данных, содержащую информацию
# о сотрудниках некой компании \ студентах вуза \ учениках школы в виде
# одной таблицы (кто желает может создать несколько связанных таблиц или
# полноценную базу данных)
# Программа должна иметь возможность изменять данные
# (редактировать добавлять, удалять), осуществлять сохранение и загрузку.
# А также выводить данные в консоль.

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from controller import *


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ok, print: /start")

#  считываем токен из файла. Глобальный, чтобы считывать его для API
token = ""

#  CREATE file "token.txt" and write down there your TOKEN



def get_token():


    global token
    tok = open("token.txt", "r") # token приходится распаковывать, тк иначе его не видит application = ApplicationBuilder().token(token).build()
    for i in tok:
        token += i
    return token

if __name__ == '__main__':

    print("start")  # обозначаем старт программы
    get_token()
    application = ApplicationBuilder().token(token).build()
    controller.bot_start(application)  # запускаем controller
    # con()  # запускаем контроллер
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()  # starts bot
    print("end")

# **end**
