#solicitar o salario dos funcionarios de uma empresa 
#finalizar a entrada de dados quando o usuario informa um salario negativo
# calcular a media salarial dos funcinarios da empresa

soma = 0            # somadora
quantidade = 0      # contadora
while True:
    salario = float(input("Informe o salário: "))
    if salario < 0:
        break
    soma += salario         #soma os salarios
    quantidade += 1         #conta os funcionarios 

media = soma / quantidade
print(f"Média dos salários: R${media:.2f}")


