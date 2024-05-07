from math import sin, pi, e, sqrt, log
from scipy import integrate

def func(x):
    if x == 0:
        return pi
    elif x == 1:
        return 5 * pi
    else:
        return (sin(pi*(x**5)))/(x**5*(1-x))

def func2(t):
    if t == 0:
        return 1
    x = 1/t - 1
    return e ** (-sqrt(x) + sin(x/10)) * (1/t**2)

def simpson(func, a, b, n):
    h = (b - a) / n
    result = func(a) + func(b)
    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * func(a + i * h)
        else:
            result += 4 * func(a + i * h)
    result *= h / 3
    return result

def degree(f, a, b, n):
    actual = integrate.quad(func2, a, b)[0]
    first = simpson(f, a, b, n) - actual
    second = simpson(f, a, b, n * 2) - actual
    return (abs(log(first / second, 2)))


a = 0
b = 1
n = 1000000

integral1 = simpson(func, a, b, n)
integral2 = simpson(func2, a, b, n)

print("Первый интеграл численно сам: ", integral1)
print("Второй интеграл численно сам: ", integral2)
print()
print("Первый интеграл не сам: ", integrate.quad(func, a, b)[0])
print("Второй интеграл не сам: ", integrate.quad(func2, a, b)[0])
print()
print("Порядок аппроксимации: ", degree(func2, a, b, n))
