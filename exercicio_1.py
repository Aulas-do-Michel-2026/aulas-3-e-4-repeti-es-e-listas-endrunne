"""
#### Exercício 1

Receba um número e calcule a soma de todos os números de 1 até ele.

Exemplo:

Digite um número:
5

A soma de 1 até 5 é 15.
--------
Digite um número:
3

A soma de 1 até 3 é 6.

Dica: Use o comando "for" junto com "range()" para percorrer os números,
e uma variável para ir acumulando a soma.
"""
inputted_number = int(input("Digite um número: "))
acc = 0
for n in range(1,inputted_number + 1):
    acc += n
print(f"A soma de 1 até {inputted_number} é {acc}")