#Problema de Associação de Tarefas (Assignment Problem)
#Utilizar tentativa e erro com Branch and Bound

#O branch and bound continua até a melhor solução ser encontrada
import math
import numpy as np
INT_MAX = 999999999
def associacao_tarefas(matriz):
    n = len(matriz)
    custo = np.array([INT_MAX])
    solucao = np.array([None])
    solucao_atual = np.zeros(n,dtype=int)
    
    menor_por_linha = np.zeros(n,dtype=float)
    for i in range(n):
        menor_por_linha[i] = min(matriz[i])
        
    colunas_visitadas = np.zeros(n,dtype=bool)
    tentativa_erro(matriz, 0, 0, custo, solucao,solucao_atual, menor_por_linha, colunas_visitadas)
    return custo[0],solucao[0]
    
def tentativa_erro(matriz, lin_at, custo_at, custo, solucao, solucao_atual, menor_por_linha, colunas_visitadas):
    n = len(matriz)
    #Apos percorrer todas as linhas
    if lin_at == n:
        #tualiza a melhor solução
        if custo_at < custo[0]:
            #Atualiza o custo minimo
            custo[0] = custo_at
            #recebe a solução atual
            solucao[0] = solucao_atual.copy()
        return
    
    for j in range(n):
        #Se a coluna ainda não foi visitada ele tenta alocar a tarefa
        if not colunas_visitadas[j]:
            #O custo tem recebe o custo atual mais o custo da alocação atual
            custo_temp = custo_at + matriz[lin_at][j]
            #Soma o custo atual mais o menor custo esperado para as próximas linhas restantes
            #lin_at+1 -> começa a somar da proxima linha ate o fim
            menor_custo_esperado = custo_temp + sum(menor_por_linha[lin_at+1:])
            
            if menor_custo_esperado < custo[0]:
                colunas_visitadas[j] = True
                #Seta a solução atual
                solucao_atual[lin_at] = j
                #Chama para a proxima linha
                tentativa_erro(matriz, lin_at + 1, custo_temp,custo, solucao, solucao_atual,menor_por_linha, colunas_visitadas
                )
                #Seto a coluna como não visitada para tentar outros caminhos, até que todas as possibilidades tenham sido testadas
                colunas_visitadas[j] = False
                solucao_atual[lin_at] = -1


#Para tester, depois pode remover
if __name__ == '__main__':
    matriz = [[9, 2, 7, 8],
              [6, 4, 3, 7],
              [5, 8, 1, 8],
              [7, 6, 9, 4]]
    custo, solucao = associacao_tarefas(matriz)
    print("Custo mínimo:", custo)
    print("Solução (tarefa atribuída a cada agente):", solucao)
