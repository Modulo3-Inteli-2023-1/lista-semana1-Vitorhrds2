#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def tem_duplicados(s):
    """
    Retorna True se algum elemento aparece mais do que uma vez em uma sequencia.
    s: string ou lista
    return: booleano
    """
    # faz uma copia de t para evitar modificar o parametro
    t = list(s)
    t.sort()

    # verifica se oselementos adjascente são iguais
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False

print(tem_duplicados('123'))
print(tem_duplicados('1221'))
print(tem_duplicados('Vitor'))
print(tem_duplicados('Anna'))






# Teste a sua função aqui (caso ache necessário)











