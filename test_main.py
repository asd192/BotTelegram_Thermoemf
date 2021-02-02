""" Тестирование возращаемых значений на соответствие с ГОСТ(табличные данные).

pytest test_main.py

Точность:
    0.000 для mV(ТП)
    0.00 для Ом(ТСМ)
    0 для T(ТП, ТСМ)
"""

# TODO добавить граничные значения

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

            assert t_standard == request_user(f"{T[i]} R", False)
            assert t_standard == request_user(f"{float(T[i])}t R", False)

            assert mv_standard == request_user(f"{mV[i]} R", False)
            assert mv_standard == request_user(f"{mV[i]}r R", False)

    @pytest.mark.tp_S
    def test_S(self):
        T = (-50, 100, 250, 400, 550, 700, 850, 1000, 1150, 1300, 1450, 1600, 1750)
        mV = (-0.236, 0.646, 1.874, 3.259, 4.732, 6.275, 7.893, 9.587, 11.351, 13.159, 14.978, 16.777, 18.503)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(S)"
            mv_standard = f"{T[i]} °C(S)"

            assert t_standard == request_user(f"{T[i]} S", False)
            assert t_standard == request_user(f"{float(T[i])}t S", False)

            assert mv_standard == request_user(f"{mV[i]} S", False)
            assert mv_standard == request_user(f"{mV[i]}r S", False)

    @pytest.mark.xfail
    @pytest.mark.tp_B
    def test_B(self):
        T = (250, 400, 550, 700, 850, 1000, 1150, 1300, 1450, 1600, 1750)
        mV = (0.291, 0.787, 1.505, 2.431, 3.546, 4.834, 6.276, 7.848, 9.524, 11.263, 13.014)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(B)"
            mv_standard = f"{T[i]} °C(B)"

            assert t_standard == request_user(f"{T[i]} B", False)
            assert t_standard == request_user(f"{float(T[i])}t B", False)

            assert mv_standard == request_user(f"{mV[i]} B", False)
            assert mv_standard == request_user(f"{mV[i]}r B", False)

    @pytest.mark.tp_J
    def test_J(self):
        T = (-210, -60, 90, 240, 390, 540, 690, 840, 990, 1140)
        mV = (-8.095, -2.893, 4.726, 13.0, 21.297, 29.647, 38.512, 48.074, 57.36, 66.102)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(J)"
            mv_standard = f"{T[i]} °C(J)"

            assert t_standard == request_user(f"{T[i]} J", False)
            assert t_standard == request_user(f"{float(T[i])}t J", False)

            assert mv_standard == request_user(f"{mV[i]} J", False)
            assert mv_standard == request_user(f"{mV[i]}r J", False)

    @pytest.mark.tp_T
    def test_T(self):
        T = (-250, -195, -120, -45, 30, 105, 180, 255, 330)
        mV = (-6.181, -5.523, -3.923, -1.648, 1.196, 4.513, 8.237, 12.293, 16.624)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(T)"
            mv_standard = f"{T[i]} °C(T)"

            assert t_standard == request_user(f"{T[i]} T", False)
            assert t_standard == request_user(f"{float(T[i])}t T", False)

            assert mv_standard == request_user(f"{mV[i]} T", False)
            assert mv_standard == request_user(f"{mV[i]}r T", False)

    @pytest.mark.tp_E
    def test_E(self):
        T = (-200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)
        mV = (-8.825, -5.237, -0.0, 6.319, 13.421, 21.036, 28.946, 37.005, 45.093, 53.112, 61.017, 68.787, 76.373)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(E)"
            mv_standard = f"{T[i]} °C(E)"

            assert t_standard == request_user(f"{T[i]} E", False)
            assert t_standard == request_user(f"{float(T[i])}t E", False)

            assert mv_standard == request_user(f"{mV[i]} E", False)
            assert mv_standard == request_user(f"{mV[i]}r E", False)

    @pytest.mark.tp_K
    def test_K(self):
        T = (-200, -170, -70, 30, 130, 230, 330, 430, 530, 630, 730, 830, 930, 1030, 1130, 1230, 1330)
        mV = (
        -5.891, -5.354, -2.587, 1.203, 5.328, 9.343, 13.457, 17.667, 21.924, 26.179, 30.382, 34.501, 38.522, 42.44,
        46.249, 49.926, 53.451)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(K)"
            mv_standard = f"{T[i]} °C(K)"

            assert t_standard == request_user(f"{T[i]} K", False)
            assert t_standard == request_user(f"{float(T[i])}t K", False)

            assert mv_standard == request_user(f"{mV[i]} K", False)
            assert mv_standard == request_user(f"{mV[i]}r K", False)

    @pytest.mark.tp_N
    def test_N(self):
        T = (-200, -120, 30, 180, 330, 480, 630, 780, 930, 1080, 1230)
        mV = (-3.990, -2.808, 0.793, 5.259, 10.413, 15.984, 21.784, 27.669, 33.541, 39.326, 44.958)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(N)"
            mv_standard = f"{T[i]} °C(N)"

            assert t_standard == request_user(f"{T[i]} N", False)
            assert t_standard == request_user(f"{float(T[i])}t N", False)

            assert mv_standard == request_user(f"{mV[i]} N", False)
            assert mv_standard == request_user(f"{mV[i]}r N", False)

    @pytest.mark.xfail
    @pytest.mark.tp_A1
    def test_A1(self):
        T = (200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400)
        mV = (2.872, 6.204, 9.606, 12.934, 16.128, 19.150, 21.976, 24.593, 26.998, 29.186, 31.142, 32.856)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(A1)"
            mv_standard = f"{T[i]} °C(A1)"

            assert t_standard == request_user(f"{T[i]} A1", False)
            assert t_standard == request_user(f"{float(T[i])}t A1", False)

            assert mv_standard == request_user(f"{mV[i]} A1", False)
            assert mv_standard == request_user(f"{mV[i]}r A1", False)

    @pytest.mark.tp_A2
    def test_A2(self):
        T = (180, 360, 540, 720, 900, 1080, 1260, 1440, 1620, 1800)
        mV = (2.578, 5.594, 8.683, 11.733, 14.696, 17.53, 20.203, 22.713, 25.067, 27.232)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(A2)"
            mv_standard = f"{T[i]} °C(A2)"

            assert t_standard == request_user(f"{T[i]} A2", False)
            assert t_standard == request_user(f"{float(T[i])}t A2", False)

            assert mv_standard == request_user(f"{mV[i]} A2", False)
            assert mv_standard == request_user(f"{mV[i]}r A2", False)

    @pytest.mark.tp_A3
    def test_A3(self):
        T = (200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800)
        mV = (2.842, 6.143, 9.506, 12.805, 15.98, 18.981, 21.781, 24.382, 26.773)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(A3)"
            mv_standard = f"{T[i]} °C(A3)"

            assert t_standard == request_user(f"{T[i]} A3", False)
            assert t_standard == request_user(f"{float(T[i])}t A3", False)

            assert mv_standard == request_user(f"{mV[i]} A3", False)
            assert mv_standard == request_user(f"{mV[i]}r A3", False)

    @pytest.mark.tp_L
    def test_L(self):
        T = (-200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800)
        mV = (-9.488, -5.641, 0.0, 6.862, 14.56, 22.843, 31.492, 40.299, 49.108, 57.859, 66.466)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(L)"
            mv_standard = f"{T[i]} °C(L)"

            assert t_standard == request_user(f"{T[i]} L", False)
            assert t_standard == request_user(f"{float(T[i])}t L", False)

            assert mv_standard == request_user(f"{mV[i]} L", False)
            assert mv_standard == request_user(f"{mV[i]}r L", False)

    @pytest.mark.tp_M
    def test_M(self):
        T = (-200, -170, -140, -110, -80, -50, -20, 10, 40, 70, 100)
        mV = (-6.154, -5.573, -4.859, -4.021, -3.066, -2.0, -0.832, 0.431, 1.783, 3.216, 4.722)

        for i in range(len(T)):
            t_standard = f"{mV[i]} mV(M)"
            mv_standard = f"{T[i]} °C(M)"

            assert t_standard == request_user(f"{T[i]} M", False)
            assert t_standard == request_user(f"{float(T[i])}t M", False)

            assert mv_standard == request_user(f"{mV[i]} M", False)
            assert mv_standard == request_user(f"{mV[i]}r M", False)


@pytest.mark.TSM  # pytest -m TSM test_main.py
class TestTSM():
    @pytest.mark.M50_426
    def test_M50_426(self):
        # TODO нет точных табличных данных 50M
        T = (-50, -1, 1, 200)
        R = (39.35, 49.787, 50.213, 92.6)

        for i in range(len(T)):
            t_standard = f"{R[i]:.2f} Ом(CU426)"
            r_standard = f"{T[i]} °C(CU426)"

            assert t_standard == request_user(f"{T[i]} 50M 426", False)
            assert t_standard == request_user(f"{float(T[i])}t 50M 426", False)

            assert r_standard == request_user(f"{R[i]} 50M 426", False)
            assert r_standard == request_user(f"{R[i]}r 50M 426", False)

    @pytest.mark.M100_426
    def test_M100_426(self):
        T = (-50, -1, 1, 200)
        R = (78.7, 99.574, 100.426, 185.2)

        for i in range(len(T)):
            t_standard = f"{R[i]:.2f} Ом(CU426)"
            r_standard = f"{T[i]} °C(CU426)"

            assert t_standard == request_user(f"{T[i]} 100M 426", False)
            assert t_standard == request_user(f"{float(T[i])}t 100M 426", False)

            assert r_standard == request_user(f"{R[i]} 100M 426", False)
            assert r_standard == request_user(f"{R[i]}r 100M 426", False)

    @pytest.mark.M50_428
    def test_M50_428(self):
        # TTODO нет точных табличных данных
        T = (-180, -1, 1, 200)
        R = (10.26, 49.79, 50.21, 92.8)

        for i in range(len(T)):
            t_standard = f"{R[i]:.2f} Ом(CU428)"
            r_standard = f"{T[i]} °C(CU428)"

            assert t_standard == request_user(f"{T[i]} 50M", False)
            assert t_standard == request_user(f"{T[i]} 50M 428", False)
            assert t_standard == request_user(f"{float(T[i])}t 50M", False)
            assert t_standard == request_user(f"{float(T[i])}t 50M 428", False)

            assert r_standard == request_user(f"{R[i]} 50M", False)
            assert r_standard == request_user(f"{R[i]} 50M 428", False)
            assert r_standard == request_user(f"{R[i]}r 50M", False)
            assert r_standard == request_user(f"{R[i]}r 50M 428", False)

    @pytest.mark.M100_428
    def test_M100_428(self):
        T = (-180, -1, 1, 200)
        R = (20.53, 99.57, 100.43, 185.60)

        for i in range(len(T)):
            t_standard = f"{R[i]:.2f} Ом(CU428)"
            r_standard = f"{T[i]} °C(CU428)"

            assert t_standard == request_user(f"{T[i]} 100M", False)
            assert t_standard == request_user(f"{T[i]} 100M 428", False)
            assert t_standard == request_user(f"{float(T[i])}t 100M", False)
            assert t_standard == request_user(f"{float(T[i])}t 100M 428", False)

            assert r_standard == request_user(f"{R[i]} 100M", False)
            assert r_standard == request_user(f"{R[i]} 100M 428", False)
            assert r_standard == request_user(f"{R[i]}r 100M", False)
            assert r_standard == request_user(f"{R[i]}r 100M 428", False)

    @pytest.mark.Pt50_385
    def test_Pt50_385(self):
        # TODO нет точных табличных данных 50M
        T = (-200, -1, 1, 850)
        R = (9.26, 49.805, 50.195, 195.24)

        for i in range(len(T)):
            t_standard = f"{R[i]:.2f} Ом(PT385)"
            r_standard = f"{T[i]} °C(PT385)"

            assert t_standard == request_user(f"{T[i]} 50P 385", False)
            assert t_standard == request_user(f"{float(T[i])}t 50P 385", False)

            assert r_standard == request_user(f"{R[i]} 50P 385", False)
            assert r_standard == request_user(f"{R[i]}r 50P 385", False)

    @pytest.mark.Pt100_385
    def test_Pt100_385(self):
        T = (-200, -1, 1, 850)
        R = (18.52, 99.61, 100.39, 390.48)

        for i in range(len(T)):
            t_standard = f"{R[i]:.2f} Ом(PT385)"
            r_standard = f"{T[i]} °C(PT385)"

            assert t_standard == request_user(f"{T[i]} 100P 385", False)
            assert t_standard == request_user(f"{float(T[i])}t 100P 385", False)

            assert r_standard == request_user(f"{R[i]} 100P 385", False)
            assert r_standard == request_user(f"{R[i]}r 100P 385", False)

    @pytest.mark.Pt50_391
    def test_Pt50_391(self):
        T = (-200, -1, 1, 850)
        R = (8.62, 49.8, 50.20, 197.58)

        for i in range(len(T)):
            t_standard = f"{R[i]:.2f} Ом(PT391)"
            r_standard = f"{T[i]} °C(PT391)"

            assert t_standard == request_user(f"{T[i]} 50P", False)
            assert t_standard == request_user(f"{T[i]} 50P 391", False)
            assert t_standard == request_user(f"{float(T[i])}t 50P", False)
            assert t_standard == request_user(f"{float(T[i])}t 50P 391", False)

            assert r_standard == request_user(f"{R[i]} 50P", False)
            assert r_standard == request_user(f"{R[i]} 50P 391", False)
            assert r_standard == request_user(f"{R[i]}r 50P", False)
            assert r_standard == request_user(f"{R[i]}r 50P 391", False)

    @pytest.mark.Pt100_391
    def test_Pt100_391(self):
        T = (-200, -1, 1, 850)
        R = (17.24, 99.60, 100.40, 395.16)

        for i in range(len(T)):
            t_standard = f"{R[i]:.2f} Ом(PT391)"
            r_standard = f"{T[i]} °C(PT391)"

            assert t_standard == request_user(f"{T[i]} 100P", False)
            assert t_standard == request_user(f"{T[i]} 100P 391", False)
            assert t_standard == request_user(f"{float(T[i])}t 100P", False)
            assert t_standard == request_user(f"{float(T[i])}t 100P 391", False)

            assert r_standard == request_user(f"{R[i]} 100P", False)
            assert r_standard == request_user(f"{R[i]} 100P 391", False)
            assert r_standard == request_user(f"{R[i]}r 100P", False)
            assert r_standard == request_user(f"{R[i]}r 100P 391", False)

    @pytest.mark.Ni_100_617
    def test_Ni_100_617(self):
        T = (-60, 99, 101, 180)
        R = (69.45, 161.03, 162.41, 223.21) # 101 - 162.41!

        for i in range(len(T)):
            t_standard = f"{R[i]:.2f} Ом(NI617)"
            r_standard = f"{T[i]} °C(NI617)"

            assert t_standard == request_user(f"{T[i]} 100NI", False)
            assert t_standard == request_user(f"{T[i]} 100N", False)
            assert t_standard == request_user(f"{float(T[i])}t 100N", False)
            assert t_standard == request_user(f"{float(T[i])}t 100N", False)

            assert r_standard == request_user(f"{R[i]} 100N", False)
            assert r_standard == request_user(f"{R[i]} 100N", False)
            assert r_standard == request_user(f"{R[i]}r 100N", False)
            assert r_standard == request_user(f"{R[i]}r 100N", False)

# if platform == "linux" or platform == "linux2":
#     os.system("nano ./result_test.txt")
# elif platform == "darwin": # OS X
#     pass
# elif platform == "win32": # Windows...
#     pass
