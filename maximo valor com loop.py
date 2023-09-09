def max(lista):
    max = 0
    for i in lista:
        if i > max:
            max = i
    return max 

lista = [1, 3, 4, 5, 6, 7, 10, 304, 123]

maximo = max(lista)
print("maior item é de: ", maximo)