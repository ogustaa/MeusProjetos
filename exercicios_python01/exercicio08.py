# Solicitar a idade de 10 pessoas
# Contar quantas pessoas são menores de idade 
# Calcular a media de idade das pessoas 

#como sei que sao 10 pessoas usarei o for!
#caso eu queira alterar a quantidade de idades solicidadas:
#quantidade = int(input("Digite a quantidade de pessoas"))
#logo após isso eu substituo o número "10" do range pela variavel solicitada "quantidade"

cont_menores = 0
soma_idades = 0
for cont in range(10):
    idade = int(input('Digite a idade: '))
    if idade < 18:
        cont_menores += 1
    soma_idades += idade

#if quantidade > 0:
media = soma_idades / 10
print(f"Quantidade de pessoas menores de idade: {cont_menores}")
print(f"Média das idades: {media:.2f}")

#else:
#   print("Nenhuma idade informada")