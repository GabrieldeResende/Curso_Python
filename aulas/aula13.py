#list

listaFrutas = ['maça', 'banana', 'abacaxi', 'limão']
listaNomes = ['Gabriel', 'Rafael', 'Allan', 'Talia']
listaTotal = listaFrutas.extend(listaNomes)

print(listaFrutas)
listaFrutas.append("laranja")
listaFrutas.pop()
listaFrutas.reverse()
listaFrutas.insert(1, "kiwi")
del listaFrutas[0]
# listaFrutas.clear()

for fruta in listaFrutas:
    print(fruta)
# print(listaFrutas[1])