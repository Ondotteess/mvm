import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, log

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
    n = len(a)

    # print("a: ", a)
    # print("b: ", b)
    # print("c: ", c)
    # print("d: ", d)

    for i in range(n - 1):
        b_i, c_i, d_i = b[i], c[i], d[i]
        d[i+1] = d[i+1] - (d_i/b_i) * a[i+1]
        b[i+1] = b[i+1] - (c_i/b_i) * a[i+1]

    b[n - 1] = d[n-1]/b[n-1]
    for i in range(n-2, -1, -1):
        b[i] = (d[i] - c[i] * b[i+1]) / b[i]

    return b

def bounds(n: int, is_derivative: tuple[bool, bool] = (False, False),
                    values: tuple[float, float] = (0, 1)):
    h = pi / n
    # print("is_derivative: ", is_derivative)
    # print("values: ", values)
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

    # print(left_mat)
    # print(right_mat)
    return left_mat, right_mat

def solve(N: int, is_der: tuple[bool, bool], values: tuple[int, int]):
    left, right = bounds(N, is_der, values)
    a, b, c, d = get_matrix(N, left, right)
    y_approx = solve_tridiagonal(a, b, c, d)
    return y_approx

def errors(a, b, c, d, solution):
    numerical = solve_tridiagonal(a, b, c, d)
    l, r = [-pi/2, pi/2]
    x = np.linspace(l, r, len(numerical))
    analytical = np.array([solution(xi) for xi in x])
    error = np.abs(analytical - numerical)
    return x, error


def degree(analytical, _bounds: tuple[float, float]):
    N = 2 ** 10
    l, r = bounds(N, (False, False), (_bounds[0], _bounds[1]))
    a, b, c, d = get_matrix(N, l, r)
    _, error = errors(a, b, c, d, analytical)
    max1 = np.max(error)

    N *= 2
    a, b, c, d = get_matrix(N, l, r)
    _, error = errors(a, b, c, d, analytical)
    max2 = np.max(error)

    print("Degree: ", abs(log(max2/max1, 2)))

def test(N: int):
    #y(-pi/2) = 4
    #y(pi/2) = -2
    # y(x) = -6x/pi - cos(x) + 1
    l_1, r_1 = bounds(N, (False, False), (4, -2))
    a1, b1, c1, d1 = get_matrix(N, l_1, r_1)
    x1, error1 = errors(a1, b1, c1, d1, lambda x: -6*x/pi - cos(x) + 1)
    plt.plot(x1, error1, label='Error for y(x) = -6x/pi - cos(x) + 1')

    # y'(-pi/2) = 3
    # y(pi/2) = -3
    # y(x) = 4x - cos(x) - 2pi - 3
    l_2, r_2 = bounds(N, (True, False), (3, -3))
    a2, b2, c2, d2 = get_matrix(N, l_2, r_2)
    x2, error2 = errors(a2, b2, c2, d2, lambda x: 4 * x - np.cos(x) - 2 * pi - 3)

    plt.plot(x2, error2, label="Error for y(x) = 4x - cos(x) - 2pi - 3")

    plt.xlabel('x')
    plt.ylabel('Error')
    plt.title('Error between Numerical and Analytical Solution')
    plt.legend()
    plt.grid(True)
    plt.show()



N = 1000
is_der = (False, False)
values = (-2, 4)

y_approx = solve(N, is_der, values)

test(N)
degree(lambda x: 6*x/pi - cos(x) + 1, (-2, 4))

x = np.linspace(-pi/2, pi/2, N + 1)
plt.plot(x, y_approx, label='y_approx')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximate Solution y(x)')
plt.legend()
plt.grid(True)
plt.show()

