import math
from coefficients import coefficients


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
    else:
        return "Я так не понимаю. Смотри как нужно - К 100 или К 20.452 и т.п.."

    # определение необходимых коэффициентов
    found = False
    for interval, coeff in coefficients[graduation][coeff_type].items():
        if interval[0] <= value <= interval[1]:
            coeff_coeff = coeff
            found = True
            break
    print(interval, coeff)
    if not found:
        return "Значение за пределами ГОСТ"

    # проверка если градуировка типа К(ХА)
    if graduation == 'K' and 500 <= value <= 1372 and coeff_type == 'T':
        K_type = True
    else:
        K_type = False

    # расчет полинома
    poly = polinom(value, coeff_coeff, K_type)

    # сбор сообщения для отправки пользователю
    result = f"{poly}({graduation})"

    return result

print(coeff_tp('N', 47.513))
print(coeff_tp('N', 1300))