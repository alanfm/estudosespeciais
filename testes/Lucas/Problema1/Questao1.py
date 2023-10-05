from ler_instancias import ler_instancia_arquivo
#from pph_alan import encontrar_S, calcular_R, calc_R_conjunto
import pph_algorithms as pph
import time

def remove_valor_zerob(a, b):
    # Quando encontrar um valor 0 em b, remove o par (a,b) da lista
    i = 0
    while(i < len(b)):
        if b[i] == 0:
            a.pop(i)
            b.pop(i)
        i += 1
    return a,b


# Lendo instancias:
instancias = ["testes/Lucas/Problema1/PPH/pph_10_01.dat", "testes/Lucas/Problema1/PPH/pph_100_01.dat", "testes/Lucas/Problema1/PPH/pph_1000_01.dat", "testes/Lucas/Problema1/PPH/pph_10000_01.dat", "testes/Lucas/Problema1/PPH/pph_100000_01.dat"]

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
    a,b = remove_valor_zerob(a,b)


    # print("Questão 1 (O(n^2))")
    # #print("Pares ordenados:", pares_ordenados)
    # print("Conjunto S*:", pph.encontrar_S(a, b, a0, b0))
    # print("Valor R*(S*):", pph.calc_R_conjunto(pph.encontrar_S(a, b, a0, b0), a0, b0))
    tempo = time.time()
    conj_S = pph.q1(a,b)
    print("Conjunto S*: ", conj_S)
    print("Tempo de execução:", time.time() - tempo)
    print("R:", pph.calc_R_conjunto(conj_S, a0, b0))
    
    
    print("--------"*10)


