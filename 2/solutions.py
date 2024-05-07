from math import tan, pi, cos

CORR = 0.00001
MAX_ITERATIONS = 1_000_000

def sgn(x: float):
    if x >= 0:
        return 1
    else:
        return -1


def func(x: float) -> float:
    return tan(x) - x


def fi(x: float) -> float:
    return x - 0.001 * func(x)


def der(x: float) -> float:
    return (1 / cos(x) ** 2) - 1


def get_interval(num: int) -> tuple:
    return (num * pi) - (pi / 2 - CORR), (num * pi) + (pi / 2 - CORR)


def bisection_method(interval, epsilon=0.0001) -> tuple:  # works
    a, b = interval
    if func(a) * func(b) > 0:
        print("Error isolation")
        return ()
    iterations = 0
    while abs((b - a) / 2) > epsilon:
        midpoint = (a + b) / 2
        if func(midpoint) == 0:
            return midpoint, iterations
        elif func(midpoint) * func(a) < 0:
            b = midpoint
        else:
            a = midpoint
        iterations += 1
    root = (a + b) / 2
    return root, iterations


def iterations(num: int, interval: tuple, eps: float = 0.0000001) -> tuple:
    iters = 0

    x0 = sgn(num) * ((pi/2 - 0.1) + abs(num) * pi)
    x1 = fi(x0)

    while iters < MAX_ITERATIONS:
        x0, x1 = x1, fi(x1)
        if abs(x1 - x0) < eps:
            break
        iters += 1
    return x1, iters


def newton(num: int, interval: tuple, eps: float = 0.000001) -> tuple: # works
    if num < 0:
        x0, x1 = interval[0], interval[1]
    else:
        x0, x1 = interval[1], interval[0]

    iters = 0
    while iters < MAX_ITERATIONS:
        if der(x0) == 0:
            print("Zero division error. Derivative is 0")
            return ()
        x1 = x0 - func(x0) / der(x0)
        if abs(x0 - x1) < eps:
            break
        x0 = x1
        iters += 1

    return x1, iters


def secant(num: int, interval: tuple, eps: float = 0.0000001) -> tuple:

    x0 = sgn(num) * ((pi / 2 - CORR) + abs(num) * pi)
    x1 = x0 - sgn(num) * 0.001
    iters = 0

    while iters < MAX_ITERATIONS:
        if func(x1) - func(x0) == 0:
            return x1, iters

        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        x0, x1 = x1, x2
        iters += 1

    return x1, iters


def newton_complex():
    pass

for num in range(-15, 16):
    interval = get_interval(num)

    root_simple_iter, iterations_simple_iter = iterations(num, interval)
    root_newton, iterations_root_newton = newton(num, interval)
    root_bisection, iterations_bisection = bisection_method(interval)
    root_secnat, iterations_secnat = secant(num, interval)
    print(f"Iterations: Root = {root_simple_iter}, Iters = {iterations_simple_iter}")
    print(f"Bisection: Root = {root_bisection}, Iters = {iterations_bisection}")
    print(f"Newton: Root = {root_newton}, Iters = {iterations_root_newton}")
    print(f"Secnat: Root = {root_secnat}, Iters = {iterations_secnat}")
    print("")
