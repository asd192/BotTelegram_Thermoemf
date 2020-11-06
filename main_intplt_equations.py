"""Расчеты НСХ ТС и ЧЭ по ГОСТ 6651-2009"""


class Temperature:
    def Pt385(t, R0=100):
        """ Платиновые ТС и ЧЭ, α = 0,00385°С """
        A, B, C = 3.9083e-3, -5.775e-7, -4.183e-12

        if t >= 0:
            C = 0

        Rt = R0 * (1 + A * t + B * t ** 2 + C * (t - 100) * t ** 3)
        return Rt

    def Pt391(t, R0=100):
        """ Платиновые ТС и ЧЭ, α = 0,00391°С """
        A, B, C = 3.9690e-3, -5.841e-7, -4.330e-12

        if t >= 0:
            C = 0

        Rt = R0 * (1 + A * t + B * t ** 2 + C * (t - 100) * t ** 3)
        return Rt

    def Cu426(t, R0=100):
        """ Медные ТС и ЧЭ, α = 0,00426°С """
        A = 4.26e-3

        Rt = R0 * (1 + A * t)
        return Rt

    def Cu428(t, R0=100):
        """ Медные ТС и ЧЭ, α = 0,00428°С """
        A, B, C = 4.28e-3, -6.2032e-7, 8.5154e-10

        if t >= 0:
            B, C = 0, 0

        Rt = R0 * (1 + A * t + B * t * (t + 6.7) + C * t ** 3)
        return Rt

    def Ni617(t, R0=100):
        """ Никеливые ТС и ЧЭ, α = 0,00617°С """
        A, B, C = 5.4963e-3, 6.7556e-6, 9.2004e-9

        if t < 100:
            C = 0

        Rt = R0 * (1 + A * t + B * t ** 2 + C * (t - 100) * t ** 2)
        return Rt

    coeff = {'Pt385': Pt385, 'Pt391': Pt391, 'Cu426': Cu426, 'Cu428': Cu428, 'Ni617': Ni617}


class Resist:
    def Pt385(r, R0=100):
        """ Платиновые ТС и ЧЭ, α = 0,00385°С """
        A, B = 3.9083e-3, -5.775e-7
        D = (255.819, 9.1455, -2.92363, 1.7909)

        if r < R0:
            Tr = [k * (r / R0 - 1) ** (n + 1) for n, k in enumerate(D)]
            return sum(Tr)

        if r >= R0:
            Tr = ((A ** 2 - 4 * B * (1 - r / R0)) ** 0.5 - A) / (2 * B)
            return Tr

    def Pt391(r, R0=100):
        """ Платиновые ТС и ЧЭ, α = 0,00391°С """
        A, B = 3.9690e-3, -5.841e-7
        D = (251.903, 8.80035, -2.91506, 1.67611)

        if r < R0:
            Tr = [k * (r / R0 - 1) ** (n + 1) for n, k in enumerate(D)]
            return sum(Tr)

        if r >= R0:
            Tr = ((A ** 2 - 4 * B * (1 - r / R0)) ** 0.5 - A) / (2 * B)
            return Tr

    coeff = {'Pt385': Pt385, 'Pt391': Pt391}


if __name__ == "__main__":
    resist = Temperature().coeff['Pt391'](-200, 100)
    print(resist)

    resist = Resist().coeff['Pt391'](17.24, 100)
    print(resist)
