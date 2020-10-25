"""Извлечение mV коэффициентов"""
import numpy as np

# массив температур для требуемых ТП
temperature = np.array([t for t in range(801)])

# массив значений температур в mV
with open("L_EDS.txt") as file:
    s = file.read()
t_in_mV = np.array(sorted(map(float, s.split())))
print(len(t_in_mV))

# количество коэффициентов
q_k = 8

# извлечение коэффициентов
k_poly = np.polyfit(t_in_mV, temperature, q_k)
print(k_poly)


def calc_poly(x, a):
    """расчёт полинома"""
    y = 0
    for i in range(q_k + 1):
        y += a[i] * x ** (q_k - i)
    return y


# получение температуры из mV
mV = 40.299
t_target = calc_poly(mV, k_poly)

print(mV, '<—>', t_target)
print(type(t_target))