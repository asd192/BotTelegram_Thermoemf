from coefficients import coefficients
from main_polinom import coeff_tp

from main_intplt_equations import Temperature
from main_intplt_equations import Resist


def separator_str_num(value):
    """ Отделяет числа от строк """
    sep_num = ''.join([n for n in value if n.isdigit() or n in ',.'])
    sep_str = ''.join([n for n in value if n.isalpha()])
    return (sep_num, sep_str)


def is_number(num: str, t=False):
    """ Преобразует в число, если число. Дробит на значения(Т, Ом или mV). """
    try:
        if float(num):
            if ('.' or ',') in num:
                num = num.replace(',', '.')
                return float(num) if t else (float(num), 'R')
            else:
                return int(num) if t else (int(num), 'T')
    except ValueError:
        # если число с указанием типа, отделяем число
        num_num = separator_str_num(num)[0]
        num_str = separator_str_num(num)[1]

        return (is_number(num_num.upper(), True), num_str)


def type_termo(value, type_value, type_grad, is_tp):
    """ Определяет тип, ТП или ТСМ. Отправляет на расчёт. """
    # определение ТП
    if not is_tp and type_grad in coefficients.keys():
        print(type_grad, value, type_value)
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

    # определение ТСМ
    if str(type_grad[0]).isdigit() and not is_tp:
        type_grad_num = ''.join([n for n in type_grad if n.isdigit() or n in ',.'])
        type_grad_str = ''.join([n for n in type_grad if n.isalpha()])

        print(type_grad_num, type_grad_str)
        # if type_value in 'TТ':
        #     return Temperature.coeff[]


def request_user(message):
    msg = message.split()
    msg0, msg1, msg2 = is_number(msg[0].upper()), msg[1].upper(), False
    if len(msg) == 3:
        msg2 = msg[2]

    msg = (*msg0, msg1, msg2)
    print(msg)

    result = type_termo(*msg)
    return result


print(request_user('100 K'))
print()
print(request_user('142.80 50m'))
print()
print(request_user('100 50м'))
print()
print(request_user('100 50m 426'))
print()
print(request_user('100 50м 428'))
print()
print()
print(request_user('100.00t 50m 426'))
print()
print(request_user('100.00т 50м 428'))
print()
print(request_user('100.00t 50p 385'))
print()
print(request_user('100.00т 50п 391'))
print()
print()
print(request_user('100.00r 50m 426'))
print()
print(request_user('100.00r 50м 428'))
print()
print(request_user('100.00r 50p 385'))
print()
print(request_user('100.00r 50п 391'))

# for i in variants.values():
#     print('Cu6' in i)
