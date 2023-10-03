import random

def calcular_R(S, a, b):
    soma_a_t = sum(a[t] for t in S)
    soma_b_t = sum(b[t] for t in S)
    return (a[0] + soma_a_t) / (b[0] + soma_b_t)

def encontrar_S(a, b):
    n = len(a)
    razoes = [(a[t]/b[t], t) for t in range(n)]

    S = set()
    razao_atual = a[0] / b[0]
    soma_a_S = 0
    soma_b_S = 0

    for _, t in razoes:
        nova_razao = (soma_a_S + a[t]) / (soma_b_S + b[t])

        if nova_razao > razao_atual:
            S.add(t)
            # Questão 01 - Remover os elementos de S que não atendem o Lema
            for t in S.copy():
                if len(S) > 0 and (a[t]/b[t]) <= calcular_R(S, a, b):
                    S.discard(t)
            razao_atual = nova_razao
            soma_a_S += a[t]
            soma_b_S += b[t]
    

    return S

# Dados do problema
n = 100000
a = [random.randint(1, n+1) for _ in range(1, n+1)]
b = [random.randint(1, n+1) for _ in range(1, n+1)]
a0 = a[0]
b0 = b[0]

# Encontrar conjunto S ótimo
conjunto_S_otimo = encontrar_S(a, b)
print(f"Conjunto S ótimo: {conjunto_S_otimo}")
valor_R_otimo = calcular_R(conjunto_S_otimo, a, b)
print(f"Valor ótimo de R(S): {valor_R_otimo:.2f}")
