export function quickSort(vetor) {
    let tamanhoVetor = vetor.length;

    if (tamanhoVetor <= 1) {
        return vetor;
    }

    const pivo = vetor[tamanhoVetor - 1];
    const left = [];
    const right = [];

    for (let i = 0; i < (tamanhoVetor-1); i++) {
        if (vetor[i] < pivo) {
            left.push(vetor[i]);
        } else {
            right.push(vetor[i]);
        }
    }

    return [...quickSort(left), pivo, ...quickSort(right)];
}

export function executarQuickSort(numeroRepeticoes, vetor, tipo_instancia) {
    let somaTempos = 0;
    let somaConsumosMemoria = 0;
    let mediaTempos = 0;
    let mediaConsumosMemoria = 0;
    let temposQuickSort = [];
    let consumosMemoriaQuickSort = [];

    for (let i = 0; i < numeroRepeticoes; i++) {
        let tempoInicial = 0;
        let tempoFinal = 0;
        let memoriaInicial = 0;
        let memoriaFinal = 0;

        memoriaInicial = process.memoryUsage().heapUsed;
        tempoInicial = performance.now().toFixed(6);
        quickSort(vetor);
        tempoFinal = performance.now().toFixed(6);
        memoriaFinal = process.memoryUsage().heapUsed;

        temposQuickSort.push((tempoFinal - tempoInicial));
        consumosMemoriaQuickSort.push((memoriaFinal - memoriaInicial));
    }

    //Cálculo da média de tempo gasto
    for (let i = 0; i < temposQuickSort.length; i++) {
        somaTempos += temposQuickSort[i];
    }
    mediaTempos = (somaTempos / temposQuickSort.length);

    //Cálculo da média de consumo de memória
    for (let i = 0; i < consumosMemoriaQuickSort.length; i++) {
        somaConsumosMemoria += consumosMemoriaQuickSort[i];
    }
    mediaConsumosMemoria = (somaConsumosMemoria / consumosMemoriaQuickSort.length);

    //Log de saída
    console.log(`
        Algoritmo: Quick Sort
        Tipo da Instância/Tamanho: ${tipo_instancia}/${vetor.length}
        Qtd. de Iterações: ${numeroRepeticoes}
        Média de Tempo Gasto: ${mediaTempos.toFixed(6)} ms
        Média de Consumo de Memória: ${mediaConsumosMemoria.toFixed(4)} bytes
    `);
}
