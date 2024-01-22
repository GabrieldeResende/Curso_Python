## classes

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa("Gabriel", "Resende")
# p1.nome = "Gabriel"
# p1.idade = 25

print(p1.nome)

class Carro:
    def __init__(self, nome, marca, placa, cor):
        self.nome = nome
        self.marca = marca
        self.placa = placa
        self.cor = cor

    def acelerar(self):
        print(f"{self.nome} Acelerando!!")

    def freiar(self):
        print(f"{self.nome} Freiando")

celta = Carro("Celta", "Fiat", "as562e","Vermelho")
print(vars(celta))
celta.nome = "Vectra"
print(vars(celta))
celta.acelerar()
celta.freiar()
corsa = Carro("Corsa", "Fiat", "45asd68","Preto")
print(f"{corsa.nome}",corsa.cor)
corsa.acelerar()