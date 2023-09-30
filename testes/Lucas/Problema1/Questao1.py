from ler_instancias import ler_instancia_arquivo
from pph_alan import encontrar_S, calcular_R

def bubble_sort(pares_ordenados):
    n = len(pares_ordenados)
    for i in range(n):
        for j in range(0, n-i-1):
            if razao(pares_ordenados[j][0], pares_ordenados[j][1]) > razao(pares_ordenados[j+1][0], pares_ordenados[j+1][1]):
            # if (pares_ordenados[j][0] / pares_ordenados[j][1]) > (pares_ordenados[j+1][0] / pares_ordenados[j+1][1]):
                pares_ordenados[j], pares_ordenados[j+1] = pares_ordenados[j+1], pares_ordenados[j]


def razao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')

def verificar_condicao(at, bt, R):
    return razao(at, bt) > R

def resolver_PPH(pares, a0, b0):
    S = set()  # Conjunto inicial vazio
    R = razao(a0, b0)  # Inicializa R com a0/b0

    for at, bt in pares:
        if verificar_condicao(at, bt, R):
            S.add((at, bt))  # Adiciona o par ao conjunto S
            R = razao(sum(x[0] for x in S), sum(x[1] for x in S))  # Atualiza R

    return S, R



# Lendo instancias:
instancias = ["Lucas/Problema1/PPH/instancias/pph_10_01.dat", "PPH/instancias/pph_100_01.dat", "PPH/instancias/pph_1000_01.dat", "PPH/instancias/pph_10000_01.dat", "PPH/instancias/pph_100000_01.dat"]

for instancia in instancias:

    n, a0, b0, pares_ordenados = ler_instancia_arquivo(instancia)
    print("N:", n)
    #print("Pares ordenados:", pares_ordenados)
    print("a0:", a0)
    print("b0:", b0)
    S, R = resolver_PPH(pares_ordenados, a0, b0)
    print("Conjunto S:", S)
    print("Valor R:", R)

    print("-------"*20)
    print("Valores Alan")
    R = 0
    # Dividir pares_ordenados em a e b
    a = [x[0] for x in pares_ordenados]
    b = [x[1] for x in pares_ordenados]
    conjunto_S_otimo = encontrar_S(a, b, a0, b0, R)

    print(f"Conjunto S ótimo: {conjunto_S_otimo}")
    valor_R_otimo = calcular_R(conjunto_S_otimo, a, b, a0, b0)
    print(f"Valor ótimo de R(S): {valor_R_otimo:.2f}")

    # bubble_sort(pares_ordenados)
    # print("Pares Resultantes:", pares_ordenados)
    print("-------"*20)
