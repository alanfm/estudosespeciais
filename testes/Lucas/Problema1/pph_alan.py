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
    
    # Retorna os pares ordenados de S a partir dos indices em melhor_S
    return [(a[t], b[t]) for t in melhor_S]
    
    # return melhor_S
