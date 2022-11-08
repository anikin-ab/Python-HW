from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from UI import *
from loging import *

# global app
def bot_start(application):
    global app
    app = application
    app.add_handler(CommandHandler("hello", hello_com))
    app.add_handler(CommandHandler("time", time_com))
    app.add_handler(CommandHandler("sum", sum_com))
    app.add_handler(CommandHandler("start", help))
    app.add_handler(CommandHandler("weather", weth))
    app.add_handler(CommandHandler("math", math))
    app.add_handler(CommandHandler("sum", sum_com))
    app.add_handler(CommandHandler("sub", sub_com))
    app.add_handler(CommandHandler("mult", mult_com))
    app.add_handler(CommandHandler("div", div_com))
    # app.run_polling()

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id,
#                                    text="I'm a bot, print /help")


# application.add_handler(CommandHandler("hello", hello_com))

# app.add_handler(CommandHandler("hello", hello_com))
# app.add_handler(CommandHandler("time", time_com))
# app.add_handler(CommandHandler("sum", sum_com))
# app.add_handler(CommandHandler("start", help))
# app.add_handler(CommandHandler("weather", weth))

# application.run_polling()
# app.run_polling()

# print("end")