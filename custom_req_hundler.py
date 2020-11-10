from coefficients import coefficients
from main_polinom import coeff_tp


def is_number(num, t=False):
    """ Преобразует в число, если число. Дробит на значения(Т, Ом или mV). """
    try:
        if float(num):
            if ('.' or ',') in num:
                return float(num) if t else (float(num), 'R')
            else:
                return int(num) if t else (int(num), 'T')
    except ValueError:
        # если число с указанием типа, отделяем число
        index_num = -1
        for i in num[::-1]:
            index_num += 1
            if i.isdigit():
                break

        return (is_number(num[:-(index_num)].upper(), True), num[-(index_num):])


def is_termo(value, type_value, type_grad, is_tp):
    """ Определяет тип, ТП или ТСМ. Отправляет на расчёт. """
    if not is_tp and type_grad in coefficients.keys():
        print(type_grad, value, type_value)
        if type_value in 'TТ':
            return coeff_tp(type_grad, value, 'T')
        elif type_value in 'BRРMVОМВ':
            return coeff_tp(type_grad, value, 'mV')
        else:
            print('ELSE', type(value))
            if type(value) is int:
                coeff_type = 'T'
            if type(value) is float:
                coeff_type = 'mV'
            return coeff_tp(type_grad, value, coeff_type)



def request_user(message):
    msg = message.split()
    msg0, msg1, msg2 = is_number(msg[0].upper()), msg[1].upper(), False
    if len(msg) == 3:
        msg2 = msg[2]

    msg = (*msg0, msg1, msg2)
    print(msg)

    result = is_termo(*msg)
    return result

print(request_user('300.05t k'))
print()
print(request_user('300 k'))
print()

print(request_user('500 a3'))
print()
print(request_user('500.00t a3'))
print()
print(request_user('7mV a3'))
print()
print(request_user('7V a3'))
print()

print(request_user('20.644 k'))
print()
print(request_user('100 Cu428'))
print()
print(request_user('142.80 Cu428'))
print()

print(request_user('100 50m 426'))
print()
print(request_user('100 50м 428'))
print()
print()

print(request_user('20v k'))
print()
print(request_user('22в k'))
print()
print(request_user('100.00t Cu428'))
print()
print(request_user('142r Cu428'))
print()
print(request_user('142р Cu428'))
print()

print(request_user('100.00t 50m 426'))
print()
print(request_user('100.00т 50м 428'))
print()
print(request_user('100.00t 50p 385'))
print()
print(request_user('100.00т 50п 391'))


# for i in variants.values():
#     print('Cu6' in i)
