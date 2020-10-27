"""Извлечение температурных коэффициентов"""
import numpy as np

# массив температур для требуемых ТП
temperature = np.array([t for t in range(500, 1373, 1)])

# массив значений температур в mV
with open("EDS_mV.txt") as file:
    s = file.read()
t_in_mV = np.array(sorted(map(float, s.split())))
print(len(t_in_mV))

# количество коэффициентов
q_k = 6

# извлечение коэффициентов
k_poly = np.polyfit(temperature, t_in_mV, q_k)
print(k_poly)


def calc_poly(x, a):
    """расчёт полинома"""
    y = 0
    for i in range(q_k + 1):
        y += a[i] * x ** (q_k - i)
    return y


# получение mV из температуры
t = 500
t_target = calc_poly(t, k_poly)

print(t, '<—>', t_target)