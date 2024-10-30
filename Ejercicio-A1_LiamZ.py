import math

L = 10
r = 1
V = 12.4
def calculoVolumen(h):
    return L * (0.5 * math.pi * r**2 - r**2 * math.asin(h / r) - h * math.sqrt(r**2 - h**2)) - V
def biseccionVolumen(f, a, b, tolerancia=0.01):
    while (b - a) / 2 > tolerancia:
        m = (a + b) / 2
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2
a = 0
b = r
profundidad = biseccionVolumen(calculoVolumen, a, b)
print(f"La profundidad del agua es aproximadamente {profundidad:.3f} cm")