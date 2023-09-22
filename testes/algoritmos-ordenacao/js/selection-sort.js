export function selectionSort(vetor) {
    let tamanhoVetor = vetor.length;

    for (let i = 0; i < (tamanhoVetor-1); i++) {
        let menorValorIndice = i;

        for (let j = i; j < tamanhoVetor; j++) {
            if(vetor[j] < vetor[menorValorIndice]) {
                menorValorIndice = j;
            }
        }

        if(vetor[i] > vetor[menorValorIndice]) {
            let auxiliar = vetor[i];
            vetor[i] = vetor[menorValorIndice];
            vetor[menorValorIndice] = auxiliar;
        }
    }
}

export function executarSelectionSort(numeroRepeticoes, vetor, tipo_instancia) {
    let somaTempos = 0;
    let somaConsumosMemoria = 0;
    let mediaTempos = 0;
    let mediaConsumosMemoria = 0;
    let temposSelectionSort = [];
    let consumosMemoriaSelectionSort = [];

    for (let i = 0; i < numeroRepeticoes; i++) {
        let tempoInicial = 0;
        let tempoFinal = 0;
        let memoriaInicial = 0;
        let memoriaFinal = 0;

        memoriaInicial = process.memoryUsage().heapUsed;
        tempoInicial = performance.now().toFixed(6);
        selectionSort(vetor);
        tempoFinal = performance.now().toFixed(6);
        memoriaFinal = process.memoryUsage().heapUsed;

        temposSelectionSort.push((tempoFinal - tempoInicial));
        consumosMemoriaSelectionSort.push((memoriaFinal - memoriaInicial));
    }

    //Cálculo da média de tempo gasto
    for (let i = 0; i < temposSelectionSort.length; i++) {
        somaTempos += temposSelectionSort[i];
    }
    mediaTempos = (somaTempos / temposSelectionSort.length);

    //Cálculo da média de consumo de memória
    for (let i = 0; i < consumosMemoriaSelectionSort.length; i++) {
        somaConsumosMemoria += consumosMemoriaSelectionSort[i];
    }
    mediaConsumosMemoria = (somaConsumosMemoria / consumosMemoriaSelectionSort.length);

    //Log de saída
    console.log(`
        Algoritmo: Selection Sort
        Tipo da Instância/Tamanho: ${tipo_instancia}/${vetor.length}
        Qtd. de Iterações: ${numeroRepeticoes}
        Média de Tempo Gasto: ${mediaTempos.toFixed(6)} ms
        Média de Consumo de Memória: ${mediaConsumosMemoria.toFixed(4)} bytes
    `);
}
