import math
import random
import time

MaxDim = 100
Rand_Max = 100000

def seedRandom(seed):
    random.seed(seed)

def randomn():
    return random.random()

def seconds():
    return time.process_time()

def randshannon():
    global I_SEED
    I_SEED = 16807 * I_SEED

    if I_SEED < 0:
        I_SEED += 2147483647

    i = I_SEED // 32767
    j = I_SEED - i * 32767

    random = j / 32767.0

    return random

def gera_conj_int(n, n_inst):
    global I_SEED
    Dim = n
    vt = [0] * MaxDim

    I_SEED = 123456789

    print("n:", n)
    print("n_inst:", n_inst)

    cputime = seconds()

    for j in range(1, n_inst + 1):
        num = str(n)
        print("Num:", num)
        j1 = str(j // 10)
        j2 = str(j - (10 * int(j1)))
        j1 += '0'
        j2 += '0'

        file = "pph_" + num + "_" + j1 + j2 + ".dat"

        with open(file, "wt") as p_in:
            p_in.write(str(n) + "\n")

            cont = 0

            for i in range(1, n + 2):
                p_in.write(" {:.0f}".format(randshannon() * 500))
                cont += 1
                if cont == 10:
                    cont = 0
                    p_in.write("\n")

            cont = 1
            x = int(randshannon() * 1000)
            if x == 0:
                x = 117
            p_in.write("\n {}".format(x))

            for i in range(1, n + 1):
                p_in.write(" {:.0f}".format(randshannon() * 1000))
                cont += 1
                if cont == 10:
                    cont = 0
                    p_in.write("\n")

    print(" CPU Time:", seconds() - cputime)

if __name__ == "__main__":
    Dim = 0
    vt = [0] * MaxDim
    I_SEED = 123456789

    Dim = int(input("n: "))
    v = int(input("n_inst: "))
    cputime = seconds()
    gera_conj_int(Dim, v)
    print(" CPU Time:", seconds() - cputime)
