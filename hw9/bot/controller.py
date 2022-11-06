from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from UI import *
from loging import *



app = ApplicationBuilder().token("5774992478:AAF9LkS-xl0cdSMgo-S7Qh4I9DeuEkE1tA8").build()
print("to start print /help")

app.add_handler(CommandHandler("hello", hello_com))
app.add_handler(CommandHandler("time", time_com))
app.add_handler(CommandHandler("sum", sum_com))
app.add_handler(CommandHandler("start", help))
app.add_handler(CommandHandler("weather", weth))

app.run_polling()

print("end")