import matplotlib.pyplot as plt
import numpy as np
from math import pi

def get_matrix(N, left, right, bounds=(-pi/2, pi/2)):
    l, r = bounds
    h = (r - l) / N

    a = [0]
    b = []
    c = []
    d = []

    for i in range(1, N):
        a.append(1 / h ** 2)
        b.append(-2 / h ** 2)
        c.append(1 / h ** 2)
        d.append(np.cos(l + i * h))

    c.append(0)

    b.insert(0, left[0])
    c.insert(0, left[1])
    d.insert(0, left[2])

    a.append(right[0])
    b.append(right[1])
    d.append(right[2])

    return np.array(a), np.array(b), np.array(c), np.array(d)

def solve_tridiagonal(a, b, c, d):
    n = len(d)

    p = np.zeros(n - 1)
    q = np.zeros(n)
    p[0] = c[0] / b[0]
    q[0] = d[0] / b[0]

    for i in range(1, n - 1):
        p[i] = c[i] / (b[i] - a[i - 1] * p[i - 1])

    for i in range(1, n):
        q[i] = (d[i] - a[i - 1] * q[i - 1]) / (b[i] - a[i - 1] * p[i - 1])

    y = np.zeros(n)
    y[-1] = q[-1]

    for i in range(n - 2, -1, -1):
        y[i] = q[i] - p[i] * y[i + 1]

    return y


def bounds(n: int, is_derivative: tuple[bool, bool] = (False, False),
                    values: tuple[int, int] = (0, 1)):
    h = pi / n

    if is_derivative[0]:
        left = values[0]
        left_mat = [-1/h, 1/h, left]
    else:
        left = values[0]
        left_mat = [1, 0, left]

    if is_derivative[1]:
        right = values[1]
        right_mat = [1/h, -1/h, right]
    else:
        right = values[1]
        right_mat = [0, 1, right]

    return left_mat, right_mat

def solve(N: int, is_der: tuple[bool, bool], values: tuple[int, int]):
    left, right = bounds(N, is_der, values)
    a, b, c, d = get_matrix(N, left, right)
    y_approx = solve_tridiagonal(a, b, c, d)
    return y_approx

N = 1000
is_der = (True, False)
values = (1, 0)

y_approx = solve(N, is_der, values)

x = np.linspace(-pi/2, pi/2, N + 1)
plt.plot(x, y_approx, label='y_approx')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximate Solution y(x)')
plt.legend()
plt.grid(True)
plt.show()
