import random
import os
import time

def iterations(file, n, multiplier):
    count = 0
    iterations = 0
    result = ''

    while iterations < n:
        iterations += 1
        if count < 9 and iterations < n:
            result += str(random.randint(1, multiplier)) + ', '
            count += 1
            continue
        else:
            result += str(random.randint(1, multiplier)) + '\n'
            file.write(result)
            result = ''
            count = 0


def generate_file(n):
    dirInstances = "./instancias/"

    if not os.path.exists(dirInstances):
        os.makedirs(dirInstances)

    file_name = "pph_" + str(n) + ".dat"
    file = open( dirInstances + file_name, "w")
    file.write(str(n) + "\n")
    
    iterations(file, n, 500)
    iterations(file, n, 1000)

    file.close()

def main():
    instances = [100, 1000, 10000, 100000, 1000000, 10000000]
    for i in instances:
        start = time.time()
        generate_file(i)
        print("Tempo para gerar instancias: ", time.time() - start)
    print("Arquivos gerados com sucesso!")
    
if __name__ == "__main__":
    main()