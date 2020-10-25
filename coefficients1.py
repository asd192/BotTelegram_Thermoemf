coefficients = {
    # от минус 200°С до 0°С
    'L_type_Neg_kA': (-5.8952244e-5, 6.3391502e-2, 6.7592964e-5, 2.0672566e-7, 5.5720884e-9, 5.7133860e-11, 3.2995593e-13, 9.9232420e-16, 1.2079584e-18),
    'L_type_Neg_kC': (1.1573067e-4, 15.884573, 4.0458554e-2, 0.3170064, 0.1666128, 5.1946958e-2, 9.5288883e-3, 1.0301283e-3, 6.0654431e-5, 1.5131878e-6),
    # от 0°С до 800°С
    'L_type_Pos_kA': (-1.8656953e-5, 6.3310975e-2, 6.0153091e-5, -8.0073134e-8, 9.6946071e-11, -3.6047289e-14, -2.4694775e-16, 4.2880341e-19, -2.0725297e-22),
    'L_type_Pos_kC': (5.18597221e-14, -1.61678388e-11, 2.25164046e-09, -1.83665676e-07, 9.63501569e-06, -3.43126373e-04, 9.26492504e-03, -2.24780770e-01, 1.57705008e+01, 1.30811184e-02),
}

def calc_poly_kC(mV=40.299, coeff='L_type_Pos_kC', negative=False):
    """расчёт T из mV"""
    if negative:
        T = sum([k * mV ** n for n, k in enumerate(coefficients[coeff])])  # < 0
    else:
        T = sum([k * mV ** (len(coefficients[coeff]) - n - 1) for n, k in enumerate(coefficients[coeff])]) # > 0

    return T


def calc_poly_kA(t=500, coeff='L_type_Pos_kA'):
    """расчёт mV из T"""
    mV = sum([k * t ** n for n, k in enumerate(coefficients[coeff])])
    return mV

if __name__ == "__main__":
    # print(calc_poly_kC(-3.554, 'K_type_Neg_kC', True))
    print(calc_poly_kA(-100, 'K_type_Neg_kA'))