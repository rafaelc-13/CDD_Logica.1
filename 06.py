#Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS.
cont = 0

for i in range(10):
    n = int(input("Valor: "))
    if n<0:
        cont += 1
print(cont," valores foram negativos.")
