#while

i = 0
while i <= 10:
    i += 1
    print(i)



while True:
    nome = input("Qual seu nome? ")
    print(f'Seu nome é {nome}')

    if nome == "sair":
        break

print("Acabou")


while i <= 100:
    i += 1

    if i >= 20 and i <= 50:
        continue
    print(i)

while False:
    print("Codigo inacessivel")


qtdLinhas = 5
qtdColunas = 5

linha = 1

while linha <= qtdLinhas:
    coluna = 1

    while coluna <= qtdColunas:
        print(f'{linha=} {coluna=}')
        coluna += 1

    linha += 1

print("Acabou!")
