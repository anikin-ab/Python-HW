from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from loging import *


async def hello_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)# вызываем функц log и туда запис два объекта
    await update.message.reply_text(f'Привет дружок, {update.effective_user.first_name}')
    

async def time_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)# вызываем функц log и туда запис два объекта
    await update.message.reply_text(f'Время уже дохерищи, ВО - {datetime.datetime.now().time()}')
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # вызываем функц log и туда запис два объекта
    await update.message.reply_text(f"print commands:\n/hello \n/time \n/weather")

async def weth(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'посмотри погоду тут https://www.gismeteo.ru/weather-saratov-5032/')

async def sum_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)# вызываем функц log и туда запис два объекта
    msg = update.message.text
    print(msg)
    item = msg.split() #/sum x y
    x = int(item[1])
    y = int(item[2])
    await update.message.reply_text(f'вот,я сложил: {x} + {y} = {x + y}')
    