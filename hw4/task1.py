# Вычислить число c заданной точностью d
# 10^(-1) ≤ d ≤10^(-10)

import math

d = 10
for i in range(1, 11):
    d *= i
    print(round(math.pi, i))
