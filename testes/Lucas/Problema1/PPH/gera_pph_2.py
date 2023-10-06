import random
import os

def iterations(file, n, multiplier):
    count = 0
    iterations = 0
    result = ' '

    while iterations < n:
        iterations += 1
        if count < 9 and iterations < n:
            result += str(random.randint(1, n * multiplier)) + ' '
            count += 1
            continue
        else:
            result += str(random.randint(1, n * multiplier)) + ' \n'
            file.write(result)
            result = ' '
            count = 0     

    file.write(' ' + str(random.randint(1, n * multiplier)) + ' \n' )


def generate_file(n):
    dirInstances = "../instancias/"

    if not os.path.exists(dirInstances):
        os.makedirs(dirInstances)

    file_name = "pph_" + str(n) + ".dat"
    file = open( dirInstances + file_name, "w")
    file.write(str(n) + "\n")
    
    iterations(file, n, 10)
    iterations(file, n, 20)

    file.close()

def main():
    instances = [10, 20, 50, 100, 200, 500, 1000, 2000]
    for i in instances:
        generate_file(i)
    print("Arquivos gerados com sucesso!")
    
if __name__ == "__main__":
    main()