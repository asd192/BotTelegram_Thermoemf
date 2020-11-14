from math import exp
from coefficients import coefficients


def polinom(value, coeff_coeff, K_Type):
    """ Расчёт полинома """
    if not K_Type:
        polinom = [k * (value) ** n for n, k in enumerate(coeff_coeff)]
    else:
        print('Type_K')
        polinom = [k * (value) ** n + (0.1185976 * exp(-0.0001183432 * ((value - 126.9686)**2))) for n, k in enumerate(coeff_coeff)]

    return f"{sum(polinom)}"


def coeff_tp(graduation, value, coeff_type):
    """ Определение требуемых коэффициентов """
    found = False
    coeff_coeff = None
    for interval, coeff in coefficients[graduation][coeff_type].items():
        if interval[0] <= value <= interval[1]:
            coeff_coeff = coeff
            found = True
            break

    if not found:
        return "Значение за пределами ГОСТ"

    # проверка если градуировка типа К(ХА)
    if graduation == 'K' and 500 <= value <= 1372 and coeff_type == 'T':
        K_type = True
    else:
        K_type = False

    # расчет полинома
    if coeff_type == 'mV':
        poly = round(float(polinom(value, coeff_coeff, K_type)))
        type_value = '°C'
    else:
        poly = round(float(polinom(value, coeff_coeff, K_type)), 3)
        type_value = 'mV'

    # сбор сообщения для отправки пользователю
    result = f"{poly} {type_value}({graduation})"

    return result

if __name__ == "__main__":
    print(coeff_tp('B', 1.975, 'mV'))
    print(coeff_tp('B', 630, 'T'))
