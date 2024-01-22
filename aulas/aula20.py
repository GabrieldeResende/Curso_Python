#encapsulamento
# public protected private
#public declara sem underline
#protected declara com um underline _
#private declara com dois underline __


class Foo:
    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'Isso é protegido'
        self.__private = "Isso é privado"

f = Foo()
print(f.public)