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

def funcion(x):
    return x**3 - 7*x**2 + 14*x - 6

intervalos = [(0, 1), (1, 3.2), (3.2, 4)]
tolerancia = 1e-5

for a, b in intervalos:
    raiz = biseccion(funcion, a, b, tolerancia)
    print(f"La raíz en el intervalo [{a}, {b}] es aproximadamente {raiz:.5f}")