import math
from coefficients import coeff


def polinom(value, coeff_coeff, K_Type):
    """ Расчёт полинома """
    if not K_Type:
        polinom = [k * (value) ** n for n, k in enumerate(coeff_coeff)]
    else:
        print('Type_K')
        polinom = [k * (value) ** n + (0.1185976 * math.exp(-0.0001183432 * ((value - 126.9686)**2))) for n, k in enumerate(coeff_coeff)]

    return f"{round(sum(polinom), 3)}"


def coeff_tp(graduation, value):
    """ Определение требуемых коэффициентов """
    # определение типа коэффициента
    if type(value) is int:
        coeff_type = 'T'
    elif type(value) is float:
        coeff_type = 'mV'

    # коэффициенты если значение в границах по ГОСТ
    for i_coeff in coeff[graduation][coeff_type].values():
        if i_coeff[0][0] <= value <= i_coeff[0][1]:
            coeff_coeff = i_coeff[1]
            not_found = False
            break
        else:
            not_found = True

    # коэффициенты если значение за границами по ГОСТ
    if not_found == True:
        min_low = coeff[graduation][coeff_type]['low'][0][0]
        max_high = coeff[graduation][coeff_type]['high'][0][1]

        if value <= min_low:
            coeff_coeff = coeff[graduation][coeff_type]['low'][1]
        if value >= max_high:
            coeff_coeff = coeff[graduation][coeff_type]['high'][1]

    # расчет полинома
    if graduation == 'K' and 500 <= value <= 1372 and coeff_type == 'T':
        K_type = True
    else:
        K_type = False

    poly = polinom(value, coeff_coeff, K_type)

    # сбор сообщения для отправки пользователю
    message = 'за пределами ГОСТ'
    result = f"{poly}({graduation}) {message if not_found else ''}"

    return result

# TODO mV-low coeff не подходят
print(coeff_tp('K', -1.889))