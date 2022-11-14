#  работа с функциями в Jupyter

from sympy import *
from sympy.plotting import plot
from sympy import Symbol
import matplotlib.pyplot as plt
import numpy as np

# Требуется:
# Найти точки пересечения
# Построить графики функций в одной системе координат
# Построить график обобщенной функции

x = Symbol("x")

# f(x) = x^3 - 50x и g(x) = -x^4 + 88x^2 - 241

fx = x**3 - 50*x

gx = -x**4 + 88*x**2 - 241
g1 = gx
# dx = fx - gx

dx = x**3 - 50*x - (-x**4 + 88*x**2 - 241)
d1 = dx
# dx = 𝑥4+𝑥3−88𝑥2−50𝑥+241

sx1, sx2, sx3, sx4 = solve(dx)  # получаем корни

# ищем значение y при найденных корнях sx

y1 = sx1**3 - 50 * sx1
y2 = sx2**3 - 50 * sx2
y3 = sx3**3 - 50 * sx3
y4 = sx4**3 - 50 * sx4

print(f" coordinates f(x1) = ({sx1.evalf(chop=True)}, {y1.evalf(chop=True)})")
print(f" coordinates f(x2) = ({sx2.evalf(chop=True)}, {y2.evalf(chop=True)})")
print(f" coordinates f(x3) = ({sx3.evalf(chop=True)}, {y3.evalf(chop=True)})")
print(f" coordinates f(x4) = ({sx4.evalf(chop=True)}, {y4.evalf(chop=True)})")

# plot(fx, gx) # Построить графики функций в одной системе координат - ВЫДАЕТ ОШИБКУ
# plot(dx) # Построить график обобщенной функции


x = np.arange(-10, 10.01, 0.01)

sp = plt.subplot(111)
sp.spines['left'].set_position('center')
sp.spines['bottom'].set_position('center')
plt.title(r'функции : fx + gx')

plt.plot(x, x**3 - 50*x, x, -x**4 + 88*x**2 - 241)
plt.show()

sp = plt.subplot(111)
sp.spines['left'].set_position('center')
sp.spines['bottom'].set_position('center')
plt.title(r'общая функция : dx')
plt.plot(x, x**3 - 50*x - (-x**4 + 88*x**2 - 241))
plt.show()

# end