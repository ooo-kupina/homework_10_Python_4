from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes

import config
import poly

def hello_command(update: Update, context: ContextTypes) -> None:
    update.message.reply_text(f'Hello, {update.effective_user.first_name}!')
    update.message.reply_text(f'Этот бот генерирует два многочлена случайным образом и показывает их сумму.')
    update.message.reply_text(f'/help Помощь\n/help Как получить результат')

def help_command(update: Update, context: ContextTypes):
    update.message.reply_text(f'/help Помощь\n Для формирования результата введите команду вида:\n/poly x y\nгде x и y - небольшие целые числа через пробел, коэффициенты многочленов № 1 и № 2 соответственно.')

def poly_command(update: Update, context: ContextTypes):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])

    poly_1 = poly.polynom1(x)
    poly_2 = poly.polynom2(y)
    poly_sum = poly.poly_sum(poly_1, poly_2)

    update.message.reply_text(f'Многочлен № 1:\n{poly_1}')
    update.message.reply_text(f'Многочлен № 2:\n{poly_2}')
    update.message.reply_text(f'Сумма многочленов:\n{poly_sum}')

updater = Updater(config.TOKEN)

updater.dispatcher.add_handler(CommandHandler("start", hello_command))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
updater.dispatcher.add_handler(CommandHandler("poly", poly_command))

print('server start')
updater.start_polling()
updater.idle()
