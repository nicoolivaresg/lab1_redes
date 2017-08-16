import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

frecuenciaMuestreo, info = read("lab1-1.wav")
print(frecuenciaMuestreo)

plt.plot(info)
plt.show()