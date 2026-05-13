# Objetivo:
#Desenvolver um algotitimo (programa em python) que solicite o nome dos tres candidatos, receba os votos e, ao final da votação, exiba um relatorio com os resultados, os requisitos estao no arquivo enviado da minha faculdade!

print("Digite o nome dos candidatos:")

candidato1 = input("1: ")
    
while candidato1 == "":
    print('Nome em branco, digite algo')
    candidato1 = input("1: ")


candidato2 = input("2: ")

while candidato2 == "":
    print("Nome em branco, digite algo")
    candidato2 = input("2: ")

candidato3 = input("3: ")

while candidato3 == "":
    print("Nome em branco, digite algo")
    candidato3 = input("3: ")


votos1 = 0
votos2 = 0
votos3 = 0
nulos = 0

voto = -1

while voto != 0:
    
    print("CANDIDATOS")
    print("1 - ", candidato1)
    print("2 - ", candidato2)
    print("3 - ", candidato3)
    print("0 - FIM DA VOTAÇÃO!") 
    voto = int(input("Voto: "))

    if voto == 1:
        votos1 += 1

    elif voto == 2:
        votos2 += 1 

    elif voto == 3:
        votos3 += 1

    elif voto != 0:
        nulos += 1

total = votos1 + votos2 + votos3 + nulos
porcentagem1 = (votos1 /total) * 100
porcentagem2 = (votos2 /total) * 100
porcentagem3 = (votos3 /total) * 100
porcentagem_nulos = (nulos / total) * 100

print("CANDIDATOS")
print("TOTAL DE VOTOS: ", total)

print(f"1 - {candidato1} -> {votos1} -> {porcentagem1:.1f}%")
print(f"2 - {candidato2} -> {votos2} -> {porcentagem2:.1f}%")
print(f"3 - {candidato3} -> {votos3} -> {porcentagem3:.1f}%")
print(f"NULOS - {nulos} -> votos -> {porcentagem_nulos:.1f}%")