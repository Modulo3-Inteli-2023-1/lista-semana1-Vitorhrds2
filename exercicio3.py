#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def soma_dos_aninhados(lista):
    soma = 0
    for sublista in lista:
        for num in sublista:
            soma += num
    return soma



# Teste a sua função aqui (caso ache necessário)
lista = [[11, 22], [33], [44, 55, 66]]
resultado = soma_dos_aninhados(lista)
print(resultado) # 231

outra_lista = [[1, 2, 3, 4], [3, 3], [4, 6]]
resultado = soma_dos_aninhados(outra_lista)
print(resultado) # 26










