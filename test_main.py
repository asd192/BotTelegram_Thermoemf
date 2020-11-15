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

        # табличные данные T ГОСТ Р 8.585-2001
        tp_t = {
            'R': ((-50, -0.226), (0, 0.0), (1064, 11.361), (1065, 11.375), (1664, 19.732), (1665, 19.746), (1768, 21.101)),
            'S': ((-50, -0.236), (0, 0.0), (1064, 10.332), (1065, 10.344), (1664, 17.53), (1665, 17.542), (1768, 18.693)),
            'B': ((0, 0.0), (630, 1.975), (631, 1.981), (1820, 13.820)),
            'J': ((-210, -8.095), (759, 42.855), (761, 42.983), (1200, 69.553)),
            'T': ((-270, -6.258), (-1, -0.039), (0, 0.00), (1, 0.039), (400, 20.872)),
            'E': ((-270, -9.835), (-1, -0.059), (1, 0.059), (1000, 76.373)),
            'K': ((-270, -6.458), (-1, -0.039), (1, 0.039), (499, 20.602), (501, 20.687), (1372, 54.886)),
            'N': ((-270, -4.345), (-1, -0.026), (1, 0.026), (1300, 47.513)),
            'A1': ((0, 0.0), (1250, 19.876), (2500, 33.640)),
            'A2': ((0, 0.0), (900, 14.696), (1800, 27.232)),
            'A3': ((0.0), (900, 14.411), (1800, 26.773)),
            'L': ((-200, -9.488), (-1, -0.063), (1, 0.063), (800, 66.466)),
            'M': ((-200, -6.154), (100, 4.722))
        }

        errors_tp_t = []

        for key, values in tp_t.items():
            for value in values:
                standard = f"{round(value[1], 3)} mV({key})"
                result_test = f"{standard} --> ({value[0]}, {value[1]}, {key})"

                request_1 = request_user(f'{value[0]} {key.upper()}')
                if request_1 != standard:
                    print(request_1, standard, result_test)
                    errors_tp_t.append(f"{request_1} <> {result_test} --> 1-T(верхний регистр) --> {value[0]} {key.upper()}")

                request_2 = request_user(f'{value[0]} {key.lower()}')
                if request_2 != standard:
                    print(request_2, standard, result_test)
                    errors_tp_t.append(f"{request_2} <> {result_test} --> 2-T(нижний регистр) --> {value[0]} {key.lower()}")

                request_3 = request_user(f'{float(value[0])}t {key}')
                if request_3 != standard:
                    print(request_3, standard, result_test)
                    errors_tp_t.append(f"{request_3} <> {result_test} --> 3-T(число с плавающей точкой, ключ t) --> {value[0]}t {key}")

        assert len(errors_tp_t) == 0, writing_result_errors(errors_tp_t)


    @pytest.mark.tp_mv  # pytest -m tp_mv test_main.py
    def test_tp_mv(self):

        # табличные данные mV ГОСТ Р 8.585-2001
        tp_mv = {
            'R': ((-0.225, -50), (1.914, 249), (1.933, 251), (11.348, 1063), (11.375, 1065), (19.718, 1663), (19.746, 1665), (21.101, 1768)),
            'S': ((-0.236, -50), (1.865, 249), (1.882, 251), (10.320, 1063), (10.344, 1065), (17.530, 1664), (17.542, 1665), (18.693, 1768)),
            'B': ((0.289, 249), (0.291, 250), (2.424, 699), (2.437, 701), (13.820, 1820)),
        }

        errors_tp_mv = []

        for key, values in tp_mv.items():
            for value in values:
                standard = f"{value[1]} °C({key})"
                result_test = f"{standard} --> ({value[0]}, {value[1]}, {key})"

                request_1 = request_user(f'{value[0]} {key.upper()}')
                if request_1 != standard:
                    print(request_1, standard)
                    errors_tp_mv.append(f"{request_1} <> {result_test} --> 1-mV(верхний регистр) --> {value[1]} {key.upper()}")

                request_2 = request_user(f'{value[0]} {key.lower()}')
                if request_2 != standard:
                    print(request_2, standard)
                    errors_tp_mv.append(f"{request_2} <> {result_test} --> 2-mV(нижний регистр) --> {value[1]} {key.lower()}")

                request_3 = request_user(f'{value[0]}mV {key}')
                if request_3 != standard:
                    print(request_3, standard)
                    errors_tp_mv.append(f"{request_3} <> {result_test} --> 3-mV(целое число в mV, ключ mV) --> {value[1]}mV {key}")

        assert len(errors_tp_mv) == 0, writing_result_errors(errors_tp_mv)


# if platform == "linux" or platform == "linux2":
#     os.system("nano ./result_test.txt")
# elif platform == "darwin": # OS X
#     pass
# elif platform == "win32": # Windows...
#     pass
