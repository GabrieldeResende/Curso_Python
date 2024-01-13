#formatação de string

nome = "Gabriel de Resende"
altura = 1.70
peso = 65
imc = peso / (altura * altura)

print(nome, "tem", altura, "de altura,", "pesa", peso, "quilos e seu IMC é: ", imc)
print(f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e seu IMC é: {imc:.2f}')


#função format

a = "A"
b = "B"
c = 1.1
formato = 'a={1} b={2} c={0}'.format(a, b, c)

print(formato)