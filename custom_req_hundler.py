variants = {
    'Pt385': {},
    'Pt391': {},
    'Cu426': {'Cu426', 'Cu46', 'Cu26', 'Cu6', '50M', 'M', '50М', 'М'},
    'Cu428': {'Cu428', 'Cu48', 'Cu28', 'Cu8', '50M', 'M', '50М', 'М'},
    'Ni617': {},
    'L': {'L', 'XK', 'TXK', 'Л', 'ХК', 'ТХК'},
    'K': {'K', 'XA', 'TXA', 'К', 'ХА', 'ТХА'},
    'R': {},
    'S': {},
    'B': {},
    'J': {},
    'T': {},
    'E': {},
    'N': {},
    'A1': {},
    'A2': {},
    'A3': {},
    'M': {}
}


def is_number(num, t=False):
    """ Преобразует в число, если число. Дробит на значения(Т, Ом или mV). """
    try:
        if float(num):
            if ('.' or ',') in num:
                return float(num) if t else (float(num), 'not_t')
            else:
                return int(num) if t else (int(num), 't')
    except ValueError:
        return (is_number(num[:-1], True), num[-1])


def is_42(grad):
    """ Определяет тип ТП или ТСМ """
    pass


def request_user(message):
    msg = message.split()
    msg0, msg1 = is_number(msg[0]), msg[1]

    return (msg0, msg1)


print(request_user('300 к'))
print(request_user('22.843 k'))
print(request_user('100 Cu428'))
print(request_user('142.80 Cu428'))
print(request_user('500 а3'))
print(request_user('100 50m 426'))
print(request_user('100 50м 428'))

print(request_user('300.00t к'))
print(request_user('22v k'))
print(request_user('22в k'))
print(request_user('100.00t Cu428'))
print(request_user('142r Cu428'))
print(request_user('142р Cu428'))
print(request_user('500.00t а3'))
print(request_user('100.00t 50m 426'))
print(request_user('100.00т 50м 428'))
print(request_user('100.00t 50p 385'))
print(request_user('100.00т 50п 391'))

# for i in variants.values():
#     print('Cu6' in i)
