# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# import datetime
from loging import *


async def hello_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)# вызываем функц log и туда запис два объекта
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}')
    

async def time_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)# вызываем функц log и туда запис два объекта
    await update.message.reply_text(f'Время уже - {datetime.datetime.now().time()}')
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # вызываем функц log и туда запис два объекта
    await update.message.reply_text(f"print commands:\n/hello \n/time \n/weather \n/math")

async def weth(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'посмотри погоду тут https://www.gismeteo.ru/weather-saratov-5032/')

async def math(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # вызываем функц log и туда запис два объекта
    await update.message.reply_text(f"I can calculate for you:\n/sum \n/sum2 \n/sub \n/mult \n/div")



# async def echo(update):
#     """Echo the user message."""
#     update.message.reply_text(sum_com(update.message.text))

async def echo(update):
    """Echo the user message."""
    update.message.reply_text(update(update.message.text))

# summarising EVAL
async def sum_com(numb):
    print("numb")

    num = numb
    sum = eval(num) #/sum x y
    await numb.message.reply_text(f'вот, я сложил: {sum}')


# summarising EVAL
# async def sum_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await log_com(update, context)# вызываем функц log и туда запис два объекта
#     msg = update.message.text
#     print(msg)
#     num = eval(msg.split("/sum")[-1]) #/sum x y
#     # x = float(num[1])
#     # y = float(num[2])
#     # z = x + y
#     await update.message.reply_text(f'вот, я сложил: {msg} = {num}')

# summarising
async def sum_com2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)# вызываем функц log и туда запис два объекта
    msg = update.message.text
    print(msg)
    num = msg.split() #/sum x y
    x = float(num[1])
    y = float(num[2])
    z = x + y
    await update.message.reply_text(f'вот, я сложил: {x} + {y} = {z}')

# substraction
async def sub_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)# вызываем функц log и туда запис два объекта
    msg = update.message.text
    print(msg)
    num = msg.split() #/sub x y
    x = float(num[1])
    y = float(num[2])
    z = x - y
    await update.message.reply_text(f'Вычитаем : {x} - {y} = {z}')

# multiply
async def mult_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)# вызываем функц log и туда запис два объекта
    msg = update.message.text
    print(msg)
    num = msg.split() #/mult x y
    x = float(num[1])
    y = float(num[2])
    z = x * y
    await update.message.reply_text(f'Умножаем : {x} x {y} = {z}')

# division
async def div_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)# вызываем функц log и туда запис два объекта
    msg = update.message.text
    print(msg)
    num = msg.split() #/div x y
    x = float(num[1])
    y = float(num[2])
    z = x / y
    await update.message.reply_text(f'Делим : {x} / {y} = {z}')

# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)