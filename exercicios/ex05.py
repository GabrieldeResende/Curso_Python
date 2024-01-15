#Calculadora com While


num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")
operador = input("Digite o operador ou 0 para sair: ")

while operador != '0':
    if operador == '+':
        total = int(num1) + int(num2)
        print(total)
        break
    elif operador == '-':
        total = int(num1) - int(num2)
        print(total)
        break
    elif operador == '/':
        total = int(num1) / int(num2)
        print(total)
        break
    elif operador == '*':
        total = int(num1) * int(num2)
        print(total)
        break
print("Fim")