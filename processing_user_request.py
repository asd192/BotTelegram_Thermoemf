import random
import datetime
from os import remove

from coefficients import coefficients
from main_polinom import coeff_tp

from main_intplt_equations import Temperature, Resist

from phrase_dict import phrase

# TODO переделать на log_all
def error(user_message, my_message=None):
    """ Обработка ошибок """
    while True:
        try:
            with open("get_log.lock", "x"):
                with open("user_message.log", "a", encoding="UTF8") as dbq_log:
                    dbq_log.write(f'{datetime.datetime.now()} - {user_message} - {my_message}\n')
            remove("get_log.lock")
            break
        except FileExistsError:
            continue

    msg_err = random.choice(phrase['error'])
    msg_help = random.choice(phrase['help'])

    return f'{msg_err}\n\n{msg_help}\n Помощь - /help'


def separator_str_num(value):
    """ Отделяет числа от строк """
    sep_num = ''.join([n for n in value if n.isdigit() or n in '.-'])
    sep_str = ''.join([n for n in value if n.isalpha()])

    return (sep_num, sep_str)


def is_number(num, from_separator=False):
    """ Преобразует в число, если число. Дробит на значения(Т, Ом или mV). """
    try:
        if float(num) or float(num) == 0:
            if num.isdigit() or num[1:].isdigit():
                num, num_str = int(num), 'T'
            else:
                num, num_str = float(num), 'R'
            result = num if from_separator else (num, num_str)

            return result
    except ValueError:
        # если число с указанием типа, отделяем число
        num_num = separator_str_num(num)[0]
        num_str = separator_str_num(num)[1]

        return (is_number(num_num, from_separator=True), num_str)


def type_termo(value, type_value, type_grad, is_tp):
    """ Определяет тип, ТП или ТСМ. Отправляет на расчёт. """
    # определение ТП
    grad, coeff_type = None, None
    if not is_tp and type_grad in coefficients.keys():
        if type_value in 'TТ':
            return coeff_tp(type_grad, value, 'T')
        elif type_value not in 'TТ':
             return coeff_tp(type_grad, value, 'mV')
        else:
            if type(value) is int:
                coeff_type = 'T'
            if type(value) is float:
                coeff_type = 'mV'
            return coeff_tp(type_grad, value, coeff_type)

    else:
        type_grad_num = separator_str_num(type_grad)[0]
        type_grad_str = separator_str_num(type_grad)[1]

        if type_grad_str in 'MМ':
            grad = 'CU428'
        if type_grad_str in 'PTПТ':
            grad = 'PT391'
        if type_grad_str in 'NIНИ':
            grad = 'NI617'

        # определение ТСМ с False
        if str(type_grad[0]).isdigit() and not is_tp:
            if type_value in 'TТ':
                result = Temperature.coeff[grad](value, float(type_grad_num))
                return f"{result:.2f} Ом({grad})"
            if type_value not in 'TТ':
                result = Resist.coeff[grad](value, float(type_grad_num))
                return f"{round(result)} °C({grad})"

        # определение ТСМ без False
        if str(type_grad[0]).isdigit() and is_tp in '426428385391':
            ### переопределяем пользовательский коэффициент на правильный ###
            g = {
                385: (385, 38, 35, 5),
                391: (391, 31, 91, 9),
                426: (426, 46, 6),
                428: (428, 48, 8),
                617: (617, 61, 67, 7)
            }

            alpha = [k for k, i in g.items() if int(is_tp) in i][0]
            grad = grad.replace(grad[2:], str(alpha))
            #################################################################

            if type_value in 'TТ':
                result = Temperature.coeff[grad](value, float(type_grad_num))
                return f"{result:.2f} Ом({grad})"
            if type_value not in 'TТ':
                result = Resist.coeff[grad](value, float(type_grad_num))
                return f"{round(result)} °C({grad})"


def request_user(message):
    """ Обрабатывает сообщение пользователя """
    msg = message.split()
    if len(msg) < 2 or len(msg) > 4:
        return error(msg)
    else:
        try:
            msg01 = is_number(msg[0].replace(',', '.').upper())
            msg2 = msg[1].upper()
            msg3 = msg[2] if len(msg) == 3 else False

            msg_processing = (*msg01, msg2, msg3)
            result = type_termo(*msg_processing)

            return result

        except IndexError:
            return error(msg, 'IndexError')
        except RecursionError:
            return error(msg, 'RecursionError')

if __name__ == '__main__':
    print(request_user('78.7 100ni'))
    print(request_user('-50 100n'))
    # print(request_user('-74.60t 100M'))
    # print(request_user('120,60r 100M 426'))
