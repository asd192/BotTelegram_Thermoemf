import random

from coefficients import coefficients
from main_polinom import coeff_tp

from main_intplt_equations import Temperature
from main_intplt_equations import Resist

from phrase_dict import phrase


def separator_str_num(value):
    """ Отделяет числа от строк """
    sep_num = ''.join([n for n in value if n.isdigit() or n in '.-'])
    sep_str = ''.join([n for n in value if n.isalpha()])

    return (sep_num, sep_str)


def is_number(num, from_separator=False):
    """ Преобразует в число, если число. Дробит на значения(Т, Ом или mV). """
    try:
        if float(num):
            if num.isdigit():
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
    print(value, type_value, type_grad, is_tp)
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
        global grad

        type_grad_num = separator_str_num(type_grad)[0]
        type_grad_str = separator_str_num(type_grad)[1]

        if type_grad_str in 'MМ':
            grad = 'CU428'
        if type_grad_str in 'PtП':
            grad = 'PT391'
        if type_grad_str in 'NiНИ':
            grad = 'NI617'

        # определение ТСМ с False
        if str(type_grad[0]).isdigit() and not is_tp:
            if type_value in 'TТ':
                result = Temperature.coeff[grad](value, float(type_grad_num))
                return f"{result:.2f} Ом({grad})"
            if type_value not in 'TТ':
                result = Resist.coeff[grad](value, float(type_grad_num))
                return f"{result:.1f} °C({grad})"

        # определение ТСМ с без False
        if str(type_grad[0]).isdigit() and is_tp in '426428385391':
            ### переопределяем пользовательский коэффициент на правильный ###
            g = {
                385: (385, 38, 35, 5),
                391: (391, 31, 91, 9),
                426: (426, 46, 6),
                428: (428, 48, 8),
                617: (617, 61, 67, 7)
            }

            a = [k for k, i in g.items() if int(is_tp) in i][0]
            grad = grad.replace(grad[2:], str(a))
            #################################################################

            if type_value in 'TТ':
                result = Temperature.coeff[grad](value, float(type_grad_num))
                return f"{result:.2f} Ом({grad})"
            if type_value not in 'TТ':
                result = Resist.coeff[grad](value, float(type_grad_num))
                return f"{result:.1f} °C({grad})"


def request_user(message):
    try:
        msg = message.split()
        print(msg)
        msg0, msg1, msg2 = is_number(msg[0].replace(',', '.').upper()), msg[1].upper(), False
        if len(msg) == 3:
            msg2 = msg[2]

        msg = (*msg0, msg1, msg2)

        result = type_termo(*msg)

        return result
    except IndexError:
        msg_err = phrase['error'][int(random.uniform(0, len(phrase['error'])))]
        msg_help = phrase['help'][int(random.uniform(0, len(phrase['help'])))]

        return f'{msg_err}\n\n{msg_help}'

if __name__ == '__main__':
    print(request_user('10 K'))
    print()
    print(request_user('20.00 K'))
    print()
    print(request_user('30,00 K'))
    print()
    print(request_user('20r K'))
    print()
    print(request_user('20.00r K'))
    print()
    print(request_user('20,00t K'))
    print()
    print(request_user('20.00t K'))
    print()
    print(request_user('20 K'))
    print()
    print()
    print(request_user('-74,60 100M'))
    print()
    print(request_user('-74.60 100M'))
    print()
    print(request_user('-74,60t 100M'))
    print()
    print(request_user('-74.60t 100M'))
    print()
    print(request_user('-74r 100M'))
    print()
    print(request_user('-74r 100M'))
    print()
    print(request_user('-74,60r 100M'))
    print()
    print(request_user('-74.60r 100M'))
    print()
    print()
    print(request_user('-74,60 100M 426'))
    print()
    print(request_user('-74.60 100M 426'))
    print()
    print(request_user('-74,60t 100M 426'))
    print()
    print(request_user('-74.60t 100M 426'))
    print()
    print(request_user('-74r 100M 426'))
    print()
    print(request_user('-74r 100M 426'))
    print()
    print(request_user('-74,60r 100M 426'))
    print()
    print(request_user('-74.60r 100M 426'))