from math import sin, pi, e, sqrt, log

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


def degree(f, a, b, n = 50, actual = 8.0349106754): #10 ** 10 accurancy
    first = abs(simpson(f, a, b, n) - actual)
    print(first)
    second = abs(simpson(f, a, b, n * 2) - actual)
    print(second)
    return abs(log(second/first, 2))


a = 0
b = 1
n = 10**2

integral1 = simpson(func, a, b, n)
integral2 = simpson(func2, a, b, n)

print("Первый интеграл численно сам: ", integral1)
print("Второй интеграл численно сам: ", integral2, "\n")
print("Первый интеграл не сам: \t", 8.034910675416852580728551153065246161339118723845)
print("Второй интеграл не сам: \t", 2.981003452558338248839706859225181957852512448493, "\n")
print("Порядок аппроксимации: ", degree(func, a, b))
