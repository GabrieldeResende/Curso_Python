class Caneta:
    def __init__(self, cor_tinta):
        self.cor_tinta = cor_tinta

    @property
    def get_cor(self):
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456
    
    

canetaAzul = Caneta("Azul")
canetaVermelho = Caneta("Vermelho")

print(canetaVermelho.get_cor)
print(canetaVermelho.cor_tampa)

print(canetaAzul.get_cor)
print(canetaAzul.get_cor)
print(canetaAzul.get_cor)
print(canetaAzul.get_cor)
print(canetaAzul.get_cor)
print(canetaAzul.get_cor)
print(canetaAzul.get_cor)
print(canetaAzul.get_cor)
print(canetaAzul.get_cor)