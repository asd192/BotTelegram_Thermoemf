""" Тестирование возращаемых значений на соответствие с ГОСТ(табличные данные).
Точность:
    0,00 для mV(ТП) и Ом(ТСМ)
    0 для T(ТП, ТСМ)
"""
import os
from sys import platform

import pytest
from processing_user_request import request_user

with open("result_test.txt", "w"):
    pass
def writing_result_errors(result_list):
    with open("result_test.txt", "a", encoding="utf8") as file:
        for i in result_list:
            file.write(i + '\n')


@pytest.mark.tp  # pytest -m tp test_main.py
class TestMainPolinom():
    @pytest.mark.tp_t  # pytest -m tp_t test_main.py
    def test_tp_t(self):

        # TODO !!!
        tp_t = {
            'R': (-50, 0, 1064, 1065, 1664, 1665, 1768),
            'S': (-50, 0, 1064, 1065, 1664, 1665, 1768),
            'B': (250, 630, 631, 1820, 13.820),
            'J': ()
        }

        errors_tp_t = []

        for key, values in TestMainPolinom.tp.items():
            for value in values:
                standard = f"{round(value[1], 3)} mV({key})"
                result_test = f"{standard} ({value[0]}, {value[1]}, {key})"

                request_1 = request_user(f'{value[0]} {key.upper()}')
                if request_1 != standard:
                    errors_tp_t.append(f"{request_1} <> {result_test} --> 1-T(верхний регистр) --> {value[0]} {key.upper()}")

                request_2 = request_user(f'{value[0]} {key.lower()}')
                if request_2 != standard:
                    errors_tp_t.append(f"{request_2} <> {result_test} --> 2-T(нижний регистр) --> {value[0]} {key.lower()}")

                request_3 = request_user(f'{float(value[0])}t {key}')
                if request_3 != standard:
                    errors_tp_t.append(f"{request_3} <> {result_test} --> 3-T(число с плавающей точкой, ключ t) --> {float(value[0])}t {key}")

        assert len(errors_tp_t) == 0, writing_result_errors(errors_tp_t)


    @pytest.mark.tp_mv  # pytest -m tp_mv test_main.py
    def test_tp_mv(self):

        # TODO !!!
        tp_mv = {
            'R': (-0.255, 1.922, 1.924, 11.360, 11.362, 19.738, 19.740, 21.103),
            'S': (),
            'B': (),
            'J': (())
        }

        errors_tp_mv = []

        for key, values in TestMainPolinom.tp.items():
            for value in values:
                standard = f"{value[0]} °C({key})"
                result_test = f"{standard} ({value[1]}, {value[0]}, {key})"

                request_1 = request_user(f'{value[1]} {key.upper()}')
                if request_1 != standard:
                    errors_tp_mv.append(f"{request_1} <> {result_test} --> 1-mV(верхний регистр) --> {value[1]} {key.upper()}")

                request_2 = request_user(f'{value[1]} {key.lower()}')
                if request_2 != standard:
                    errors_tp_mv.append(f"{request_2} <> {result_test} --> 2-mV(нижний регистр) --> {value[1]} {key.lower()}")

                request_3 = request_user(f'{value[1]}mV {key}')
                if request_2 != standard:
                    errors_tp_mv.append(f"{request_3} <> {result_test} --> 3-mV(целое число в mV, ключ mV) --> {value[1]}mV {key}")

        assert len(errors_tp_mv) == 0, writing_result_errors(errors_tp_mv)


# if platform == "linux" or platform == "linux2":
#     os.system("nano ./result_test.txt")
# elif platform == "darwin": # OS X
#     pass
# elif platform == "win32": # Windows...
#     pass
