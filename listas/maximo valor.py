def maximo(lista):
    if len(lista) == []:
        return 0
    elif len(lista) == 1:
        return lista[0] 
    else:
        sub_max = maximo(lista[1:])
        return lista[0] if lista[0] > sub_max else sub_max
    
lista = [1, 3, 413, 403, 309, 1234, 3294, 1923, 12394, 132094, 12, 314, 123, 45, 6]

resultado = maximo(lista)

print('o maximo valor dessa lista é de: ', resultado)