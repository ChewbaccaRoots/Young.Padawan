#função que recebe uma lista de strings com nome de pessoas como parâmetro e devolve o nome mais curto presente na lista.

def menor_nome(nomes):
    menor_nome = nomes[0].strip().capitalize()
    for nome in nomes:
        nome = nome.strip().capitalize()
        if len(nome) < len(menor_nome):
            menor_nome = nome
    return menor_nome
    
#função que recebe uma frase (uma string) como parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.

def maiusculas(frase):
    letras_maiusculas = ''
    for letra in frase:
        if ord('A') <= ord(letra) <= ord('Z'):
            letras_maiusculas += letra
    return letras_maiusculas
    
#função que recebe como primeiro parâmetro uma string contendo uma frase e como segundo parâmetro uma outra string.

def conta_letras(frase, contar="vogais"):
    vogais = 'aeiou'
    frase = frase.lower()
    if contar == 'vogais':
        return sum(1 for letra in frase if letra in vogais)
    elif contar == 'consoantes':
        return sum(1 for letra in frase if letra.isalpha() and letra not in vogais)
    else:
        return "Tipo de letra inválido. Escolha 'vogais' ou 'consoantes'."

#função que recebe uma lista de strings como parâmetro e devolve o primeiro string na ordem lexicográfica.

def primeiro_lex(lista):
    return sorted(lista)[0]
