'''Faça um código para ler 2 valores e
realize a divisão do primeiro pelo
segundo valor recebido, caso o
segundo valor digitado, seja 0, solicite
novamente o valor, informando que só
aceitaremos valores diferentes de
zero.'''

n1 = int(input('Vamos dividir 2 valores, digite o primeiro: '))
n2 = int(input('Vamos dividir 2 valores, digite o segundo: '))

while n2 == 0:
    n2 = int(input('Não aceitamos zero aqui.\n'
                   'Digite novamente o segundo valor: '))
div = n1 / n2
print('A divisão de ',n1,' por ',n2,'é igual a: ',div)
