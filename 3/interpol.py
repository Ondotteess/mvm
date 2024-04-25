import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return 1 / (1 + 25 * x**2)

def lagrange_basis(x_values, i, x):
    basis = 1
    for j in range(len(x_values)):
        if j != i:
            basis *= (x - x_values[j]) / (x_values[i] - x_values[j])
    return basis

def lagrange_interpolation(x_values, y_values, x):
    result = 0
    for i in range(len(x_values)):
        result += y_values[i] * lagrange_basis(x_values, i, x)
    return result

def chebyshev_nodes(n):
    nodes = np.zeros(n)
    for i in range(n):
        nodes[i] = np.cos(np.pi * (2 * i + 1) / (2 * n))
    return nodes

x_values = np.linspace(-1, 1, 1000)

mode = "chebyshev"
#mode = "default"
for n in range(3, 11):

    if mode == "default":
        xi = np.linspace(-1, 1, n)
        yi = func(xi)
        interpolated_y = [lagrange_interpolation(xi, yi, x) for x in x_values]
        plt.figure(figsize=(8, 6))
        plt.plot(x_values, interpolated_y, label=f'Interpolated Polynomial (n={n}) - Uniform Nodes', color='blue')
        plt.plot(x_values, func(x_values), label='Original Function', color='green', linewidth=2)
        plt.scatter(xi, func(xi), color='red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Interpolated Polynomial vs Original Function (n={n})')
        plt.legend()
        plt.grid(True)
        plt.show()

    elif mode == "chebyshev":
        xi_chebyshev = chebyshev_nodes(n)
        yi_chebyshev = func(xi_chebyshev)
        interpolated_y_chebyshev = [lagrange_interpolation(xi_chebyshev, yi_chebyshev, x) for x in x_values]
        plt.figure(figsize=(8, 6))
        plt.plot(x_values, interpolated_y_chebyshev, label=f'Interpolated Polynomial (n={n}) - Chebyshev Nodes', color='blue')
        plt.plot(x_values, func(x_values), label='Original Function', color='green', linewidth=2)
        plt.scatter(xi_chebyshev, func(xi_chebyshev), color='red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Interpolated Polynomial vs Original Function (n={n}) ')
        plt.legend()
        plt.grid(True)
        plt.show()
