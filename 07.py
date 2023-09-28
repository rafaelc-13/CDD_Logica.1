#Ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10,20] (incluindo os
#valores 10 e 20 no intervalo) e quantos deles estão fora deste intervalo.

cont_in = 0
cont_out = 0

for x in range (10):
    valor = int(input(f"Valor {x+1}: "))
    if valor >= 10 and valor <=20:
        cont_in += 1
    else:
        cont_out += 1
print(f"A quantidade de valores entre 10-20 foram: {cont_in}\n A quantidade de valores fora desse intervalo foram: {cont_out}")

