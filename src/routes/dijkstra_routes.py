from flask import Blueprint, request, jsonify
from models.grafo_model import GrafoDijkstra

dijkstra_bp = Blueprint('dijkstra', __name__)
grafo_dijkstra = GrafoDijkstra()

@dijkstra_bp.route('/api/dijkstra/camino', methods=['GET'])
def obtener_camino():
    try:
        origen = int(request.args.get('origen'))
        destino = int(request.args.get('destino'))

        if not (1 <= origen <= 30 and 1 <= destino <= 30):
            return jsonify({'error': 'Los nodos deben estar entre 1 y 30'}), 400

        camino, distancia = grafo_dijkstra.obtener_camino_y_distancia(origen, destino)
        distancia_redondeada = round(distancia, 2) if distancia != float('inf') else "infinito"

        return jsonify({
            "origen": camino[0] if camino else "",
            "destino": camino[-1] if camino else "",
            "camino": " -> ".join(camino),
            "nodos": camino,
            "distancia_km": f"{distancia_redondeada} km"
        })

    except Exception as ex:
        return jsonify({'error': str(ex)}), 400
