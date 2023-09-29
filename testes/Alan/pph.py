def calcular_R(S, a, b, a0, b0):
    soma_a_t = sum(a[t] for t in S)
    soma_b_t = sum(b[t] for t in S)
    return (a0 + soma_a_t) / (b0 + soma_b_t)

def encontrar_S(a, b, a0, b0, R):
    n = len(a)
    melhor_R = 0
    melhor_S = []

    for mascara in range(1, 2**n):
        S = [t for t in range(n) if (mascara >> t) & 1]
        if all((a[t]/b[t]) > R for t in S):
            valor_R = calcular_R(S, a, b, a0, b0)
            if valor_R > melhor_R:
                melhor_R = valor_R
                melhor_S = S
    
    return melhor_S

# Dados do problema
n = 5
a = [3, 4, 2, 5, 1]
b = [1, 2, 2, 3, 1]
a0 = 2
b0 = 1
R = 1.5

# Encontrar conjunto S ótimo
conjunto_S_otimo = encontrar_S(a, b, a0, b0, R)
print(f"Conjunto S ótimo: {conjunto_S_otimo}")
valor_R_otimo = calcular_R(conjunto_S_otimo, a, b, a0, b0)
print(f"Valor ótimo de R(S): {valor_R_otimo:.2f}")