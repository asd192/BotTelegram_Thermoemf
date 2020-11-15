""" Тестирование возращаемых значений на соответствие с ГОСТ(табличные данные).
Точность:
    0,00 для mV(ТП) и Ом(ТСМ)
    0 для T(ТП, ТСМ)
"""
import os
from sys import platform

import pytest
from processing_user_request import request_user


# with open("result_test.txt", "w"):
#     pass
# def writing_result_errors(result_list):
#     with open("result_test.txt", "a", encoding="utf8") as file:
#         for i in result_list:
#             file.write(i + '\n')


@pytest.mark.tp  # pytest -m tp test_main.py
class TestTPT():
    @pytest.mark.tp_R
    def test_R(self):
        T = (-50, 100, 250, 400, 550, 700, 850, 1000, 1111, 1150, 1300, 1450, 1600, 1750)
        mV = (-0.226, 0.647, 1.923, 3.408, 5.021, 6.743, 8.571, 10.506, 12.0, 12.535, 14.629, 16.746, 18.849, 20.877)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(R)"
            mv_standard = f"{T[i]} °C(R)"

            assert t_standard == request_user(f"{T[i]} R")
            assert t_standard == request_user(f"{float(T[i])}t R")

            assert mv_standard == request_user(f"{mV[i]} R")
            assert mv_standard == request_user(f"{mV[i]}r R")

    @pytest.mark.tp_S
    def test_S(self):
        T = (-50, 100, 250, 400, 550, 700, 850, 1000, 1150, 1300, 1450, 1600, 1750)
        mV = (-0.236, 0.646, 1.874, 3.259, 4.732, 6.275, 7.893, 9.587, 11.351, 13.159, 14.978, 16.777, 18.503)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(S)"
            mv_standard = f"{T[i]} °C(S)"

            assert t_standard == request_user(f"{T[i]} S")
            assert t_standard == request_user(f"{float(T[i])}t S")

            assert mv_standard == request_user(f"{mV[i]} S")
            assert mv_standard == request_user(f"{mV[i]}r S")

    @pytest.mark.tp_B
    def test_B(self):
        T = (250, 400, 550, 700, 850, 1000, 1150, 1300, 1450, 1600, 1750)
        mV = (0.291, 0.787, 1.505, 2.431, 3.546, 4.834, 6.276, 7.848, 9.524, 11.263, 13.014)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(B)"
            mv_standard = f"{T[i]} °C(B)"

            assert t_standard == request_user(f"{T[i]} B")
            assert t_standard == request_user(f"{float(T[i])}t B")

            assert mv_standard == request_user(f"{mV[i]} B")
            assert mv_standard == request_user(f"{mV[i]}r B")

    @pytest.mark.tp_J
    def test_J(self):


        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(J)"
            mv_standard = f"{T[i]} °C(J)"

            assert t_standard == request_user(f"{T[i]} J")
            assert t_standard == request_user(f"{float(T[i])}t J")

            assert mv_standard == request_user(f"{mV[i]} J")
            assert mv_standard == request_user(f"{mV[i]}r J")

# if platform == "linux" or platform == "linux2":
#     os.system("nano ./result_test.txt")
# elif platform == "darwin": # OS X
#     pass
# elif platform == "win32": # Windows...
#     pass
