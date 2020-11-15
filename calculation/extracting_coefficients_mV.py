"""Извлечение mV коэффициентов для случаев опечаток и неверных данных в ГОСТ Р 8.585-2001"""

import numpy as np

# массив температур для требуемых ТП
temperature = np.array([t for t in range(0, 2501, 1)])

# массив значений температур в mV
with open("EDS_mV.txt") as file:
    s = file.read()
t_in_mV = np.array(sorted(map(float, s.split())))
print(len(t_in_mV))

# количество коэффициентов
q_k = 7

# извлечение коэффициентов
k_poly = np.polyfit(t_in_mV, temperature, q_k)
print(k_poly)
print(list(k_poly))


def calc_poly(x, a):
    """расчёт полинома"""
    y = 0
    for i in range(q_k + 1):
        y += a[i] * x ** (q_k - i)
    return y


# получение температуры из mV
mV = 33.640
t_target = calc_poly(mV, k_poly)

print(mV, '<—>', t_target)

# print(t_in_mV)