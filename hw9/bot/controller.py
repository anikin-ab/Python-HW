# -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from telegram.ext import MessageHandler, filters

from UI import *
from loging import *


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
    # app.add_handler(CommandHandler("sum2", echo))
    app.add_handler(MessageHandler(filters.TEXT, echo))


    # app.run_polling()
