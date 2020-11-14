""" Тестирование возращаемых значений на соответствие с ГОСТ(табличные данные).
Точность:
    0,00 для mV(ТП) и Ом(ТСМ)
    0 для T(ТП, ТСМ)
"""
import pytest
from processing_user_request import request_user


@pytest.mark.tp # pytest -m tp -s -v --tb=line test_main.py
class TestMainPolinom():
    tp = {
        'R': ((-50, -0.226), (0, 0.000), (1064, 11.361), (1065, 11.375), (1768, 21.101)),
        'S': ((-50, -0.236), (0, 0.000), (1064, 10.332), (1065, 10.344), (1768, 18.693)),
        'B': ((630, 1.975), (631, 1.981), (1820, 13.820)),
    }

    @pytest.mark.tp_t
    def test_tp_t(self):
        for key, values in TestMainPolinom.tp.items():
            for value in values:
                standard = f"{round(value[1], 1)} mV({key})"

                request_1 = request_user(f'{value[0]} {key.upper()}')
                assert request_1 == standard, "test 1-T: 20 K(верхний регистр)"

                request_2 = request_user(f'{value[0]} {key.lower()}')
                assert request_2 == standard, "test 2-T: 20 k(нижний регистр)"

                request_3 = request_user(f'{float(value[0])}t {key}')
                assert request_3 == standard, "test 3-T: 20.0t k(плавающая точка в температуре, ключ t)"

    @pytest.mark.tp_mv
    def test_tp_mv(self):
        for key, values in TestMainPolinom.tp.items():
            for value in values:
                standard = f"{value[0]} °C({key})"

                request_1 = request_user(f'{value[1]} {key.upper()}')
                assert request_1 == standard, "test 1-mV: 20 K(верхний регистр)"

                request_2 = request_user(f'{value[1]} {key.lower()}')
                assert request_2 == standard, "test 2-mV: 20 k(нижний регистр)"

                request_3 = request_user(f'{value[1]}mV {key}')
                assert request_3 == standard, "test 3-mV: 20mv k(без плавающей точки в mV, ключ mv)"
