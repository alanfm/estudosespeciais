export function insertionSort(vetor) {
    let tamanhoVetor = vetor.length;

    for (let i = 1; i < tamanhoVetor; i++) {
        let elementoAtual = vetor[i];
        let j = i-1; 

        while ((j > -1) && (elementoAtual < vetor[j])) {
            vetor[j+1] = vetor[j];
            j--;
        }

        vetor[j+1] = elementoAtual;
    }
}

export function executarInsertionSort(numeroRepeticoes, vetor, tipo_instancia) {
    let somaTempos = 0;
    let somaConsumosMemoria = 0;
    let mediaTempos = 0;
    let mediaConsumosMemoria = 0;
    let temposInsertionSort = [];
    let consumosMemoriaInsertionSort = [];

    for (let i = 0; i < numeroRepeticoes; i++) {
        let tempoInicial = 0;
        let tempoFinal = 0;
        let memoriaInicial = 0;
        let memoriaFinal = 0;

        memoriaInicial = process.memoryUsage().heapUsed;
        tempoInicial = performance.now().toFixed(6);
        insertionSort(vetor);
        tempoFinal = performance.now().toFixed(6);
        memoriaFinal = process.memoryUsage().heapUsed;

        temposInsertionSort.push((tempoFinal - tempoInicial));
        consumosMemoriaInsertionSort.push((memoriaFinal - memoriaInicial));
    }

    //Cálculo da média de tempo gasto
    for (let i = 0; i < temposInsertionSort.length; i++) {
        somaTempos += temposInsertionSort[i];
    }
    mediaTempos = (somaTempos / temposInsertionSort.length);

    //Cálculo da média de consumo de memória
    for (let i = 0; i < consumosMemoriaInsertionSort.length; i++) {
        somaConsumosMemoria += consumosMemoriaInsertionSort[i];
    }
    mediaConsumosMemoria = (somaConsumosMemoria / consumosMemoriaInsertionSort.length);

    //Log de saída
    console.log(`
        Algoritmo: Insertion Sort
        Tipo da Instância/Tamanho: ${tipo_instancia}/${vetor.length}
        Qtd. de Iterações: ${numeroRepeticoes}
        Média de Tempo Gasto: ${mediaTempos.toFixed(6)} ms
        Média de Consumo de Memória: ${mediaConsumosMemoria.toFixed(4)} bytes
    `);
}