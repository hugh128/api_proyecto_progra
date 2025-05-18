from services.warshall_service import cargar_matriz_adyacencia, warshall

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
    