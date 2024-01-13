#condicionais if/elif/ else

entrada = input("Você quer entrar ou sair? ")

if entrada == "entrar" :
    print("Você entrou do sistema") 
elif entrada == "sair":
    print("Você saiu do sistema")
else:
    print("Digite 'entrar' ou 'sair'")


num2 = 10
print("par" if num2 % 2 == 0 else "impar")

num = 11
if(num % 2 == 0): 
    print("Par")
else:
    print("Impar")
