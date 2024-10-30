s0 = 300
m = 0.25
g = 9.81
k = 0.1
def calculoAltura(t):
    return s0 - (m * g / k) * t + (m**2 * g / k**2) * (1 - math.exp(-k * t / m))
def biseccionTiempo(f, a, b, tolerancia=0.01):
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
b = 100
tiempo_tardado = biseccionTiempo(calculoAltura, a, b)
print(f"El tiempo que tarda en golpear el piso es aproximadamente {tiempo_tardado:.2f} segundos")