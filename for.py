"""
for variavel in range(10):
    print(variavel) """

"""
for variavel in range(1, 10): #o valor sempre irá ao número menor do que o ultimo, exemplo, neste pedido, ele vai de um ao nove
    print(variavel)"""

"""
for variavel in range(1, 12, 3):
    print(variavel)"""

"""
nota1 = float(input('Informe sua nota 1: '))
nota1 = float(input('Informe sua nota 2: '))
nota1 = float(input('Informe sua nota 3: '))"""

soma = 0

for i in range(1, 4):
    nota = float(input(F'Informe a sua nota {i}: '))

    soma = soma + nota

print (soma / 3)
