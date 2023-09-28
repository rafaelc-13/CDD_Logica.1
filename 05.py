#Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive).

valor = int(input("Digite um valor: "))

while valor <= 0:
        valor = int(input("Digite um valor válido: "))

for x in range (1,valor+1,1):
    print(x, end=" ")

