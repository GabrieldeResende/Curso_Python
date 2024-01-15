#try except

numero = input ('vou digitar o numero que vc digitar: ')

try:
    numeroDobro = float(numero) * 2
    print(f'o dobro de {numero} é {numeroDobro:.0f}')
except:
    print('Isso não é um numero')

# print(numero.isdigit())
