from ler_instancias import ler_instancia_arquivo
import pph_algorithms as pph
import time
import os

# Aumentar o limite de recursão
import sys
sys.setrecursionlimit(100000)



# Lendo instancias:
#dir = "./testes/Lucas/Problema1/instancias"
dir = "./testes/Lucas/Problema1/PPH/"
instancias = [os.path.join(dir, instancia) for instancia in os.listdir(dir)]


for instancia in instancias:

    n, a0, b0, pares_ordenados = ler_instancia_arquivo(instancia)
    # Append a0 e b0 em pares_ordenados no inicio da lista
    pares_ordenados.insert(0, (a0, b0))
    print("N:", n)
    print("a0:", a0)
    print("b0:", b0)
    # Dividir pares_ordenados em a e b
    a = [x[0] for x in pares_ordenados]
    b = [x[1] for x in pares_ordenados]
    pph.remove_valor_zerob(a,b)

    tmp = time.time()
    conj_S = pph.q4_quickS_pivo(a,b)
    print("Conjunto S*: ", conj_S)
    print("Tempo de execução:", time.time() - tmp)
    print("R:", pph.calc_R_conjunto(conj_S, a0, b0))
    
    
    print("--------"*10)


