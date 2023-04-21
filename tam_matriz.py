
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
