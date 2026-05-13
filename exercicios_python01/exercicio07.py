# Solicitar 10 numeros e calcular a media dos numeros

#usar o for = saber quantas repitições vao acontecer, caso eu nao saiba, eu posso solicitar para o usuario!

#quantidade = int(input("Digite a quantidade de números: "))
#soma = 0
#for cont in range(quantidade):
#    numero = int(input("Digite um número: "))
#    soma += numero



quantidade = int(input("Digite a quantidade de números: "))
soma = 0
for cont in range(quantidade):
    numero = int(input("Digite um número: "))
    soma += numero


    
media = soma / 10
print(f"Média dos números: {media:.2f}")

# (.2f) serve pra deixar o numero em decimal
