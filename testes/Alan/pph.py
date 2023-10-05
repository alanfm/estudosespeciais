import random

def calcular_R(S, a, b):
    soma_a_t = sum(a[t] for t in S)
    soma_b_t = sum(b[t] for t in S)
    return (a[0] + soma_a_t) / (b[0] + soma_b_t)

def encontrar_S(a, b, R):
    n = len(a)
    melhor_R = 0
    melhor_S = []

    for mascara in range(1, 2**n):
        S = [t for t in range(n) if (mascara >> t) & 1]
        print(f"Testando S = {S}")
        if all((a[t]/b[t]) > R for t in S):
            valor_R = calcular_R(S, a, b)
            if valor_R > melhor_R:
                melhor_R = valor_R
                melhor_S = S
    
    return melhor_S

# Dados do problema
n = 10
a = [random.randint(1, n+1) for _ in range(1, n+1)]
print(a)
b = [random.randint(1, n+1) for _ in range(1, n+1)]
print(b)
R = a[0] / b[0]

# Encontrar conjunto S ótimo
conjunto_S_otimo = encontrar_S(a, b, R)
print(f"Conjunto S ótimo: {conjunto_S_otimo}")
valor_R_otimo = calcular_R(conjunto_S_otimo, a, b)
print(f"Valor ótimo de R(S): {valor_R_otimo:.2f}")