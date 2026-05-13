#solicitar varios numeros ao usuario
#calcular o somatorio dos numeros

soma = 0               # variavel somadora / acumuladora
cont = 0               # variavel contadora
while True:
    numero = int(input("digite um numero: "))
    if numero < 0:
        break
    soma += numero
    cont += 1

print(f"Somatorio dos numeros : {soma}")
media = soma / cont
print(f"Média dos numeros: {media}")
