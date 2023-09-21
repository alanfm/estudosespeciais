export function merge(left, right) {
    let vetor = [];

    while (left.length && right.length) {
        if (left[0] < right[0]) {
            vetor.push(left.shift());
        } else {
            vetor.push(right.shift());
        }
    }

    return [...vetor, ...left, ...right];
}

export function mergeSort(vetor) {
    const half = vetor.length / 2;

    if (vetor.length < 2) {
        return vetor;
    }

    const left = vetor.splice(0, half);
    return merge(mergeSort(left), mergeSort(vetor));
}

export function executarMergeSort(numeroRepeticoes, vetor, tipo_instancia) {
    let somaTempos = 0;
    let somaConsumosMemoria = 0;
    let mediaTempos = 0;
    let mediaConsumosMemoria = 0;
    let temposMergeSort = [];
    let consumosMemoriaMergeSort = [];

    for (let i = 0; i < numeroRepeticoes; i++) {
        let tempoInicial = 0;
        let tempoFinal = 0;
        let memoriaInicial = 0;
        let memoriaFinal = 0;

        memoriaInicial = process.memoryUsage().heapUsed;
        tempoInicial = performance.now().toFixed(6);
        mergeSort(vetor);
        tempoFinal = performance.now().toFixed(6);
        memoriaFinal = process.memoryUsage().heapUsed;

        temposMergeSort.push((tempoFinal - tempoInicial));
        consumosMemoriaMergeSort.push((memoriaFinal - memoriaInicial));
    }

    //Cálculo da média de tempo gasto
    for (let i = 0; i < temposMergeSort.length; i++) {
        somaTempos += temposMergeSort[i];
    }
    mediaTempos = (somaTempos / temposMergeSort.length);

    //Cálculo da média de consumo de memória
    for (let i = 0; i < consumosMemoriaMergeSort.length; i++) {
        somaConsumosMemoria += consumosMemoriaMergeSort[i];
    }
    mediaConsumosMemoria = (somaConsumosMemoria / consumosMemoriaMergeSort.length);

    //Log de saída
    console.log(`
        Algoritmo: Merge Sort
        Tipo da Instância/Tamanho: ${tipo_instancia}/${vetor.length}
        Qtd. de Iterações: ${numeroRepeticoes}
        Média de Tempo Gasto: ${mediaTempos.toFixed(6)} ms
        Média de Consumo de Memória: ${mediaConsumosMemoria.toFixed(4)} bytes
    `);
}