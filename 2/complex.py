import numpy as np
import matplotlib.pyplot as plt

MAX_ITERATIONS = 1000  
EPSILON = 1e-6  

def f(z):
    return z**3 - 1

def f_prime(z):
    return 3 * z**2

def newton(z, eps=EPSILON):
    iters = 0
    while iters < MAX_ITERATIONS:
        if abs(f_prime(z)) < eps:
            return None
        z -= f(z) / f_prime(z)
        iters += 1
    return z

def generate_initial_points(n_points=100, radius=1.5):
    points = []
    for theta in np.linspace(0, 2 * np.pi, n_points):
        points.append(radius * np.exp(1j * theta))
    return points

def find_all_roots():
    roots = set()
    initial_points = generate_initial_points()
    for point in initial_points:
        root = newton(point)
        if root:
            roots.add(round(root.real, 6) + round(root.imag, 6) * 1j)
    return roots

def plot_newton_basins(roots):
    x_min, x_max = -2, 2
    y_min, y_max = -2, 2
    n_points = 1000
    X = np.linspace(x_min, x_max, n_points)
    Y = np.linspace(y_min, y_max, n_points)
    X, Y = np.meshgrid(X, Y)
    Z = X + 1j * Y

    basin_colors = np.zeros_like(Z, dtype=int)

    for i in range(Z.shape[0]):
        for j in range(Z.shape[1]):
            root = newton(Z[i, j])
            if root in roots:
                basin_colors[i, j] = list(roots).index(root) + 1

    plt.figure(figsize=(10, 8))
    plt.imshow(basin_colors, extent=(x_min, x_max, y_min, y_max), cmap='jet', origin='lower', alpha=0.9)
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.show()

if __name__ == "__main__":
    roots = find_all_roots()
    print("Roots found:", roots)
    plot_newton_basins(roots)


