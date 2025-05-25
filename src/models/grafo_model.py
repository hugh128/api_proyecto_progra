from services.warshall_service import cargar_matriz_adyacencia, warshall
from services.dijkstra_service import grafo_costos, dijkstra, obtener_nombres_nodos

class Grafo:
    def __init__(self):
        self.matriz_adj = cargar_matriz_adyacencia()
        self.matriz_c = None

    def calcular_warshall(self):
        self.matriz_c = warshall(self.matriz_adj)
    
    def hay_camino(self, a, b):
        if self.matriz_c is None:
            self.calcular_warshall()
        return int(self.matriz_c[a-1, b-1])
    
    def obtener_matriz_c(self):
        if self.matriz_c is None:
            self.calcular_warshall()
        return self.matriz_c.tolist()
    

class GrafoDijkstra:
    def __init__(self):
        self.grafo = grafo_costos()
        self.nombres_nodos = obtener_nombres_nodos()
        self.resultado = None

    def calcular_dijkstra(self, origen):
        self.resultado = dijkstra(self.grafo, origen)

    def obtener_camino_y_distancia(self, origen, destino):
        if self.resultado is None or self.resultado["origen"] != origen:
            self.calcular_dijkstra(origen)
        camino_ids = self.resultado["caminos"].get(destino, [])
        distancia = self.resultado["distancias"].get(destino, float('inf'))

        camino_nombres = [self.nombres_nodos.get(nodo, f"Desconocido({nodo})") for nodo in camino_ids]

        return camino_nombres, distancia

    