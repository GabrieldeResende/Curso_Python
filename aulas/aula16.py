# *args

x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args):
    for numeros in args:
        total = total + numeros
        print(numeros, total)


soma(1, 2, 3, 4, 5)

# teste = (1, 2, 3, 4, 5)
# teste2 = [1, 2, 3, 4, 5]
# print(teste, type(teste))
# print( teste2, type(teste2))
# teste2[0] = 6
# print(teste2)
# print(teste[0])
