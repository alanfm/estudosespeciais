import numpy as np

class Item:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
        self.proporcao = valor / peso

def read(instancia, algorithm):
    result = np.loadtxt(instancia, dtype=np.int64, delimiter=",", skiprows=1)
    result = result.flatten()
    half = int(len(result)/2)
    
    if algorithm != 'mf_a':
        return [Item(result[i], result[i+half]) for i in range(half)]
    
    a, b = result[:half], result[half:]
    return [(a[i], b[i]) for i in range(len(a))]