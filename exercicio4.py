#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def tem_duplicados(lista):
    if len(lista) == len(set(lista)):
        return False
    else:
        return True






# Teste a sua função aqui (caso ache necessário)
lista1 = [1, 2, 3, 4, 5]
resultado = tem_duplicados(lista1)
print(resultado) # False

lista2 = [1, 2, 3, 4, 4, 5]
resultado = tem_duplicados(lista2)
print(resultado) # True











