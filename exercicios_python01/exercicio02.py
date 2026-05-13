#Solicitar ao usuario N numeros inteiros 
#Contar quantos numeros sao pares e quantos sao impares


quantidade = int(input("informe a quantidade de numeros: "))
cont = 0
cont_pares = 0
cont_impares = 0
while cont < quantidade:
    numero = int(input("Digite um numero: "))   
    if numero % 2 == 0:
        cont_pares +=1
    else:
        cont_impares += 1
    cont += 1

print(f"Quantidade de pares: {cont_pares}")
print(f"Quantidade de impares: {cont_impares}")