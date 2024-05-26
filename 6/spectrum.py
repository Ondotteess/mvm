import numpy as np
import matplotlib.pyplot as plt

def f1(t):
    return 0.1 * np.sin(15 * t) + np.cos(20.5 * t)

def f2(t):
    return np.sin(5.1 * t) + 0.002 * np.sin(5 * t)

def hann(N):
    return 0.5 * (1 - np.cos(2 * np.pi * np.arange(N) / (N - 1)))

def DFT(x, is_hann: bool):
    N = len(x)
    if is_hann:
        window = hann(N)
        x = x * window
    X = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)
    return X

T = 2 * np.pi
n = 500
is_Hann = True
display_func = False

if display_func:
    t_values = np.linspace(0, T, n, endpoint=False)
    f_values = f2(t_values)
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, f_values)
    plt.xlabel('')
    plt.ylabel('')
    plt.title('Default Function')
    plt.grid(True)
    plt.show()

    window = hann(n)
    f_values_windowed = f_values * window
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, f_values_windowed)
    plt.xlabel('')
    plt.ylabel('')
    plt.title('Han Function')
    plt.grid(True)
    plt.show()
else:
    t_values = np.linspace(0, T, n, endpoint=False)
    f_values = f1(t_values)
    transformed = DFT(f_values, is_Hann)
    power_spectrum = np.abs(transformed) ** 2

    plt.figure(figsize=(10, 6))
    plt.plot(t_values, power_spectrum)
    plt.yscale('log')
    plt.xlabel('frequency')
    plt.ylabel('power spectrum')
    plt.title('power spectrum ')
    plt.grid(True)
    plt.show()
