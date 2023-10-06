import numpy as np
import os
import time

def ler(instancia):
    result = np.loadtxt(instancia, dtype=np.int64, delimiter=",", skiprows=1)
    result = result.flatten()
    half = int(len(result)/2)
    a, b = result[:half], result[half:]
    return len(a), a, b


def main():
    dir = "./instancias"
    instancias = [os.path.join(dir, instancia) for instancia in os.listdir(dir)]
    for instancia in instancias:
        start = time.time()
        print(ler(instancia))
        end = time.time()
        print("Tempo para ler instancias: ", end - start)
        break

if __name__ == "__main__":
    main()