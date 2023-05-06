#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def multiplas_operacoes(a, b):
    if b == 0:
        return 0
    else:
        soma = a + b
        subtracao = a - b
        multiplicacao = a * b
        divisao = a / b
        return soma, subtracao, multiplicacao, divisao





# Teste a sua função aqui (caso ache necessário
resultado = multiplas_operacoes(20, 10)
print(resultado) # (30, 10, 200, 2.0)

resultado = multiplas_operacoes(9, 0)
print(resultado) # 0











