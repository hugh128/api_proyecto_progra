import numpy as np
from database.connection import get_connection

def cargar_matriz_adyacencia():
    n = 30
    matriz = np.zeros((n, n), dtype=int)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT origen, destino, adyacencia FROM ARISTA")

    for origen, destino, adyacencia in cursor.fetchall():
        matriz[origen-1, destino-1] = 1 if adyacencia else 0

    cursor.close()
    conn.close()

    return matriz

def warshall(matriz_adj):
    n = matriz_adj.shape[0]
    matriz_c = matriz_adj.copy()

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matriz_c[i, j] == 0:
                    matriz_c[i, j] = matriz_c[i, k] and matriz_c[k, j]

    return matriz_c
