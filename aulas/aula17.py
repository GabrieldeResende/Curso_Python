#try except
a = 10
b = 0
try:
    print(a / b)
except ZeroDivisionError as error:
    print("Não é possivel dividir por 0", error.__class__.__name__)
except (TypeError, IndexError) as error:
    print("MSG", error.__class__.__name__)