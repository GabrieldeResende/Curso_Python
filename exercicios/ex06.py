#jogo para usuario adivinhar qual palavra


#Palavra secreta

palavraSecreta = 'perfume'
letrasAcertadas = ''
numeroTetantivas = 0
while True:
    letraDigitada = input("Digite uma letra: ")
    numeroTetantivas += 1

    if len(letraDigitada) > 1 :
        print("Digite somente uma letra!")
        continue

    if letraDigitada in palavraSecreta:
        letrasAcertadas += letraDigitada
    
    palavraFormada = ''
    for letraSecreta in palavraSecreta:
        if letraSecreta in letrasAcertadas:
            palavraFormada += letraSecreta
        else:
            palavraFormada += '*'
    print(f"Palavra Formada {palavraFormada}")
    if palavraFormada == palavraSecreta:
        print("Voce Acertou")
        print("Palavra Secreta:", palavraSecreta)
        print("Quantidade de tentativas:", numeroTetantivas)
        break