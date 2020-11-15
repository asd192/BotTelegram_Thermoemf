import telebot
from telebot import types

from phrase_dict import phrase
from processing_user_request import request_user
from processing_user_request import log_all

with open("API-Token.txt", "r", encoding="UTF8") as token:
    token = token.readlines()[1].strip()

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def menu_down(message):
    """Крафт и отправка нижнего меню"""
    keyboard_down = types.ReplyKeyboardMarkup(True, False)
    keyboard_down.row('/help')

    bot.send_message(message.chat.id, 'Привет. Если нужна помощь нажми кнопку внизу или напиши /help.',
                     reply_markup=keyboard_down)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f"Целые числа бот распознаёт как значение температуры. Числа с плавающей точкой как \
Ом-ы или мВ. Если требуется указать температуру с плавающей точкой или Ом-ы и мВ целым числом, используй префиксы t, mV,\
Ом после значения. Например так:\n74r 100M --> вернёт <-60.2°C (тип Cu85)>\n\nКоманды вводить нужно так:\n\n{phrase['help'][0]}\n{phrase['main_help']}")


@bot.message_handler(content_types=['text'])
def get_result(message):
    bot.send_message(message.chat.id, request_user(message.text))


bot.polling(none_stop=True, interval=0)
