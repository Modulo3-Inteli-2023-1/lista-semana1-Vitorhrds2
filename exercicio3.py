#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui


def soma_aninhada(t):
    """
    Calcula o total de todos os numeros na lista de listas.
   
    t: lista da lista de numeros
    return: valor total somado
    """
    total = 0
    for i in t:
        total += sum(i)
    return total

t = [[11, 22], [33], [44, 55, 66]]
print(soma_aninhada(t))



# Teste a sua função aqui (caso ache necessário)











