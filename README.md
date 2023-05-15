#Criar uma classe Triângulo

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c
        

#Definiar qual tipo de Triâgulo

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        elif self.a != self.b != self.c != self.a:
            return 'escaleno'
        else:
            return 'isósceles'
            
    
#Definir se é Triânfulo retângulo

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        elif self.a != self.b != self.c != self.a:
            return 'escaleno'
        else:
            return 'isósceles'

    def retangulo(self):
        if self.c**2 == self.a**2 + self.b**2:
            return True
        else:
            return False
          

#Definir se os Triângulos são semelhantes

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        elif self.a != self.b != self.c != self.a:
            return 'escaleno'
        else:
            return 'isósceles'

    def retangulo(self):
        if self.c**2 == self.a**2 + self.b**2:
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        lados_1 = [self.a, self.b, self.c]
        lados_2 = [triangulo.a, triangulo.b, triangulo.c]
        lados_1.sort()
        lados_2.sort()
        razoes = [lados_1[i] / lados_2[i] for i in range(3)]
        if razoes[0] == razoes[1] == razoes[2]:
            return True
        else:
            return False
            
            
