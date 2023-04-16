# > VAriáveis

# 1. Variáveis

idade = 25 #criando uma variável

print(idade)

nome = 'Jarisson Neves'

print(nome)


"""
    Tipos de variáveis
    1. int: números inteiros, ou seja, números	sem parte decimal: 0, 5, -1, 1000
    2. float: números decimais, ou seja, números    com parte decimal: 0.1, -2.7, 3.14
    3. str: cadeias de caracteres, ou seja, dados textuais (string)
    4. bool: Valores logicos (booleanos): True ou False

"""

idade = 25 # do tipo int
altura = 1.77 # do tipo float
nome = 'Jarisson Neves' # do tipo string
estudando = True  # do tipo bool

print( type(idade) )
print( type(altura) )
print( type(nome) )
print( type(estudando) )


# Obtendo dados do usuário e salvando em variáveis

linguagem = input('Qual é a linguagem de programação que você está estudando?')

print(' A linguagem que você está estudando é', linguagem)