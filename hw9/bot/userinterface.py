# -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import  ContextTypes
from loging import *
import datetime


async def hello_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # вызываем функц log и туда запис два объекта
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}')


async def time_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # вызываем функц log и туда запис два объекта
    await update.message.reply_text(f'Время уже - {datetime.datetime.now().time()}')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # вызываем функц log и туда запис два объекта
    await update.message.reply_text(f"print commands:\n/hello \n/time \n/weather \n/math")


async def weth(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'посмотри погоду тут https://www.gismeteo.ru/weather-saratov-5032/')


async def math(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # вызываем функц log и туда запис два объекта
    await update.message.reply_text(f"I can calculate for you:"
                                    f"\nprint /calc N+M*K/T")


# calculator EVAL
async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # вызываем функц log и туда запис два объекта
    msg = update.message.text
    print(msg)
    num = eval(msg.split("/calc")[-1])  # вводим через проблем, убираем вводное значение
    await update.message.reply_text(f'вот, что получилось: {msg} = {num}')

# **end**