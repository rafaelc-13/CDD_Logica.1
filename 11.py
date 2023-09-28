'''Escreva um código para ler as notas
da 1a. e 2a. avaliações de um aluno,
calcule e imprima a média desse
aluno. Só devem ser aceitos valores
válidos durante a leitura (0 a 10) para
cada nota.'''

x = 0
soma = 0

while x < 2:
    nota = float(input(f"Digite sua {x+1}º nota: "))
    while nota < 0 or nota > 10 :
        nota = float(input('Valor inválido. \nDigite sua nota novamente: '))
    soma += nota
    x += 1
media = soma / x
print('Sua média foi: ',media)
