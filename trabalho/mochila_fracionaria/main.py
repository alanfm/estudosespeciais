import time
import math
import os
import tracemalloc
import instances_reader as reader
import csv
import algorithms

def exec_algorithms(algorithm, capacity, items):
    repeat = 1
    start = time.time()
    complexity = ''
    time_max = 0
    time_min = 0

    tracemalloc.start()
    while True:
        repeat += 1
        if algorithm == 'mf_a':
            algorithms.mf_a(items, capacity)
            complexity = 'O(n.log(n))'
            reason = len(items) * math.log(len(items))
        elif algorithm == 'mf_b':
            algorithms.mf_b(capacity, items)
            complexity = 'O(n)'
            reason = len(items)   
        elif algorithm == 'mf_c':
            algorithms.mf_c(capacity, items)
            complexity = 'O(n)'
            reason = len(items)      
        
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
    return [algorithm, len(items), complexity, str(f'{cpu_time:.7f}'), reason/cpu_time, time_max, time_min, memory[1]]

def main():
    algorithms = ['mf_a', 'mf_b', 'mf_c']
    dir = "./instancias"
    instances = [os.path.join(dir, instance) for instance in os.listdir(dir)]
    with open('results.csv', 'w') as file:
        spamWriter = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamWriter.writerow(['algoritmo', 'tamanho', 'complexidade', 'tempo', 'razao', 'tempo_max', 'tempo_min', 'memoria'])
        
        for algorithm in algorithms:
            for instance in instances:
                if (not instance.endswith(".dat")):
                        continue
                start = time.time()
                items = reader.read(instance, algorithm)
                print("Tempo para ler instancias [" + str(len(items)) + "]:", time.time() - start)
                print("Executando algoritmo: " + algorithm)
                capacity = 1000
                spamWriter.writerow(exec_algorithms(algorithm, capacity,  items))


if __name__ == "__main__":
    main()