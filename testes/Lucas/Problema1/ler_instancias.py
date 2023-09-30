def ler_instancia_arquivo(arquivo):
    with open(arquivo, 'r') as f:
        n = int(f.readline())

        # Lê todos os números do arquivo e os separa em uma lista. O arquivo contem varias linhas;
        # cada linha contem 10 numeros separados por espaco. execeto a linha do numero n+1 e 2*n+1
        # que contem somente um numero.
        numbers = [int(number) for line in f for number in line.split()]

        # Separa os coeficientes de a e b; Os n+1 primeiros são os coeficientes de a, os n+1 últimos são os coeficientes de b
        coef_a = numbers[:n+1]
        coef_b = numbers[n+1:]

    a0, b0 = coef_a[0], coef_b[0]  # Obtém a0 e b0
    pares = list(zip(coef_a[1:], coef_b[1:]))  # Obtém os pares (at, bt)

    return n, a0, b0, pares