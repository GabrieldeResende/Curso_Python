# #operadores logicos

# # and 

entrada = input("[E]ntrar [S]air: ")
senha = input("Digite sua senha: ")

senhaAltorizada = '123456'
if entrada == 'E' and senha == senhaAltorizada:
    print("Entrar")
else:
    print("Sair")


# #or

entrada = input("[E]ntrar [S]air: ")
senha = input("Digite sua senha: ")


senhaAltorizada = '123456'
if (entrada == 'E' or entrada == 'e') and senha == senhaAltorizada:
    print("Entrar")
else:
    print("Sair")


# #not

senha = input("Senha: ")

if senha != '123456':
    print("Senha incorreta")
else:
    print("Entrou")


#in e not in

nome = 'Gabriel'
letra = 'G'

if(letra in nome):
    print(f'tem {letra} em {nome}')
else:
    print(f'não tem {letra} em {nome}')

numeros = [1,2,3,4,5]

print(6 not in numeros)