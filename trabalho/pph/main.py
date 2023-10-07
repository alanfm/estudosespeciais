import time
import algorithms
import math
import os
import tracemalloc
import instances_reader as reader
import csv

def exec_algorithms(algorithm, a, b):
    repeat = 1
    start = time.time()
    complexity = ''
    time_max = 0
    time_min = 0
    tracemalloc.start()
    while True:
        repeat += 1
        if algorithm == 'pph':
            algorithms.q1(a, b)
            complexity = 'O(n^2)'
            reason = len(a)**2
        elif algorithm == 'pph_bubble':
            algorithms.q2_bubble(a, b)
            complexity = 'O(n^2)'
            reason = len(a)**2
        elif algorithm == 'pph_insertion':
            algorithms.q2_insertion(a, b)
            complexity = 'O(n^2)'
            reason = len(a)**2
        elif algorithm == 'pph_selection':
            algorithms.q2_selection(a, b)
            complexity = 'O(n^2)'
            reason = len(a)**2
        elif algorithm == 'pph_heapsort':
            algorithms.q2_heapsort(a, b)
            complexity = 'O(n.log(n))'
            reason = len(a) * math.log(len(a))
        elif algorithm == 'pph_mergesort':
            algorithms.q2_mergesort(a, b)
            complexity = 'O(n.log(n))'
            reason = len(a) * math.log(len(a))
        elif algorithm == 'pph_quicksort':
            algorithms.q2_quicksort(a, b)
            complexity = 'O(n.log(n))'
            reason = len(a) * math.log(len(a))
        elif algorithm == 'q3_quickselect':
            algorithms.q3_quickselect(a, b)
            complexity = 'O(n^2)'
            reason = len(a)**2
        
        if (time.time() - start) > time_max:
            time_max = time.time() - start
        
        if (time.time() - start) < time_min or time_min == 0:
            time_max = time.time() - start
        
        if time.time() - start > 5:
            break
    memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tracemalloc.clear_traces()

    cpu_time = (time.time() - start) / repeat
    return [algorithm, len(a), complexity, str(f'{cpu_time:.7f}'), reason/cpu_time, time_max, time_min, memory[1]]

def main():
    algorithms = ['pph', 'pph_bubble', 'pph_insertion', 'pph_selection', 'pph_heapsort', 'pph_mergesort', 'pph_quicksort', 'q3_quickselect']
    dir = "./instancias"
    instances = [os.path.join(dir, instance) for instance in os.listdir(dir)]
    with open('results.csv', 'w') as file:
        spamWriter = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamWriter.writerow(['algoritmo', 'tamanho', 'complexidade', 'tempo', 'razao', 'tempo_max', 'tempo_min', 'memoria'])
        
        for instance in instances:
            if (not instance.endswith(".dat")):
                    continue
            start = time.time()
            a, b = reader.read(instance)
            print("Tempo para ler instancias [" + str(len(a)) + "]:", time.time() - start)
            for algorithm in algorithms:
                print("Executando algoritmo: " + algorithm)
                spamWriter.writerow(exec_algorithms(algorithm, a, b))

if __name__ == "__main__":
    main()