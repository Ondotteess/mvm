import numpy as np

def f1(x):
    return np.exp(-np.sqrt(x)) + np.sin(x/10)

def f(x):
    x = np.where(x == 0, 1e-4, x)
    x = np.where(x == 1, 1 - 1e-4, x)
    return np.sin(np.pi * x ** 5) / (x ** 5 * (1 - x))


def x_t(t):
    t = np.where(t == 0, 1e-4, t)
    t = np.where(t == 1, 1 - 1e-4, t)
    return t / (1 - t)

def f_inf(t):
    return f(x_t(t))


def simpson(f, a, b, n):
    if (np.isinf(b)):
        return simpson(f_inf, 0, 1, n)
    if n % 2 != 0:
        n -= 1

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    s = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2])
    return h / 3 * s

def degree(f, a, b, n):
    first = simpson(f, a, b, n)
    second = simpson(f, a, b, n*2)
    return np.log2(abs(first - 2) / abs(second - 2))


a = 0
b = 1
n = 10**3


integral_value = simpson(f, a, b, n)
print("Значение интеграла:", integral_value)

actual_value = 8.03491067543358       # n = 10**8
print(degree(f, a, b, n))
