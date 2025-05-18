from flask import Blueprint, request, jsonify
from models.grafo_model import Grafo

warshall_bp = Blueprint('warshall', __name__)
grafo = Grafo()

@warshall_bp.route('/api/warshall/camino', methods=['GET'])
def verificar_camino():
    try:
        origen = int(request.args.get('origen'))
        destino = int (request.args.get('destino'))

        if not (1 <= origen <= 30 and 1 <= destino <= 30):
            return jsonify({'error': 'Los nodos deben estar entre 1 y 30'}), 400

        resultado = grafo.hay_camino(origen, destino)
        matriz_c = grafo.obtener_matriz_c()

        return jsonify({
            "origen": origen,
            "destino": destino,
            "camino": resultado,
            "matriz_c": matriz_c
        })

    except Exception as ex:
        return jsonify({'error': str(ex)}), 400
