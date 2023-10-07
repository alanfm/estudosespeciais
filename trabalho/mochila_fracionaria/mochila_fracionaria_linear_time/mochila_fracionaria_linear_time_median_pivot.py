import random

class Item:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
        self.proporcao = valor / peso

def mf_c(W, itens):
    n = len(itens)  # Número de itens

    if n == 0:  # Se não houver itens
        return 0.0  # Retorna 0

    r1, r2, r3 = [], [], []  # Partições
    w1, w2, w3 = 0, 0, 0  # Pesos de cada partição
    v1 = 0.0  # Inicializa o valor

    # Escolhe um pivot baseado na media do somatorio das proporção vezes o inverso da quantidade de items
    soma = 0.0
    for i in range(len(itens)):
        soma += itens[i].proporcao

    pivot = soma / n 

    # Particiona os itens em r1, r2, r3 comparando com a proporção do pivot
    for i in range(n):
        #Adiciona em r1 caso a proporção do item seja maior que o pivot, adiciona o peso em W1
        #e incrimenta a variável de valor
        if itens[i].proporcao > pivot:
            r1.append(itens[i])
            w1 += itens[i].peso
            v1 += itens[i].valor
        #Adiciona em r2 caso a proporção do item seja igual ao pivot e incrementa o peso em w2
        elif itens[i].proporcao == pivot:
            r2.append(itens[i])
            w2 += itens[i].peso
        #Adiciona em r3 caso a proporção seja menor que o pivot e incrementa o peso em w3
        else:
            r3.append(itens[i])
            w3 += itens[i].peso

    if w1 > W:  # Neste caso, os itens de r1 serão suficientes para maximizar o valor
        return mf_c(W, r1)
    else:
        W -= w1 #decrementa o valor do peso a partir do que estava em w1
        valor_total = v1 #Valor total recebe todo o valor que está na primeira partição

        # Se houver itens em r2, precisamos considerá-los
        while W > 0 and r2:
            # Obtemos o item inteiro se possível
            if W - r2[-1].peso > 0: # Verifica o peso do ultimo elemento e decrementa o peso da mochila
                W -= r2[-1].peso # Decrementa o peso da mochila
                valor_total += r2[-1].valor # Adiciona o valor dessa partição no valor total
            else:
                # Obtemos a parte fracionária do item
                valor_total += W * r2[-1].proporcao #Adiciona a parte restante
                W = 0 #Esvazia w pois só restou ser adicionado uma parte do objeto
            r2.pop() #Remove o elemento de pop

        if W == 0:  # Se a mochila estiver cheia, terminamos
            return valor_total
        else:  # Se a mochila não estiver cheia, precisamos considerar os itens de r3
            return valor_total + mf_c(W, r3)

if __name__ == "__main__":
    n = 5
    capacidade = 100
    pesos = [20, 10, 30, 40, 50]
    valores = [100, 60, 120, 130, 400]

    itens = [Item(pesos[i], valores[i]) for i in range(n)]

    print('Proporção dos itens', itens[0].proporcao)
    print('Proporção dos itens', itens[1].proporcao)
    print('Proporção dos itens', itens[2].proporcao)

    valor_maximo = mf_c(capacidade, itens)
    print("Valor máximo:", valor_maximo)