import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 1 / (1 + 25 * x ** 2)


def Pn(x, xi, fi):
    n = len(xi)
    result = 0
    for i in range(n):
        term = fi[i]
        for j in range(n):
            if j != i:
                term *= (x - xi[j]) / (xi[i] - xi[j])
        result += term
    return result


def chebyshev_roots(n):
    return np.cos((2 * np.arange(1, n + 1) - 1) * np.pi / (2 * n))


def difference(is_chebyshev: bool = False, show_difference: bool = True):
    plt.figure(figsize=(10, 6))

    for i in range(3, 11):
        if is_chebyshev:
            xi_cheb = chebyshev_roots(i)
        else:
            xi_cheb = np.linspace(-1, 1, i)

        fi_cheb = f(xi_cheb)
        x_values = np.linspace(-1, 1, 1000)
        y_values_Pn_cheb = Pn(x_values, xi_cheb, fi_cheb)

        if not show_difference: plt.plot(x_values, y_values_Pn_cheb, label='Pn(x) (n={})'.format(i))

        x_values_f = np.linspace(-1, 1, 1000)
        y_values_f = f(x_values_f)
        if not show_difference: plt.plot(x_values_f, y_values_f, label='f(x)', color='black')

        absolute_error = np.abs(y_values_Pn_cheb - y_values_f)
        if show_difference: plt.plot(x_values, absolute_error, label=f'|P{i}(x) - f(x)|')


    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('f(x) and Pn(x)')
    plt.legend()
    plt.grid(True)
    plt.show()


def max_errors():
    max_errors_uniform = []
    max_errors_chebyshev = []

    for i in range(3, 11):
        xi_uniform = np.linspace(-1, 1, i)
        xi_cheb = chebyshev_roots(i)

        fi_uniform = f(xi_uniform)
        fi_cheb = f(xi_cheb)

        x_values = np.linspace(-1, 1, 1000)

        y_values_Pn_uniform = Pn(x_values, xi_uniform, fi_uniform)
        y_values_Pn_cheb = Pn(x_values, xi_cheb, fi_cheb)

        absolute_errors_uniform = np.abs(y_values_Pn_uniform - f(x_values))
        absolute_errors_chebyshev = np.abs(y_values_Pn_cheb - f(x_values))

        max_errors_uniform.append(np.max(absolute_errors_uniform))
        max_errors_chebyshev.append(np.max(absolute_errors_chebyshev))

    plt.figure(figsize=(10, 6))

    plt.plot(range(3, 11), max_errors_uniform, label='Uniform Nodes')
    plt.plot(range(3, 11), max_errors_chebyshev, label='Chebyshev Nodes')

    plt.xlabel('Number of Interpolation Points')
    plt.ylabel('Max Absolute Error')
    plt.title('Max Absolute Error vs Number of Interpolation Points')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    show_error = False
    is_chebyshev = True
    show_difference = True
    if show_error:
        max_errors()
    else:
        difference(is_chebyshev, show_difference)
