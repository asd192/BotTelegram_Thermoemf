""" Тестирование возращаемых значений на соответствие с ГОСТ(табличные данные).
Точность:
    0,00 для mV(ТП) и Ом(ТСМ)
    0 для T(ТП, ТСМ)
"""
import pytest
from custom_req_hundler import request_user
from coefficients import coefficients
from main_intplt_equations import Temperature, Resist


@pytest.mark.tp
class TestMainPolinom():
    tp = {
        'R': ((-50, -0.226), (0, 0.000), (1064, 11.361), (1065, 11.375), (1768, 21.101)),
        'S': ((-50, -0.236), (0, 0.000), (1064, 11.507), (1065, 11.519), (1768, 18.693)),
        'B': ((0, 0.000), (630, 1.975), (631, 1.981), (1820, 13.820)),
    }
    for key, value in tp.items():
        for value in tp[key]:
            print(request_user(f'{value[0]} {key}'))


# print(request_user('-50 R'))