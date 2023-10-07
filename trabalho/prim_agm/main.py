import algoritmos
import ler_arquivo
import math
import numpy as np
import os
import time
import csv
import tracemalloc

def exec_algorithms(algorithm, matriz_dados):
    repeat = 1
    start = time.time()
    complexity = ''
    time_max = 0
    time_min = 0

    tracemalloc.start()
    while True:
        repeat += 1
        if algorithm == 'agm_a':
            gBin = algoritmos.GraphBin(matriz_dados)
            parentBin = gBin.prim_mst()
            gBin.print_mst_edges(parentBin)
            print('Arvore Binaria')
            complexity = 'O(n)'
            reason = len(matriz_dados[0])
        elif algorithm == 'agm_b':
            gAvl = algoritmos.GraphAVL(matriz_dados)
            parentAvl = gAvl.prim_mst()
            print('avl')
            gAvl.print_mst_edges(parentAvl)            
            complexity = 'O(n)'
            reason = len(matriz_dados[0])   
        elif algorithm == 'agm_c':
            gHeapFibonacci = algoritmos.GraphHeapFibonacci(matriz_dados)
            parent_fib = gHeapFibonacci.prim_mst_fibonacci_heap()
            print('heap fibonacci')
            gHeapFibonacci.print_mst_edges(parent_fib)
            complexity = 'O(n)'
            reason = len(matriz_dados[0])      
        
        if (time.time() - start) > time_max:
            time_max = time.time() - start
        
        if (time.time() - start) < time_min or time_min == 0:
            time_max = time.time() - start
        
        if time.time() - start > 5:
            break
    memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tracemalloc.clear_traces()

    cpu_time = (time.time() - start) / repeat
    return [algorithm, len(matriz_dados), complexity, str(f'{cpu_time:.7f}'), reason/cpu_time, time_max, time_min, memory[1]]


def main():
    algorithms = ['agm_c']
    # algorithms = ['agm_a', 'agm_b', 'agm_c']
    dirs = ["./instancias/alue", "./instancias/alut", "./instancias/dmxa"]
    instances = []

    for dir in dirs:
        instances += [os.path.join(dir, instance) for instance in os.listdir(dir) if instance.endswith(".stp")]
    
    with open('results.csv', 'w') as file:
        spamWriter = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamWriter.writerow(['algoritmo', 'tamanho', 'complexidade', 'tempo', 'razao', 'tempo_max', 'tempo_min', 'memoria'])
        
        for algorithm in algorithms:
            for instance in instances:
                start = time.time()
                matriz_dados = ler_arquivo.ler_dados_arquivo(instance)
                print(instance + ":", time.time() - start)
                print("Executando algoritmo: " + algorithm)
                spamWriter.writerow(exec_algorithms(algorithm, matriz_dados))

    # # inica o local do arquivo
    # nome_arquivo = 'alue2105.stp'
    # matriz_dados = ler_arquivo.ler_dados_arquivo(nome_arquivo)
    # matriz_dados = np.round(matriz_dados).astype(int)

    # # exemplo arvore binaria
    # gBin = algoritmos.GraphBin(matriz_dados)
    # parentBin = gBin.prim_mst()
    # gBin.print_mst_edges(parentBin)
    # print('arvore binaria')
    # # plotar a arvore, mas ainda não tá funcionando
    # # gBin.plot_mst(parentBin)

    # # exemplo avl
    # gAvl = algoritmos.GraphAVL(matriz_dados)
    # parentAvl = gAvl.prim_mst()
    # print('avl')
    # gAvl.print_mst_edges(parentAvl)
    # # plotar a arvore, mas ainda não tá funcionando
    # # gAvl.plot_mst(parentAvl)

    # # exemplo heap fibonacci
    # gHeapFibonacci = algoritmos.GraphHeapFibonacci(matriz_dados)
    # parent_fib = gHeapFibonacci.prim_mst_fibonacci_heap()
    # print('heap fibonacci')
    # gHeapFibonacci.print_mst_edges(parent_fib)
    # # plotar a arvore, mas ainda não tá funcionando
    # # gHeapFibonacci.plot_mst(parent_fib)

if __name__ == "__main__":
    main()