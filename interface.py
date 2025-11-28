import assigment_problem as ap
import huffman_coding as hc
import fractional_knapsack as fk
import knapsack_problem as kp
import longest_common_subsequence as lcs
import math
INT_MAX = 999999999

def main():
    while True:
        print("\n========= MENU DE PROBLEMAS =========")
        print("1. Problema de Atribuição (Assignment Problem)")
        print("2. Codificação de Huffman")
        print("3. Mochila Fracionária")
        print("4. Problema da Mochila (Knapsack)")
        print("5. Subsequência Comum Mais Longa (LCS)")
        print("6. Sair")
        print("======================================")
        
        escolha = input("Digite o número correspondente ao problema: ")
        
        if escolha == '1':
            matrix = ler_matriz()

            while not validacao_matriz(matrix):
                print("A matriz digitada é inválida! Digite novamente.\n")
                matrix = ler_matriz()
            
            custo, solucao = ap.associacao_tarefas(matrix)
            print("Custo mínimo:", custo)
            print("Solução (tarefa atribuída a cada agente):", solucao)
            
            
        elif escolha == '2':
            while True:
                texto = input("\nDigite o texto a ser codificado: ").strip()
                if texto == "":
                    print("\nO texto não pode ser vazio! Digite novamente.\n")
                else:
                    break

            codigos, codificado = hc.codificacao_huffman_texto(texto)

        elif escolha == '3':
            capacidade, items = verificacao_fk()
            valor_total, itens_tomados = fk.mochila_fracionária(items, capacidade)
            print(f"\nValor máximo obtido: {valor_total}")
            print(f"Itens tomados: {itens_tomados}")
            
            
        elif escolha == '4':
            kp.run_knapsack_problem()
        elif escolha == '5':
            lcs.run_longest_common_subsequence()
        elif escolha == '6':
            print("Saindo!\n")
            break
        else:
            print("Escolha inválida! Tente novamente.\n")
            continue
        continuar = input("Deseja resolver outro problema? (s/n): ")
        if continuar.lower() != 's':
            break
        
        
def ler_matriz():
    matriz = []
    print("Digite a matriz de custos linha por linha:")
    print("Exemplo de linha válida: 3 5 2 7")
    print("Digite uma linha vazia para terminar.")
    print("Os valores devem ser inteiros não negativos e menores que", INT_MAX, "\n")

    while True:
        #strip() remove espaços em branco no início e no fim
        linha = input("Linha (ou pressione Enter para terminar): ").strip()
        #Se a linha estiver vazia, termina a entrada
        if linha == "":
            break
        #Valida a linha
        linha = validacao_numero(linha)
        #Se a linha for válida, adiciona à matriz
        if linha is not False:
            matriz.append(linha)

    return matriz
    
def validacao_numero(input_str): 
    # Divide a string em partes usando espaços para separar os números
    valores_str = input_str.split()

    valores = []
    for v in valores_str:
        # Verifica se é número inteiro
        if not v.isdigit():
            print(f"'{v}' não é um número inteiro!")
            return False
        
        num = int(v)
        # Verifica se é negativo
        if num < 0:
            print(f"Valor negativo encontrado ({num}).")
            return False
        
        # Verifica se é maior que o limite
        if num >= INT_MAX:
            print(f"Valor {num} é maior ou igual ao limite permitido ({INT_MAX}).")
            return False
        
        valores.append(num)

    return valores  
def validacao_matriz(matriz):
    
    # Matriz vazia
    if len(matriz) == 0:
        print("Matriz vazia!")
        return False

    n = len(matriz)
    # Verifica se é quadrada
    for i, linha in enumerate(matriz):
        if len(linha) != n:
            print(f"A linha {i+1} tem tamanho diferente ({len(linha)}) do esperado ({n}).")
            return False

    # Verifica elementos
    for i, linha in enumerate(matriz):
        for j, v in enumerate(linha):
            #Se o elemento é inteiro
            if not isinstance(v, int):
                print(f"Elemento na posição ({i+1},{j+1}) não é inteiro.")
                return False
            #Se o valor é negativo
            if v < 0:
                print(f"Elemento negativo encontrado em ({i+1},{j+1}).")
                return False
            #Se o valor é muito grande
            if v >= INT_MAX:
                print(f"Elemento muito grande em ({i+1},{j+1}).")
                return False

    return True


def ler_inteiro_positivo(msg, maximo=INT_MAX):
    while True:
        entrada = input(msg).strip()
        if entrada == "" or not entrada.isdigit():
            print("Entrada inválida! Digite um número inteiro positivo.\n")
            continue

        valor = int(entrada)
        if valor <= 0 or valor > maximo:
            print("Valor fora do intervalo permitido!\n")
            continue

        return valor
           
def verificacao_fk():
    # Ler capacidade
    capacidade = ler_inteiro_positivo("\nDigite a capacidade máxima da mochila: ")

    # Número de itens
    numero_itens = ler_inteiro_positivo("Digite o número de itens: ")

    # Lista de itens
    itens = []
    for i in range(numero_itens):
        print(f"\n--- ITEM {i+1} ---")
        valor = ler_inteiro_positivo("Digite o valor do item: ")
        peso  = ler_inteiro_positivo("Digite o peso do item: ")
        itens.append((valor, peso))

    return capacidade, itens
           
            
            
            
            
if __name__ == "__main__":
    main()