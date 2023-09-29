def mochila_fracionaria(itens, capacidade):
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

# Testando a função, mochila_fracionaria
capacidade = 50
itens = [(10, 60), (20, 100), (25, 120), ]
valor_total, objetos_mochila = mochila_fracionaria(itens, capacidade)

print(f"Valor total na mochila: {valor_total}")
print("Itens na mochila:")

for peso, fracao in objetos_mochila:
    print(f"Peso: {peso}, Fração: {fracao}")