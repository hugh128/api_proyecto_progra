import heapq
from database.connection import get_connection

def grafo_costos():
    grafo = {}
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT origen, destino, costo FROM ARISTA")

    for origen, destino, costo in cursor.fetchall():
        if origen not in grafo:
            grafo[origen] = {}
        grafo[origen][destino] = costo

    cursor.close()
    conn.close()
    return grafo

def obtener_nombres_nodos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM NODO")
    nombres = {id: nombre for id, nombre in cursor.fetchall()}
    cursor.close()
    conn.close()
    return nombres

def dijkstra(grafo, origen):
    distancias = {nodo: float('inf') for nodo in grafo}
    anteriores = {nodo: None for nodo in grafo}
    distancias[origen] = 0
    heap = [(0, origen)]

    while heap:
        actual_dist, actual_nodo = heapq.heappop(heap)

        if actual_dist > distancias[actual_nodo]:
            continue

        for vecino, peso in grafo.get(actual_nodo, {}).items():
            if peso is not None:  # Peso != NULL
                nueva_dist = actual_dist + peso
                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    anteriores[vecino] = actual_nodo
                    heapq.heappush(heap, (nueva_dist, vecino))

    caminos = {}
    for destino in grafo:
        camino = []
        actual = destino
        while actual is not None:
            camino.insert(0, actual)
            actual = anteriores[actual]
        if camino and camino[0] == origen:
            caminos[destino] = camino

    return {"origen": origen, "distancias": distancias, "caminos": caminos}
