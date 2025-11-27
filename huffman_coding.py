#Codificação de Huffman para compressão de um texto fornecido pelo usuário
#Utilizar um algoritmo guloso 
#fonte base:https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/huffman.html
#Para compactação de arquivos de texto, representá-lo por um arquivo de binário menor
#Arvore de huffman é um árvore binária em que cada nó tem dois filhos. Além disso, ignoram
#a relação de rodem (esq,dir) entre filhos. Ela pode ser ponderada, ou seja, cada nó tem um peso associado
#Usa fila de prioridade (heapq) para construir a árvore de Huffman
import heapq
from collections import Counter
#Classe para o nó da árvore de huffman
class Nohuffman:
    #Inicializa o nó
    def init_no(Nohuff, simbolo, frequencia):
        Nohuff.simbolo = simbolo #caractere
        Nohuff.frequencia = frequencia #freq do caractere ou a soma deles
        Nohuff.esquerda = None
        Nohuff.direita = None
    
    #Compara dois nós com base na freq para a fila de prioridade
    def cmp_no_freq(self, outro):
        if self.frequencia < outro.frequencia:
            return True
        else:
            return False
#simbolos: lista de símbolos (caracteres)
#probabilidades: lista de probabilidades associadas a cada símbolo
def codificacao_huffman(simbolos,probabilidades):
    #fila de prioridade (heapq)
    heap_fila = []
    #para garantir que o heap nunca precise comparar dois objetos
    cont = 0
    
    #Inicializa a fila de prioridade com os nós folha
    #zip combina os simbolos com suas probabilidades
    for i, proba in zip(simbolos,probabilidades):
        Nohuff = Nohuffman()
        Nohuff.init_no(i, proba)
        heapq.heappush(heap_fila, (Nohuff.frequencia,cont, Nohuff))
        cont+=1
    
    #Constrói a árvore de Huffman
    while len(heap_fila) > 1:
        #Remove os dois nós com menor frequência, os quais estão no topo da fila de prioridade
        freq1, _, no1 = heapq.heappop(heap_fila) #menor
        freq2, _, no2 = heapq.heappop(heap_fila) #segundo menor
        
        #Cria um novo nó com a soma das frequências para ser o pai dos dois nós removidos
        new_no = Nohuffman()
        new_no.init_no(None, freq1+freq2)
        new_no.esquerda = no1
        new_no.direita = no2
        
        #Add o novo nó de volta à fila de prioridade
        heapq.heappush(heap_fila, (new_no.frequencia,cont, new_no) )
        cont+=1
    #O nó restante na fila é a raiz da árvore de Huffman 
    #que representa o texto compactado
    return heapq.heappop(heap_fila)[2] #para retornar apenas o nó

#Gera os códigos binários para cada símbolo a partir da árvore de Huffman
def gerar_codigos_huffman(nohuff, prefixo="", codigos=None):
    #Inicializa o dicionário de códigos, se necessário
    if codigos is None:
        codigos = {}
    
    #Percorre a árvore de forma recursiva
    if nohuff is not None:
        
        #Se o nó é uma folha, atribui o código binário ao símbolo
        if nohuff.simbolo is not None:
            codigos[nohuff.simbolo] = prefixo
        #esquerda é 0 e direita é 1
        #esquerda é 0 porque é o nó com menor frequência
        if nohuff.esquerda:
            gerar_codigos_huffman(nohuff.esquerda, prefixo + "0", codigos)
        #direita é 1 porque é o nó com maior frequência
        if nohuff.direita:
            gerar_codigos_huffman(nohuff.direita, prefixo + "1", codigos)
            
    return codigos

def codificacao_huffman_texto(texto):
    #Calcula a frequência de cada caractere no texto
    freq = Counter(texto)
    total = sum(freq.values())

    #Obtém os símbolos e suas probabilidades
    simbolos = list(freq.keys())
    probabilidades = [f / total for f in freq.values()]

    #Constrói a árvore de Huffman e gera os códigos binários
    raiz = codificacao_huffman(simbolos, probabilidades)
    codigos = gerar_codigos_huffman(raiz)
    
    #Codifica o texto usando os códigos gerados
    codigo_binario_por_caractere = []
    for caractere in texto:
        codigo_binario_por_caractere.append(codigos[caractere])
    
    #join é um método de string que concatena uma lista de strings em uma única string
    texto_codificado = "".join(codigo_binario_por_caractere)

    # Printa os resultados
    print("\nCódigos de Huffman para cada caractere:")
    for s in codigos:
        print(f"'{s}': {codigos[s]}")

    print("\nTexto codificado em binário:")
    print(texto_codificado)

    # Retorna também os valores
    return codigos, texto_codificado


#Para tester, depois pode remover
if __name__ == "__main__":
    texto = input("Digite um texto para codificação Huffman: ")
    codigos, texto_codificado = codificacao_huffman_texto(texto)