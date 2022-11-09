from loging import *
import datetime


async def hello_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # �������� ����� log � ���� ����� ��� �������
    await update.message.reply_text(f'������, {update.effective_user.first_name}')


async def time_com(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # �������� ����� log � ���� ����� ��� �������
    await update.message.reply_text(f'����� ��� - {datetime.datetime.now().time()}')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # �������� ����� log � ���� ����� ��� �������
    await update.message.reply_text(f"print commands:\n/hello \n/time \n/weather \n/math")


async def weth(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'�������� ������ ��� https://www.gismeteo.ru/weather-saratov-5032/')


async def math(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # �������� ����� log � ���� ����� ��� �������
    await update.message.reply_text(f"I can calculate for you:"
                                    f"\nprint /calc N+M*K/T")


# calculator EVAL
async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_com(update, context)  # �������� ����� log � ���� ����� ��� �������
    msg = update.message.text
    print(msg)
    num = eval(msg.split("/calc")[-1])  # ������ ����� �������, ������� ������� ��������
    await update.message.reply_text(f'���, ��� ����������: {msg} = {num}')

## end