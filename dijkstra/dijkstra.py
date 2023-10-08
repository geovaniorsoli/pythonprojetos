import sys 

def calcular(grafo, origem):
    distancia = {v: sys.maxsize for v in grafo}
    distancia[origem] = 0 
    visitado = set()
    
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
    return distancia    

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
caminhocurto = calcular(grafo, origem)

for destino, distancia in caminhocurto.items():
    print(f"caminho menor de {origem} ate {destino} é de {distancia}")