import numpy as np
import heapq

# Leitura do arquivo
def ler_dados_arquivo(nome_arquivo):
    dados = []
    with open(nome_arquivo, 'r') as arquivo:
        # percorres todas as linhas do arquivo
        for linha in arquivo:
            # iniciando na linha que começa com a letra E e a ignorando
            if linha.startswith('E'):
                valores = linha.split()[1:]
                if len(valores) == 3:
                    x, y, z = map(float, valores)
                    dados.append([x, y, z])
    return dados