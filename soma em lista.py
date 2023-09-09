def soma(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + soma(lista[1:])
    
lista = [1, 30, 304, 401293, 301941, 123049, 2301]


resultado = soma(lista)
print("resultado é: ", resultado)

