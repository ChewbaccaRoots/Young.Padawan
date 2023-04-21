#Função que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida

def dimensoes(matriz):
    linhas = len(matriz)
    if linhas == 0:
        print("0x0")
        return
    colunas = len(matriz[0])
    for linha in matriz:
        if len(linha) > colunas:
            colunas = len(linha)
    print(f"{linhas}x{colunas}")
    

#Função que soma os valores de matrizes com a mesma dimensão
    
def soma_matrizes(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False
    else:
        result = []
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                linha.append(m1[i][j] + m2[i][j])
            result.append(linha)
        return result

#Função que recebe uma matriz e imprime linha a linha

def imprime_matriz(matriz):
    for linha in matriz:
        for elemento in linha[:-1]:
            print(elemento, end=" ")
        print(linha[-1])
        
#Função que define se as matrizes m1 e m2 são multiplicáveis

def sao_multiplicaveis(m1, m2):
    if len(m1[0]) == len(m2):
        return True
    else:
        return False
