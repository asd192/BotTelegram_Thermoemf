""" Тестирование возращаемых значений на соответствие с ГОСТ(табличные данные).
Точность:
    0,000 для mV(ТП) и Ом(ТСМ)
    0 для T(ТП, ТСМ)
"""

import os
from sys import platform

import pytest
from processing_user_request import request_user


@pytest.mark.TP  # pytest -m tp test_main.py
class TestTP():
    @pytest.mark.tp_R
    def test_R(self):
        T = (-50, 100, 250, 400, 550, 700, 850, 1000, 1111, 1150, 1300, 1450, 1600, 1750)
        mV = (-0.226, 0.647, 1.923, 3.408, 5.021, 6.743, 8.571, 10.506, 12.0, 12.535, 14.629, 16.746, 18.849, 20.877)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(R)"
            mv_standard = f"{T[i]} °C(R)"

            assert t_standard == request_user(f"{T[i]} R"), "T1"
            assert t_standard == request_user(f"{float(T[i])}t R"), "T2"

            assert mv_standard == request_user(f"{mV[i]} R"), "R1"
            assert mv_standard == request_user(f"{mV[i]}r R"), "R2"

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
        T = (-210, -60, 90, 240, 390, 540, 690, 840, 990, 1140)
        mV = (-8.095, -2.893, 4.726, 13.0, 21.297, 29.647, 38.512, 48.074, 57.36, 66.102)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(J)"
            mv_standard = f"{T[i]} °C(J)"

            assert t_standard == request_user(f"{T[i]} J")
            assert t_standard == request_user(f"{float(T[i])}t J")

            assert mv_standard == request_user(f"{mV[i]} J")
            assert mv_standard == request_user(f"{mV[i]}r J")

    @pytest.mark.tp_T
    def test_T(self):
        T = (-250, -195, -120, -45, 30, 105, 180, 255, 330)
        mV = (-6.181, -5.523, -3.923, -1.648, 1.196, 4.513, 8.237, 12.293, 16.624)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(T)"
            mv_standard = f"{T[i]} °C(T)"

            assert t_standard == request_user(f"{T[i]} T")
            assert t_standard == request_user(f"{float(T[i])}t T")

            assert mv_standard == request_user(f"{mV[i]} T")
            assert mv_standard == request_user(f"{mV[i]}r T")

    @pytest.mark.tp_E
    def test_E(self):
        T = (-200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)
        mV = (-8.825, -5.237, -0.0, 6.319, 13.421, 21.036, 28.946, 37.005, 45.093, 53.112, 61.017, 68.787, 76.373)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(E)"
            mv_standard = f"{T[i]} °C(E)"

            assert t_standard == request_user(f"{T[i]} E")
            assert t_standard == request_user(f"{float(T[i])}t E")

            assert mv_standard == request_user(f"{mV[i]} E")
            assert mv_standard == request_user(f"{mV[i]}r E")

    @pytest.mark.tp_K
    def test_K(self):
        T = (-200, -170, -70, 30, 130, 230, 330, 430, 530, 630, 730, 830, 930, 1030, 1130, 1230, 1330)
        mV = (-5.891, -5.354, -2.587, 1.203, 5.328, 9.343, 13.457, 17.667, 21.924, 26.179, 30.382, 34.501, 38.522, 42.44, 46.249, 49.926, 53.451)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(K)"
            mv_standard = f"{T[i]} °C(K)"

            assert t_standard == request_user(f"{T[i]} K")
            assert t_standard == request_user(f"{float(T[i])}t K")

            assert mv_standard == request_user(f"{mV[i]} K")
            assert mv_standard == request_user(f"{mV[i]}r K")

    @pytest.mark.tp_N
    def test_N(self):
        T = (-200, -120, 30, 180, 330, 480, 630, 780, 930, 1080, 1230)
        mV = (-3.990, -2.808, 0.793, 5.259, 10.413, 15.984, 21.784, 27.669, 33.541, 39.326, 44.958)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(N)"
            mv_standard = f"{T[i]} °C(N)"

            assert t_standard == request_user(f"{T[i]} N")
            assert t_standard == request_user(f"{float(T[i])}t N")

            assert mv_standard == request_user(f"{mV[i]} N")
            assert mv_standard == request_user(f"{mV[i]}r N")

    @pytest.mark.tp_A1
    def test_A1(self):
        T = (200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400)
        mV = (2.872, 6.204, 9.606, 12.934, 16.128, 19.150, 21.976, 24.593, 26.998, 29.186, 31.142, 32.856)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(A1)"
            mv_standard = f"{T[i]} °C(A1)"

            assert t_standard == request_user(f"{T[i]} A1")
            assert t_standard == request_user(f"{float(T[i])}t A1")

            assert mv_standard == request_user(f"{mV[i]} A1")
            assert mv_standard == request_user(f"{mV[i]}r A1")

    @pytest.mark.tp_A2
    def test_A2(self):
        T = (180, 360, 540, 720, 900, 1080, 1260, 1440, 1620, 1800)
        mV = (2.578, 5.594, 8.683, 11.733, 14.696, 17.53, 20.203, 22.713, 25.067, 27.232)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(A2)"
            mv_standard = f"{T[i]} °C(A2)"

            assert t_standard == request_user(f"{T[i]} A2")
            assert t_standard == request_user(f"{float(T[i])}t A2")

            assert mv_standard == request_user(f"{mV[i]} A2")
            assert mv_standard == request_user(f"{mV[i]}r A2")
            
    @pytest.mark.tp_A3
    def test_A3(self):
        T = (200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800)
        mV = (2.842, 6.143, 9.506, 12.805, 15.98, 18.981, 21.781, 24.382, 26.773)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(A3)"
            mv_standard = f"{T[i]} °C(A3)"

            assert t_standard == request_user(f"{T[i]} A3")
            assert t_standard == request_user(f"{float(T[i])}t A3")

            assert mv_standard == request_user(f"{mV[i]} A3")
            assert mv_standard == request_user(f"{mV[i]}r A3")

    @pytest.mark.tp_L
    def test_L(self):
        T = (-200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800)
        mV = (-9.488, -5.641, 0.0, 6.862, 14.56, 22.843, 31.492, 40.299, 49.108, 57.859, 66.466)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(L)"
            mv_standard = f"{T[i]} °C(L)"

            assert t_standard == request_user(f"{T[i]} L")
            assert t_standard == request_user(f"{float(T[i])}t L")

            assert mv_standard == request_user(f"{mV[i]} L")
            assert mv_standard == request_user(f"{mV[i]}r L")
            
    @pytest.mark.tp_M
    def test_M(self):
        T = (-200, -170, -140, -110, -80, -50, -20, 10, 40, 70, 100)
        mV = (-6.154, -5.573, -4.859, -4.021, -3.066, -2.0, -0.832, 0.431, 1.783, 3.216, 4.722)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(M)"
            mv_standard = f"{T[i]} °C(M)"

            assert t_standard == request_user(f"{T[i]} M")
            assert t_standard == request_user(f"{float(T[i])}t M")

            assert mv_standard == request_user(f"{mV[i]} M")
            assert mv_standard == request_user(f"{mV[i]}r M")


@pytest.mark.TSM  # pytest -m TSM test_main.py
class TestTSM():
    @pytest.mark.M50_426
    def test_M50_426(self):
        pass

    @pytest.mark.M100_426
    def test_M100_426(self):
        pass

    @pytest.mark.M50_428
    def test_M50_428(self):
        pass

    @pytest.mark.M100_428
    def test_M100_428(self):
        T = (-180, -1, 1, 200)
        R = (20.53, 99.57, 100.43, 185.60)

        for i in range(len(T)):
            t_standard = f"{R[i]:.2f} Ом(CU428)"
            r_standard = f"{T[i]} °C(CU428)"

            assert t_standard == request_user(f"{T[i]} 100M")
            assert t_standard == request_user(f"{T[i]} 100M 428")
            assert t_standard == request_user(f"{float(T[i])}t 100M")
            assert t_standard == request_user(f"{float(T[i])}t 100M 428")

            assert r_standard == request_user(f"{R[i]} 100M")
            assert r_standard == request_user(f"{R[i]} 100M 428")
            assert r_standard == request_user(f"{R[i]}r 100M")
            assert r_standard == request_user(f"{R[i]}r 100M 428")

    @pytest.mark.Pt50
    def test_Pt50(self):
        pass

    @pytest.mark.Pt100
    def test_Pt100(self):
        pass

    @pytest.mark.Ni
    def test_Ni(self):
        pass

# if platform == "linux" or platform == "linux2":
#     os.system("nano ./result_test.txt")
# elif platform == "darwin": # OS X
#     pass
# elif platform == "win32": # Windows...
#     pass
