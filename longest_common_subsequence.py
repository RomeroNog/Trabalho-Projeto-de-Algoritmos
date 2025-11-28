# Problema da Subsequência Comum Máxima (Longest Common Subsequence)
# Utilizar Programação Dinâmica
# Para encontrar o comprimento da maior subsequência comum entre duas sequências
# Uma subsequência é uma sequência que aparece na mesma ordem relativa, mas não necessariamente contígua
# A programação dinâmica constrói uma tabela que armazena as soluções
# Usa uma matriz dp onde dp[i][j] representa o comprimento da LCS
# usando os primeiros i caracteres de S1 e os primeiros j caracteres de S2

def lcs(S1, S2):
    # m: comprimento da primeira sequência
    m = len(S1)
    # n: comprimento da segunda sequência
    n = len(S2)
    # dp: matriz de programação dinâmica
    # dp[i][j] = comprimento da LCS usando os primeiros i caracteres de S1 e j caracteres de S2
    dp = [[0] * (n + 1) for x in range(m + 1)]
    
    # Constrói a tabela dp de baixo para cima
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Se os caracteres batem, incrementa o comprimento da LCS
            # S1[i-1] e S2[j-1] porque a indexação da lista começa em 0
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Se não batem, pega o máximo entre remover um caractere de S1 ou S2
                dp[i][j] = max(dp[i - 1][j],
                               dp[i][j - 1])
    
    # dp[m][n] contém o comprimento da LCS para S1 e S2
    return dp[m][n]

# Para testar, depois pode remover
if __name__ == "__main__":
    S1 = "AGGTAB"
    S2 = "GXTXAYB"
    print(lcs(S1, S2))
    
    
    
    
    """"""
    # Problema da Subsequência Comum Máxima (Longest Common Subsequence)
# Utilizar Programação Dinâmica
# Para encontrar o comprimento da maior subsequência comum entre duas sequências
# Uma subsequência é uma sequência que aparece na mesma ordem relativa, mas não necessariamente contígua
# A programação dinâmica constrói uma tabela que armazena as soluções
# Usa uma matriz dp onde dp[i][j] representa o comprimento da LCS
# usando os primeiros i caracteres de S1 e os primeiros j caracteres de S2
    """def lcs(S1, S2):
    # m: comprimento da primeira sequência
    m = len(S1)
    # n: comprimento da segunda sequência
    n = len(S2)
    # dp: matriz de programação dinâmica
    # dp[i][j] = comprimento da LCS usando os primeiros i caracteres de S1 e j caracteres de S2
    dp = [[0] * (n + 1) for x in range(m + 1)]
    
    # Constrói a tabela dp[m+1][n+1] de baixo para cima
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Se os caracteres coincidem, incrementa o comprimento da LCS
            # S1[i-1] e S2[j-1] porque a indexação da lista começa em 0
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Se não coincidem, pega o máximo entre remover um caractere de S1 ou S2
                dp[i][j] = max(dp[i - 1][j],
                               dp[i][j - 1])
    
    # dp[m][n] contém o comprimento da LCS para S1[0..m-1] e S2[0..n-1]
    return dp[m][n], dp

# Função para reconstruir a subsequência comum máxima
def reconstruir_lcs(S1, S2, dp):
    # Começa do final da tabela
    i = len(S1)
    j = len(S2)
    lcs_str = []
    
    # Reconstrói a LCS percorrendo a tabela de trás para frente
    while i > 0 and j > 0:
        # Se os caracteres são iguais, faz parte da LCS
        if S1[i - 1] == S2[j - 1]:
            lcs_str.append(S1[i - 1])
            i -= 1
            j -= 1
        # Move na direção do maior valor
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    # Inverte a string pois foi construída de trás para frente
    return ''.join(reversed(lcs_str))

# Para testar, depois pode remover
if __name__ == "__main__":
    # Recebe as duas sequências do usuário
    print("=== Subsequência Comum Máxima (LCS) ===\n")
    S1 = input("Digite a primeira sequência: ")
    S2 = input("Digite a segunda sequência: ")
    
    # Calcula o comprimento da LCS e obtém a tabela dp
    comprimento, dp = lcs(S1, S2)
    
    # Reconstrói a subsequência comum
    subsequencia = reconstruir_lcs(S1, S2, dp)
    
    # Exibe os resultados de forma clara
    print(f"\n--- Resultados ---")
    print(f"Sequência 1: {S1}")
    print(f"Sequência 2: {S2}")
    print(f"Comprimento da LCS: {comprimento}")
    print(f"Subsequência comum máxima: {subsequencia}")
    """

    """"""