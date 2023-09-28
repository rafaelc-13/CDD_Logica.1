'''Escreva um código que solicite o
nome completo do usuário e mostre
quantas letras tem esse nome'''


n = input("Digite seu nome completo: ")
cont = 0
for x in (n):
    if x != " ":
        cont += 1
print("Seu nome tem : ",cont," letras.")

