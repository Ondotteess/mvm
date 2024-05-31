import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, log


def analytical(input: (tuple[float, float], tuple[bool, bool])):
    values, conditions = input[0], input[1]
    a, b = values

    if conditions[0] == False and conditions[1] == False:
        return lambda _x: -cos(_x) + (b - a) / pi * _x + a + (b - a) / 2
    else:
        if conditions[0] == False and conditions[1] == True:
            return lambda _x: (b - 1) * _x - cos(_x) + a - (b - 1) * (-pi / 2)

        elif conditions[0] == True and conditions[1] == False:
            return lambda _x: (a + 1) * _x - cos(_x) + b - (a + 1) * (pi / 2)

        else:
            raise ValueError("there's no solution for y'(-pi/2)=a and y''(pi/2)=b")


def get_matrix(N, left, right ):
    l, r = -pi/2, pi/2
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
        d[i + 1] = d[i + 1] - (d_i / b_i) * a[i + 1]
        b[i + 1] = b[i + 1] - (c_i / b_i) * a[i + 1]

    b[n - 1] = d[n - 1] / b[n - 1]
    for i in range(n - 2, -1, -1):
        b[i] = (d[i] - c[i] * b[i + 1]) / b[i]

    return b


def bounds(n: int, is_derivative: tuple[bool, bool], values: tuple[float, float]):

    h = pi / n
    # print("is_derivative: ", is_derivative)
    # print("values: ", values)
    if is_derivative[0]:
        left = values[0]
        left_mat = [-1 / h, 1 / h, left]
    else:
        left = values[0]
        left_mat = [1, 0, left]

    if is_derivative[1]:
        right = values[1]
        right_mat = [1 / h, -1 / h, -right]
    else:
        right = values[1]
        right_mat = [0, 1, right]

    # print(left_mat)
    # print(right_mat)
    return left_mat, right_mat


def solve(N: int, input: tuple[tuple[float, float], tuple[bool, bool]]):
    is_der = input[1]
    values = input[0]
    left, right = bounds(N, is_der, values)
    a, b, c, d = get_matrix(N, left, right)
    y_approx = solve_tridiagonal(a, b, c, d)
    return y_approx



def errors(a, b, c, d, solution):
    numerical = solve_tridiagonal(a, b, c, d)
    l, r = [-pi / 2, pi / 2]
    x = np.linspace(l, r, len(numerical))
    analytical = np.array([solution(xi) for xi in x])
    error = np.abs(analytical - numerical)
    return x, error


def degree(analytical, _bounds: tuple[float, float], is_der):
    N = 2 ** 3
    l, r = bounds(N, is_der, (_bounds[0], _bounds[1]))
    a, b, c, d = get_matrix(N, l, r)
    _, error = errors(a, b, c, d, analytical)
    max1 = np.max(error)

    N *= 2
    l, r = bounds(N, is_der, (_bounds[0], _bounds[1]))
    a, b, c, d = get_matrix(N, l, r)
    _, error = errors(a, b, c, d, analytical)
    max2 = np.max(error)
    print(max1, max2)

    print("Degree: ", abs(log(max2 / max1, 2)))


def test(N: int):
    plt.title('Error between Numerical and Analytical Solution')
    plt.grid(True)

    # y(-pi/2) = 4
    # y(pi/2) = -2
    test1 = ((4, -2), (False, False))
    l_1, r_1 = bounds(N, test1[1], test1[0])
    a1, b1, c1, d1 = get_matrix(N, l_1, r_1)
    x1, error1 = errors(a1, b1, c1, d1, analytical(test1))
    plt.plot(x1, error1, label='Error for both function value')
    plt.legend()
    plt.show()


    # y'(-pi/2) = 3
    # y(pi/2) = -3
    test2 = ((3, -3), (True, False))
    l_2, r_2 = bounds(N, test2[1], test2[0])
    a2, b2, c2, d2 = get_matrix(N, l_2, r_2)
    x2, error2 = errors(a2, b2, c2, d2, analytical(test2))

    plt.plot(x2, error2, label="Error for y'(-pi/2)=3 y(pi/2)=-3")
    plt.legend()
    plt.grid(True)
    plt.show()

    # y'(-pi/2) = 7
    # y(pi/2) = -1
    test3 = ((7, -1), (False, True))
    l_2, r_2 = bounds(N, test3[1], test3[0])
    a2, b2, c2, d2 = get_matrix(N, l_2, r_2)
    x2, error2 = errors(a2, b2, c2, d2, analytical(test3))

    plt.plot(x2, error2, label="Error for y'(-pi/2)=3 y(pi/2)=-3")

    plt.legend()
    plt.grid(True)
    plt.show()

def draw(x, y_approx, y_analytical):
    plt.plot(x, y_approx, label="approx")
    plt.plot(x, y_analytical, label="analytical")
    plt.legend()
    plt.title("Analytical and approx solutions")
    plt.grid(True)
    plt.show()

N = 100
is_der = (True, False)
values = (-2, 4)

input_data = (values, is_der)

y_approx = solve(N, input_data)
analytical_solution = analytical(input_data)

x_values = np.linspace(-pi/2, pi/2, N+1)
y_analytical = [analytical_solution(x) for x in x_values]

test(N)
degree(analytical_solution, input_data[0], input_data[1])
draw(x_values, y_approx, y_analytical)
