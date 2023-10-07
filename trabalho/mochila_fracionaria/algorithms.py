import random

def mf_a(itens, capacidade):
    # Ordena os itens por sua relação valor/peso em ordem decrescente
    itens.sort(key=lambda x: x[1] / x[0], reverse=True)

    # Define os valores iniciais do valor total e objetos na mochila
    valor_total = 0
    objetos_mochila = []

    # Inserção de objetos na mochila
    # 1 = Objeto todo
    for peso, valor in itens:
        if capacidade >= peso:
            valor_total += valor
            objetos_mochila.append((peso, 1))
            capacidade -= peso
        else:
            fracao = capacidade / peso
            valor_total += fracao * valor
            objetos_mochila.append((peso, fracao))
            break

    # Retorna o valor total na mochila e o array de objetos na mochila,
    # atualizados
    return valor_total, objetos_mochila

class Item:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
        self.proporcao = valor / peso

def mf_b(W, itens):
    n = len(itens)  # Número de itens

    if n == 0:  # Se não houver itens
        return 0.0  # Retorna 0

    r1, r2, r3 = [], [], []  # Partições
    w1, w2, w3 = 0, 0, 0  # Pesos de cada partição
    v1 = 0.0  # Inicializa o valor

    # Escolhe um pivô aleatório para particionar os itens
    indice_pivot = random.randint(0, n - 1)

    # Particiona os itens em r1, r2, r3 comparando com a proporção do pivot
    for i in range(n):
        #Adiciona em r1 caso a proporção do item seja maior que o pivot, adiciona o peso em W1
        #e incrimenta a variável de valor
        if itens[i].proporcao > itens[indice_pivot].proporcao:
            r1.append(itens[i])
            w1 += itens[i].peso
            v1 += itens[i].valor
        #Adiciona em r2 caso a proporção do item seja igual ao pivot e incrementa o peso em w2
        elif itens[i].proporcao == itens[indice_pivot].proporcao:
            r2.append(itens[i])
            w2 += itens[i].peso
        #Adiciona em r3 caso a proporção seja menor que o pivot e incrementa o peso em w3
        else:
            r3.append(itens[i])
            w3 += itens[i].peso

    if w1 > W:  # Neste caso, os itens de r1 serão suficientes para maximizar o valor
        return mf_b(W, r1)
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
            return valor_total + mf_b(W, r3)

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