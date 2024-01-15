#for + Range

numeros = range(0, 81, 8)

for i in numeros:
    print(i)

#for letra in nome 
nome = 'Gabriel'

for letra in nome:
    print(letra)
print("Fim do For")

iterador = iter(nome)
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break