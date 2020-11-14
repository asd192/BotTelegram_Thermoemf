""" Тестирование возращаемых значений на соответствие с ГОСТ(табличные данные).
Точность:
    0,00 для mV(ТП) и Ом(ТСМ)
    0 для T(ТП, ТСМ)
"""
import pytest
from processing_user_request import request_user
from coefficients import coefficients
from main_intplt_equations import Temperature, Resist


# pytest -m tp -s -v --tb=line test_main.py
@pytest.mark.tp
class TestMainPolinom():
    tp = {
        'R': ((-50, -0.226), (0, 0.000), (1064, 11.361), (1065, 11.375), (1768, 21.101)),
        'S': ((-50, -0.236), (0, 0.000), (1064, 10.332), (1065, 10.344), (1768, 18.693)),
        'B': ((0, 0.000), (630, 1.975), (631, 1.981), (1820, 13.820)),
    }
    def test_tp(self):
        for key, value in TestMainPolinom.tp.items():
            for value in TestMainPolinom.tp[key]:
                # test 1: 20 K(верхний регистр)
                result_request_1 = request_user(f'{value[0]} {key.upper()}')
                result_my_1 = f"{round(value[1], 1)} mV({key})"
                assert result_request_1 == result_my_1, "test 1: 20 K(верхний регистр)"

                # test 2: 20 k(нижний регистр)
                result_request_2 = request_user(f'{value[0]} {key.lower()}')
                result_my_2 = f"{round(value[1], 1)} mV({key})"
                assert result_request_2 == result_my_2, "test 2: 20 k(нижний регистр)"

                # test 3: 20.0t k(плавающая точка в температуре, ключ t)
                result_request_3 = request_user(f'{float(value[0])}t {key}')
                result_my_3 = f"{round(value[1], 1)} mV({key})"
                assert result_request_3 == result_my_3, "test 3: 20.0t k(плавающая точка в температуре, ключ t)"

                print(result_request_1, result_my_1)
                print(result_request_2, result_my_2)
                print(result_request_3, result_my_3)
            print()


# print(request_user('-50 R'))