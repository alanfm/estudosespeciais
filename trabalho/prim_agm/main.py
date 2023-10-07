import algoritmos
import ler_arquivo
from math import log
import numpy as np

def main():
    # inica o local do arquivo
    nome_arquivo = 'alue2105.stp'
    matriz_dados = ler_arquivo.ler_dados_arquivo(nome_arquivo)
    matriz_dados = np.round(matriz_dados).astype(int)

    # exemplo arvore binaria
    gBin = algoritmos.GraphBin(matriz_dados)
    parentBin = gBin.prim_mst()
    gBin.print_mst_edges(parentBin)
    print('arvore binaria')
    # plotar a arvore, mas ainda não tá funcionando
    # gBin.plot_mst(parentBin)

    # exemplo avl
    gAvl = algoritmos.GraphAVL(matriz_dados)
    parentAvl = gAvl.prim_mst()
    print('avl')
    gAvl.print_mst_edges(parentAvl)
    # plotar a arvore, mas ainda não tá funcionando
    # gAvl.plot_mst(parentAvl)

    # exemplo heap fibonacci
    gHeapFibonacci = algoritmos.GraphHeapFibonacci(matriz_dados)
    parent_fib = gHeapFibonacci.prim_mst_fibonacci_heap()
    print('heap fibonacci')
    gHeapFibonacci.print_mst_edges(parent_fib)
    # plotar a arvore, mas ainda não tá funcionando
    # gHeapFibonacci.plot_mst(parent_fib)

if __name__ == "__main__":
    main()