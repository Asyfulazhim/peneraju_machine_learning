from scipy.fft import fft, ifft
import numpy as np

x = input("Enter the sequence (comma-separated values):\n")
x = [float(val) for val in x.split(",")]
y = fft(x)
y_inv = ifft(y)

print(f"Fourier Transform of the sequence: {y}")
print(f"Inverse Fourier Transform of the transformed sequence: {y_inv}")