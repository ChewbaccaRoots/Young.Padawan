class ordenador:
    def selecao_direta(self, lista):

        fim = len(lista)

        for i in range(fim - 1):
            # Inicialmente, o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            # Coloca o menor elemento encontrado no inicio do sub-lista
            # Para isso, troca de lugar os elementos nas podições i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]


    def bolha(self, lista):
            fim = len(lista)

            for i in range(fim-1, 0, -1):
                for j in range(i):
                    if lista[j] > lista[j+1]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]


    def bolha_curta(self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                return
