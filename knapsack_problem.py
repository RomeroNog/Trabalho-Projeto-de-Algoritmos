# Problema da Mochila Booleana (mochila 0-1 – em inglês, Knapsack Problem)
# Utilizar Programação Dinâmica
#Fonte base:https://www.ime.usp.br/~pf/analise_de_algoritmos/repository/AA-EXERCICIOS.pdf
# Para resolver o problema de maximizar o valor dos itens em uma mochila com capacidade limitada
# Cada item pode ser incluído (1) ou não incluído (0) na mochila, sem possibilidade de fracionamento
# A programação dinâmica constrói uma tabela que armazena as soluções
# Usa uma matriz dp onde dp[i][j] representa o valor máximo 
# usando os primeiros i itens com capacidade j

def mochila(capacidade, valores, pesos):
    # n: número de itens disponíveis
    n = len(pesos)
    # dp: matriz de programação dinâmica 
    # dp[i][j] = valor máximo usando os primeiros i itens com capacidade j
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Constrói a tabela dp de baixo para cima
    for i in range(n + 1):
        for j in range(capacidade + 1):

            # Se não há item ou a capacidade da mochila é 0
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                pegar = 0

                # Pega o i item se ele não passar a capacidade da mochila
                # pesos[i-1] porque a indexação da lista começa em 0
                if pesos[i - 1] <= j:
                    # Valor do item atual + valor máximo com capacidade restante
                    pegar = valores[i - 1] + dp[i - 1][j - pesos[i - 1]]

                # Não pega o i item
                # Mantém o valor máximo obtido sem incluir o item atual
                naoPegar = dp[i - 1][j]

                # Pega ou não pega o item
                dp[i][j] = max(pegar, naoPegar)

    # Retorna o valor máximo que pode ser obtido
    return dp[n][capacidade]

# Para testar, depois pode remover
if __name__ == "__main__":
    # Recebe a capacidade da mochila
    capacidade = int(input("Digite a capacidade da mochila: "))
    
    # Recebe o número de itens
    n = int(input("Digite o número de itens: "))
    
    valores = []
    pesos = []
    
    # Recebe o valor e peso de cada item
    for i in range(n):
        print(f"\nItem {i + 1}:")
        valor = int(input("  Valor: "))
        peso = int(input("  Peso: "))
        valores.append(valor)
        pesos.append(peso)
    
    # Calcula e exibe o resultado
    resultado = mochila(capacidade, valores, pesos)
    print(f"\nValor máximo que pode ser obtido: {resultado}")
    
    ####def mochila(capacidade, valores, pesos):
    #n = len(pesos)
   # dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Constrói a tabela dp[][] de baixo para cima
    #for i in range(n + 1):
      #  for j in range(capacidade + 1):

          #  # Se não há item ou a capacidade da mochila é 0
          #  if i == 0 or j == 0:
           #     dp[i][j] = 0
          #  else:
          #      pegar = 0

                # Pega o i-ésimo item se ele não exceder a capacidade da mochila
           #     if pesos[i - 1] <= j:
           #         pegar = valores[i - 1] + dp[i - 1][j - pesos[i - 1]]

                # Não pega o i-ésimo item
             #   naoPegar = dp[i - 1][j]

            #    dp[i][j] = max(pegar, naoPegar)

   # return dp[n][capacidade]

#if __name__ == "__main__":
   # valores = [1, 2, 3]
  #  pesos = [4, 5, 1]
  #  capacidade = 4
    
  #  print(mochila(capacidade, valores, pesos))
    
    
    
    
    
    ####