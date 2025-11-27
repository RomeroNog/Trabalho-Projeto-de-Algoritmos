#Problema da Mochila Fracionária (Fractional Knapsack Problem)
#Utilizar um algoritmo guloso (pesquisar sobre o problema)
#fonte base: https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/mochila-frac.html
#Cada objeto tem pesoe valor, posso escolher uma fração do objeto
#Amochila tem uma capacidade máxima de peso
#Objetivo: maximizar o valor total na mochila
#Podendo ser resolvido com algoritmo guloso, escolhendo os itens com maior valor por peso primeiro
#alguns itens podem acabar não entrando na mochila, pq os melhores entram primeiro e pode não sobrar espaço
#temos um vetor de itens, onde cada item é uma tupla (valor, peso) e uma capacidade máxima da mochila
#Da preferencia para objetos de maior valor por peso
def mochila_fracionária(items, capacidade):
    capacidade_ini = capacidade
    #items é uma lista de tuplas (valor, peso)
    #Key calcula o valor por peso para cada item
    #Ordena os itens pelo valor por peso em ordem decrescente
    #lambda faz valor/peso para cada item
    items_ordenados = sorted(enumerate(items), key=lambda x: x[1][0]/x[1][1], reverse=True)

    
    valor_total = 0.0  #Valor total na mochila
    itens_tomados = []   #Itens tomados (índice do item, fração tomada)
    
    for indice, (valor, peso) in items_ordenados:
        #Se a capacidade da mochila for zero, para
        if capacidade <= 0:
            break  #Mochila cheia
        #Se o peso do item for menor ou igual à capacidade restante
        if peso <= capacidade:
            #Pega o item inteiro
            valor_total += valor
            capacidade -= peso
            #cada item é usado uma vez, então a fração é 1
            itens_tomados.append((indice, 1))  #Tomou o item inteiro
        else:
            #Pega a fração do item que cabe na mochila
            fracao = capacidade / peso
            valor_total += valor * fracao
            itens_tomados.append((indice, fracao))  #Tomou uma fração do item
            capacidade = 0  #Mochila cheia

    print(f"Capacidade da mochila: {capacidade_ini}")
    print(f"Valor total obtido: {valor_total:.2f}")
    print("Itens tomados (índice, fração):")
    for indice, fracao in itens_tomados:
        valor, peso = items[indice]
        print(f"->Item {indice}: valor={valor}, peso={peso}, fração={fracao:.2f}")
        
    return valor_total, itens_tomados
#Para tester, depois pode remover
if __name__ == "__main__":
    
    items = [(80, 10), (100, 20), (120, 30)]
    capacidade = 100
    valor_total, itens_tomados = mochila_fracionária(items, capacidade)
    