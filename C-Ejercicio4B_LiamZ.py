import math
def funcion(x):
    return x - 1 - math.exp(x)
def biseccion(f, a, b, tolerancia=1e-5):
    while (b - a) / 2 > tolerancia:
        m = (a + b) / 2
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2
a = -2
b = 0
tolerancia = 1e-5
raiz = biseccion(funcion, a, b, tolerancia)
print(f"La raíz en el intervalo [{a}, {b}] es aproximadamente {raiz:.5f}")