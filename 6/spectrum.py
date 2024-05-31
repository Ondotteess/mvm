import numpy as np
import matplotlib.pyplot as plt
from obspy import signal
from obspy.signal.freqattributes import spectrum


def f1(t):
    return 0.1 * np.sin(15 * t) + np.cos(20.5 * t)


def f2(t):
    return np.sin(5.1 * t) + 0.002 * np.sin(9 * t)


def hann(N):
    return 0.5 * (1 - np.cos(2 * np.pi * np.arange(N) / (N - 1)))


def DFT(x, is_hann: bool):
    N = len(x)
    if is_hann:
        window = hann(N)
        x = x * window
    X = np.fft.fft(x)
    return X


def IDFT(X):
    return np.fft.ifft(X)


T = 2 * np.pi
n = 1000
is_Hann = True
display_func = False

if display_func:
    t_values = np.linspace(0, T, n, endpoint=False)
    f_values = f2(t_values)
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, f_values)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Default Function')
    plt.grid(True)
    plt.show()

    window = hann(n)
    f_values_windowed = f_values * window
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, f_values_windowed)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Windowed Function with Hann Window')
    plt.grid(True)
    plt.show()
else:
    t_values = np.linspace(0, T, n, endpoint=False)
    f_values = f2(t_values)
    transformed = DFT(f_values, is_Hann)
    power_spectrum = np.abs(transformed)
    spec = spectrum(f_values, 2* np.pi, n)

    plt.figure(figsize=(10, 6))
    freq_values = 2 * np.pi * np.arange(n) / T
    plt.plot(np.fft.fftfreq(n, T/n), power_spectrum)
    plt.yscale('log')
    plt.xlabel('Frequency')
    plt.ylabel('Power Spectrum')
    plt.title('Power Spectrum')
    plt.grid(True)
    plt.show()

    restored_values = IDFT(transformed).real

    plt.figure(figsize=(10, 6))
    plt.plot(t_values, restored_values)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Restored Function')
    plt.grid(True)
    plt.show()
