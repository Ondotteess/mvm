import numpy as np
from math import pi

def get_matrix(N, left, right, bounds = (-pi/2, pi/2)):
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
    c_ = np.zeros(n)
    d_ = np.zeros(n)

    # прямой проход
    c_[0] = c[0] / b[0]
    d_[0] = d[0] / b[0]
    for i in range(1, n):
        c_[i] = c[i] / (b[i] - a[i] * c_[i-1])
        d_[i] = (d[i] - a[i] * d_[i-1]) / (b[i] - a[i] * c_[i-1])

    # Обратный проход
    y = np.zeros(n)
    y[-1] = d_[-1]
    for i in range(n-2, -1, -1):
        y[i] = d_[i] - c_[i] * y[i+1]
    return y

def bounds(n: int):
    h = pi/n
    is_derivative = False

    if is_derivative:
        left = 1
        # TODO: left_mat = ...
    else:
        left = 1
        left_mat = [1, 0, left]

    if is_derivative:
        right = 0
        # TODO: right_mat = ...
    else:
        right = 0
        right_mat = [0, 1, right]

    return left_mat, right_mat


def solve(N):
    left, right = bounds(N)
    a, b, c, d = get_matrix(N, left, right)
    y_approx = solve_tridiagonal(a, b, c, d)

    return y_approx


N = 30
y_approx = solve(N)
print(y_approx)
