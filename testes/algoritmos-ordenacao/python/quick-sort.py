def quick_sort(vetor):
    tamanho_vetor = len(vetor)

    if tamanho_vetor <= 1:
        return vetor

    pivo = vetor[-1]
    left = []
    right = []

    for i in range(tamanho_vetor - 1):
        if vetor[i] < pivo:
            left.append(vetor[i])
        else:
            right.append(vetor[i])

    return quick_sort(left) + [pivo] + quick_sort(right)

def executar_quick_sort(numero_repeticoes, vetor, tipo_instancia):
    soma_tempos = 0
    soma_consumos_memoria = 0
    media_tempos = 0
    media_consumos_memoria = 0
    tempos_quick_sort = []
    consumos_memoria_quick_sort = []

    for i in range(numero_repeticoes):
        tempo_inicial = 0
        tempo_final = 0
        memoria_inicial = 0
        memoria_final = 0

        memoria_inicial = sys.getsizeof(vetor)
        tempo_inicial = time.time()
        quick_sort(vetor.copy())
        tempo_final = time.time()
        memoria_final = sys.getsizeof(vetor)

        tempos_quick_sort.append((tempo_final - tempo_inicial) * 1000)  # Em milissegundos
        consumos_memoria_quick_sort.append(memoria_final - memoria_inicial)

    soma_tempos = sum(tempos_quick_sort)
    media_tempos = soma_tempos / numero_repeticoes

    soma_consumos_memoria = sum(consumos_memoria_quick_sort)
    media_consumos_memoria = soma_consumos_memoria / numero_repeticoes

    print(f"""
        Algoritmo: Quick Sort
        Tipo da Instância/Tamanho: {tipo_instancia}/{len(vetor)}
        Qtd. de Iterações: {numero_repeticoes}
        Média de Tempo Gasto: {media_tempos:.6f} ms
        Média de Consumo de Memória: {media_consumos_memoria:.4f} bytes
    """)
