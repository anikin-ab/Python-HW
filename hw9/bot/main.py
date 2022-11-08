# coding: utf8
# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и
# комплексными числами, организовать меню, добавив в неё систему логирования

import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
import controller

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

#  считываем токен из файла
token = ""


def get_token():
    global token
    tok = open("token.txt", "r")
    for i in tok:
        token += i
    return token

if __name__ == '__main__':

    print("start")  # обозначаем старт программы
    get_token()
    application = ApplicationBuilder().token(token).build()
    controller.bot_start(application)  # запускаем controller
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()

    print("end")
