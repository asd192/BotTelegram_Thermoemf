import telebot
from telebot import types

from coefficients import coefficients
from main_polinom import coeff_tp


with open("API-Token.txt", "r", encoding="UTF8") as token:
    token = token.readlines()[1].strip()

bot = telebot.TeleBot(token)

def num(N):
    try:
        return int(N)
    except ValueError:
        return float(N)

@bot.message_handler(commands=['start'])
def menu_down(message):
    """Крафт и отправка нижнего меню"""
    keyboard_down = types.ReplyKeyboardMarkup(True, False)
    keyboard_down.row('Помощь')

    bot.send_message(message.chat.id, 'Если нужна помощь нажми кнопку внизу или напиши <Помощь>.', reply_markup=keyboard_down)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Команды вводить нужно так - <Тип ТСМ или ТП><Пробел><Температура, Ом-ы или mV>.\
\n\nНапример, так: K -5.89, K -200, Cu85 74.60 или Cu85 115.")


@bot.message_handler(content_types=['text'])
def get_result(message):
    msg_txt = message.text.upper()
    msg_txt = msg_txt.split()

    if msg_txt[0] in coefficients.keys():
        print(type(msg_txt[0]), type(num(msg_txt[1])))
        result = coeff_tp(msg_txt[0], num(msg_txt[1]))
        return bot.send_message(message.chat.id, result)


    else:
        help(message)

bot.polling(none_stop=True, interval=0)
