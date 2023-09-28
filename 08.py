'''Ler 10 valores, calcular e
escrever a média aritmética
desses valores lidos.
(usando While)'''
soma=0
x=1
while x <= 10:
    valor = int(input(f'Digite o valor ({x}/10) :\n'))
    x +=1
    soma += valor
media = soma / 10
print(f'A média é: {media}')
