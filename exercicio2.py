#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def cumulativo(lista):
    lista = [2, 3, 4, 5]
    comprimento = len(lista)
    lista2 = []
    soma = 0

    for i in range(comprimento):
        soma = soma + lista[i]
        lista2.append(soma)

    return lista2

print(cumulativo([2, 3, 4, 5]))





# Teste a sua função aqui (caso ache necessário)











