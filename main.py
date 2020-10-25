from coefficients import coeff


def polinom(value, coeff_coeff):
    """ Расчет полинома """
    polinom = round(sum([k * (value) ** n for n, k in enumerate(coeff_coeff)]), 3)
    return f"{polinom}"


def coeff_tp(graduation, value):
    """ Определение требуемых коэффициентов """
    # определение типа коэффициента
    if type(value) is int:
        coeff_type = 'T'
    elif type(value) is float:
        coeff_type = 'mV'

    # определение требуемых коэффициентов
    for i_coeff in coeff[graduation][coeff_type].values():
        # если значение в границах по ГОСТ
        if i_coeff[0][0] <= value <= i_coeff[0][1]:
            coeff_coeff = i_coeff[1]
            not_found = False
            break
        else:
            not_found = True

    # если значение за границами по ГОСТ
    if not_found == True:
        min_low = coeff[graduation][coeff_type]['low'][0][0]
        max_high = coeff[graduation][coeff_type]['high'][0][1]

        if value <= min_low:
            coeff_coeff = coeff[graduation][coeff_type]['low'][1]
        if value >= max_high:
            coeff_coeff = coeff[graduation][coeff_type]['high'][1]


    poly = polinom(value, coeff_coeff)

    message = 'за пределами ГОСТ'
    result = f"{poly}({graduation}) {message if not_found == True else ''}"

    return result


print(coeff_tp('L', -201))

# print(coeff['L']['T'])
# g = 'L'
# k = 'T'
# for i in coeff[g][k].values():
#     print(i[0])
