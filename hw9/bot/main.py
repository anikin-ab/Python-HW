from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import controller

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="I'm a bot, print /help")


if __name__ == '__main__':

    application = ApplicationBuilder().token('5774992478:AAF9LkS-xl0cdSMgo-S7Qh4I9DeuEkE1tA8').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()