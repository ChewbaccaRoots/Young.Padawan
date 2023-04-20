#criar matriz parte 1

def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)

        matriz.append(linha)

    return matriz
        
#criar matriz parte 2 (com quebas de linha):

def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(str(valor))
        matriz.append(linha)
    return '\n'.join([' '.join(linha) for linha in matriz])
    
#criar matriz parte 3

def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)

        matriz.append(linha)

    return matriz

def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    cria_matriz(lin, col)

    return cria_matriz(lin, col)
