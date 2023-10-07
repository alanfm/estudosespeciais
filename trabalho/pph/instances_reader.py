import numpy as np

def read(instancia):
    result = np.loadtxt(instancia, dtype=np.int64, delimiter=",", skiprows=1)
    result = result.flatten()
    half = int(len(result)/2)
    a, b = result[:half], result[half:]
    return a, b