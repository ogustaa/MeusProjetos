#solicitar quantidade de varias pessoas
#finalizar a entrada de dados quando o usuario indicar uma idade negativa
#contar quantas pessoas sao menores de idade (idade < 18)

cont_menores = 0           #contadora
while True:                #true infinito
    idade = int(input("Informe a idade (digite -1 para finalizar): "))
    if idade  < 0:
        break      #finaliza o loop
    if idade < 18:
        cont_menores += 1

print(f"Quantidade de pessoas menores de idade {cont_menores}")