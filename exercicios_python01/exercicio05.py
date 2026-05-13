# Implementar uma calculadora básica (soma, subtração, multiplação e divisão)
#menu com as opções 

while True:
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5- Sair")
    opcao = int(input("Escolha uma das opções acima: "))
    if 1 <= opcao <= 4:  
        a = float(input("Informe um número: "))
        b = float(input("Informe outro número: "))

    if opcao == 1:
        print(f"Resultado da soma: {a + b}")
    elif opcao == 2:
        print(f"Resultado da subtração: {a - b}")
    elif opcao == 3:
        print(f"Resultado da multiplicação: {a * b}")
    elif opcao == 4:
        if b !=0:
            print(f"Resultado da divisão: {a / b}")
        else:
            print("Erro. Divisão por 0!")
    elif opcao == 5:
        print("Programa finalizado")
        break               #finaliza o loop
    else:
        print("Opção Invalida")