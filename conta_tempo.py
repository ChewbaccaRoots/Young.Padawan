import ordenador
import random
import time

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [radom.randrange(1000) for x in range(n)]
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = ordenador.Ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha demorou", depois - antes)

        antes = time.time()
        o,selecao_direta(lista2)
        depois = time.time()
        print("Seleção direta demorou", depois - antes)
