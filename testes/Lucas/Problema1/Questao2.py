from ler_instancias import ler_instancia_arquivo
#from pph_alan import encontrar_S, calcular_R, calc_R_conjunto
import pph_algorithms as pph
import time
import os



# Lendo instancias:
# instancias = ["testes/Lucas/Problema1/PPH/pph_10_01.dat", "testes/Lucas/Problema1/PPH/pph_100_01.dat", "testes/Lucas/Problema1/PPH/pph_1000_01.dat", "testes/Lucas/Problema1/PPH/pph_10000_01.dat", "testes/Lucas/Problema1/PPH/pph_100000_01.dat"]
dir = "./instancias"
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
    #conj_S = pph.q2_bubble(a,b)
    #conj_S = pph.q2_insertion(a,b)
    #conj_S = pph.q2_selection(a,b)
    #conj_S = pph.q2_heapsort(a,b)
    #conj_S = pph.q2_mergesort(a,b)
    conj_S = pph.q2_quicksort(a,b)
    print("Conjunto S*: ", conj_S)
    print("Tempo de execução:", time.time() - tmp)
    print("R:", pph.calc_R_conjunto(conj_S, a0, b0))
    
    
    print("--------"*10)


