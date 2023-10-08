import sys 

def calcular(grafo, origem, destino_final=None):
    distancia = {v: sys.maxsize for v in grafo}
    distancia[origem] = 0 
    visitado = set()
    predecessor = {v: None for v in grafo}
    
    while visitado != set(distancia):
        vertice_atual = None
        menor_distancia = sys.maxsize
        for v in grafo:
            if v not in visitado and distancia[v] < menor_distancia:
                vertice_atual = v
                menor_distancia = distancia[v]
                
        visitado.add(vertice_atual)
        
        for vizinho, peso in grafo[vertice_atual].items():
            if distancia[vertice_atual] + peso < distancia[vizinho]:
                distancia[vizinho] = distancia[vertice_atual] + peso
                predecessor[vizinho] = vertice_atual
                
        if vertice_atual == destino_final:
            break
            
    if destino_final:
        caminho = []
        while destino_final:
            caminho.insert(0, destino_final)
            destino_final = predecessor[destino_final]
        return distancia, caminho
    else:
        return distancia, None

def escolher_destino():
   return input("Escolha seu ponto final: ")

grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2, 'F': 6},
    'F': {'E': 6, 'G': 3},
    'G': {'F': 3}
}

origem = "A"
destino_final = escolher_destino()
distancias, caminho = calcular(grafo, origem, destino_final)

if caminho:
    print(f"Caminho mais curto de {origem} até {destino_final} é {caminho} com distância total de {distancias[destino_final]}")
else:
    for destino, dist in distancias.items():
        print(f"Caminho mais curto de {origem} até {destino} é de {dist}")
