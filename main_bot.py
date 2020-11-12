import telebot
from telebot import types

from custom_req_hundler import request_user

with open("API-Token.txt", "r", encoding="UTF8") as token:
    token = token.readlines()[1].strip()

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def menu_down(message):
    """Крафт и отправка нижнего меню"""
    keyboard_down = types.ReplyKeyboardMarkup(True, False)
    keyboard_down.row('Помощь')

    bot.send_message(message.chat.id, 'Если нужна помощь нажми кнопку внизу или напиши <Помощь>.',
                     reply_markup=keyboard_down)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Команды вводить нужно так - <Тип ТСМ или ТП><Пробел><Температура, Ом-ы или mV>.\
\n\nНапример, так: K -5.89, K -200, Cu85 74.60 или Cu85 115.")


@bot.message_handler(content_types=['text'])
def get_result(message):
    bot.send_message(message.chat.id, request_user(message.text))


bot.polling(none_stop=True, interval=0)
