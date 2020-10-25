import coefficients1 as c


def calc_tp(graduation, value):
    """сборка имен ключей словаря coefficients"""
    k_interval, coeff = '', ''

    if value <= 0:
        coeff = 'Neg'
        negative = True
    if value > 0:
        coeff = 'Pos'

    if type(value) is int:
        k = f"{graduation}_type_{coeff}_kA"
        print(k)
        return c.calc_poly_kA(value, k)
    if type(value) is float:
        k = f"{graduation}_type_{coeff}_kC"
        print(k)
        return c.calc_poly_kC(value, k, negative)


print(calc_tp('K', -270))
