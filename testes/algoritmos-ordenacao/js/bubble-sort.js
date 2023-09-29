export function bubbleSort(vetor) {
  let tamanhoVetor = vetor.length;

  for (let i = 0; i < (tamanhoVetor-1); i++) {
    for (let j = 0; j < (tamanhoVetor-1); j++) {
      if (vetor[j] > vetor[j + 1]) {
        let auxiliar = vetor[j];
        vetor[j] = vetor[j + 1];
        vetor[j + 1] = auxiliar;
      }
    }
  }
}

export function executarBubbleSort(numeroRepeticoes, vetor, tipo_instancia) {
  let somaTempos = 0;
  let somaConsumosMemoria = 0;
  let mediaTempos = 0;
  let mediaConsumosMemoria = 0;
  let temposBubbleSort = [];
  let consumosMemoriaBubbleSort = [];

  for (let i = 0; i < numeroRepeticoes; i++) {
    let tempoInicial = 0;
    let tempoFinal = 0;
    let memoriaInicial = 0;
    let memoriaFinal = 0;

    memoriaInicial = process.memoryUsage().heapUsed;
    tempoInicial = performance.now().toFixed(6);
    bubbleSort(vetor);
    tempoFinal = performance.now().toFixed(6);
    memoriaFinal = process.memoryUsage().heapUsed;

    temposBubbleSort.push(tempoFinal - tempoInicial);
    consumosMemoriaBubbleSort.push(memoriaFinal - memoriaInicial);
  }

  //Cálculo da média de tempo gasto
  for (let i = 0; i < temposBubbleSort.length; i++) {
    somaTempos += temposBubbleSort[i];
  }
  mediaTempos = somaTempos / temposBubbleSort.length;

  //Cálculo da média de consumo de memória
  for (let i = 0; i < consumosMemoriaBubbleSort.length; i++) {
    somaConsumosMemoria += consumosMemoriaBubbleSort[i];
  }
  mediaConsumosMemoria = somaConsumosMemoria / consumosMemoriaBubbleSort.length;

  //Log de saída
  console.log(`
        Algoritmo: Bubble Sort
        Tipo da Instância/Tamanho: ${tipo_instancia}/${vetor.length}
        Qtd. de Iterações: ${numeroRepeticoes}
        Média de Tempo Gasto: ${mediaTempos.toFixed(6)} ms
        Média de Consumo de Memória: ${mediaConsumosMemoria.toFixed(4)} bytes
    `);
}
