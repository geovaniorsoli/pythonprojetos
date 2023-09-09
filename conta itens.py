def conta(lista):
    if lista == []:
        return 0
    else:
        return 1 + conta(lista[1:])
    
    
    
lista = [ 1, 3904, 3012, 123, 3456, 5092, 3918, 312459, 31]

resultado = conta(lista)
print("O total de itens é de: ", resultado)