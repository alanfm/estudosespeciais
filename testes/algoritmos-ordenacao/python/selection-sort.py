def selection_sort(vetor):
    tamanho_vetor = len(vetor)

    for i in range(tamanho_vetor - 1):
        menor_valor_indice = i

        for j in range(i, tamanho_vetor):
            if vetor[j] < vetor[menor_valor_indice]:
                menor_valor_indice = j

        if vetor[i] > vetor[menor_valor_indice]:
            vetor[i], vetor[menor_valor_indice] = vetor[menor_valor_indice], vetor[i]

def executar_selection_sort(numero_repeticoes, vetor, tipo_instancia):
    soma_tempos = 0
    soma_consumos_memoria = 0
    media_tempos = 0
    media_consumos_memoria = 0
    tempos_selection_sort = []
    consumos_memoria_selection_sort = []

    for i in range(numero_repeticoes):
        tempo_inicial = 0
        tempo_final = 0
        memoria_inicial = 0
        memoria_final = 0

        memoria_inicial = sys.getsizeof(vetor)
        tempo_inicial = time.time()
        selection_sort(vetor.copy())
        tempo_final = time.time()
        memoria_final = sys.getsizeof(vetor)

        tempos_selection_sort.append((tempo_final - tempo_inicial) * 1000)  # Em milissegundos
        consumos_memoria_selection_sort.append(memoria_final - memoria_inicial)

    soma_tempos = sum(tempos_selection_sort)
    media_tempos = soma_tempos / numero_repeticoes

    soma_consumos_memoria = sum(consumos_memoria_selection_sort)
    media_consumos_memoria = soma_consumos_memoria / numero_repeticoes

    print(f"""
        Algoritmo: Selection Sort
        Tipo da Instância/Tamanho: {tipo_instancia}/{len(vetor)}
        Qtd. de Iterações: {numero_repeticoes}
        Média de Tempo Gasto: {media_tempos:.6f} ms
        Média de Consumo de Memória: {media_consumos_memoria:.4f} bytes
    """)
