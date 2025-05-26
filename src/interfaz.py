import flet as ft
import networkx as nx
import requests
from database.connection import get_connection
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time
start= 0
destination= 0

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Proyect_Path"
    page.add(ft.Text("ProyectPath - Logística", size=30, weight=ft.FontWeight.BOLD))
    page.theme_mode = ft.ThemeMode.SYSTEM
    existe_camino = ft.Text("", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
    page.bgcolor = "#E9EDF0"
    page.controls.append(
        ft.Row(
            controls=[
                ft.Container(
                    content=ft.Divider(height=1, thickness=2, color="white"),
                    padding=ft.Padding(left=20, top=0, right=20, bottom=0),
                    expand=True
                )
            ]
        )
    )
    lugares = [
        {"name": " 1. Aeropuerto"},
        {"name": " 2. Benito Juárez"},
        {"name": " 3. Cementerio General"},
        {"name": " 4. Centro Intercultural"},
        {"name": " 5. Cerro el Baúl"},
        {"name": " 6. Cervecería"},
        {"name": " 7. Colonia el maestro"},
        {"name": " 8. Comisaría PNC 41"},
        {"name": " 9. Cuesta Blanca"},
        {"name": "10. CUNOC"},
        {"name": "11. Edificio San Lucas"},
        {"name": "12. Estadio Mario Camposeco"},
        {"name": "13. Hospital General"},
        {"name": "14. Hospital Rodolfo Robles"},
        {"name": "15. IGSS"},
        {"name": "16. Indeca"},
        {"name": "17. La Pila"},
        {"name": "18. Monumento Tecún Umán"},
        {"name": "19. Parque Central"},
        {"name": "20. Parque Japón"},
        {"name": "21. Pradera"},
        {"name": "22. Rotonda Marimba"},
        {"name": "23. Teatro Municipal"},
        {"name": "24. Terminal"},
        {"name": "25. Tinajón"},
        {"name": "26. Tribunales"},
        {"name": "27. Universidad Mariano Gálvez"},
        {"name": "28. Universidad Rafael Landivar"},
        {"name": "29. Vipersa"},
        {"name": "30. Zoológico"},
    ]

    def get_options():
        options = []
        for i in lugares:
            options.append(
                ft.DropdownOption(key= i["name"], leading_icon=ft.Icons.ARROW_RIGHT_OUTLINED)
            )
        return options

    def dropdown_changed_origen(e):
        e.control.color = ft.Colors.BLUE_900
        page.update()

    def dropdown_changed_destino(e):
        e.control.color = ft.Colors.BLUE_900
        page.update()

    #Función que mostrará el resultado
    def agregar_tarea(e):

        url = f"http://127.0.0.1:5000/api/warshall/camino?origen={origen.value[0:2].rstrip() }&destino={destino.value[0:2].rstrip()}"
        req = requests.get(url)
        json_devuelto = req.json()
        there_is_path = json_devuelto['camino']
        if there_is_path==1:
            existe_camino.value = f"Si existe camino entre {origen.value} y {destino.value},\nLongitud de (Dijstra)\nNodos_del_camino_mas_corto(Dijstra),\nRuta..."
            marcar_camino()
            page.update()
        else:
            existe_camino.value = f"No existe camino entre {origen.value} y {destino.value}"
            page.update()
    
    origen = ft.Dropdown(
        
        border=ft.InputBorder.UNDERLINE,
        enable_filter=True,
        enable_search=True,
        editable=True,
        leading_icon=ft.Icons.MY_LOCATION,
        label="Lugar de origen",
        options=get_options(),
        bgcolor="#E6F0FA",
        width=400,
        on_change= dropdown_changed_origen,
    )

    destino = ft.Dropdown(
        border=ft.InputBorder.UNDERLINE,
        enable_filter=True,
        enable_search=True,
        editable=True,
        leading_icon=ft.Icons.EDIT_LOCATION_ALT_OUTLINED,
        label="Lugar de destino",
        options=get_options(),
        width=400,
        bgcolor="#E6F0FA",
        on_change=dropdown_changed_destino
    )
    
    boton_agregar = ft.FilledButton(" Buscar ruta", on_click=agregar_tarea, icon=ft.Icons.LOCATION_SEARCHING_OUTLINED, style=ft.ButtonStyle(
        bgcolor="#1269B6", color="white",shape=ft.RoundedRectangleBorder(radius=15),padding=20,overlay_color="#081966",))

    page.add(origen, destino,boton_agregar,existe_camino)
    grafo_ciudades(None,None)

    page.scroll_vertical = ft.Column(expand=1, wrap=False, scroll=ft.ScrollMode.ALWAYS)
    page.graph_image = ft.Image(src="grafo.png", width=1762, height=1421, fit=ft.ImageFit.CONTAIN, border_radius=ft.border_radius.all(50),)
    page.scroll_vertical.controls.append(page.graph_image)
    page.add(page.scroll_vertical)

    def marcar_camino():
        nodos=['9', '8', '14', '10']
        aristas=[('9','8'),('8','14'),('14','10')]
        grafo_ciudades(nodos,aristas)
        page.graph_image.src = f"grafo2.png"
        page.update()

        

def grafo_ciudades(nodos, listado_aristas):
    grafo_dirigido = get_info_arista_vertices()
    #nodos = ['1', '2', '3', '4','5', '6', '7', '8','9', '10', '11', '12','13', '14', '15', '16','17', '18', '19', '20','21', '22', '23', '24','25', '26', '27', '28','29','30']
    #grafo_dirigido.add_nodes_from(nodos)

    plt.figure(figsize=(20,20))
    pos = nx.spring_layout(grafo_dirigido, seed=42, k=5, iterations=100)
    #pos = nx.spring_layout(grafo_dirigido)
 
    if(nodos == None):
        nx.draw(grafo_dirigido, pos, with_labels = True, node_color = 'skyblue', node_size = 1500, edge_color='gray', font_size=16)
        labels = nx.get_edge_attributes(grafo_dirigido, 'weight')
        nx.draw_networkx_edge_labels(grafo_dirigido, pos, edge_labels=labels, font_size=10, font_color='red')
        plt.tight_layout()
        plt.savefig("grafo.png", bbox_inches = 'tight')
    else:
        colores = ['midnightblue' if i in nodos else 'gray' for i in grafo_dirigido.nodes()]
        nx.draw_networkx_nodes(grafo_dirigido, pos, node_color = colores, node_size = 800)
        
        nx.draw_networkx_edges(grafo_dirigido, pos, edgelist=[e for e in grafo_dirigido.edges() if e not in listado_aristas],edge_color='gray',arrows=True, arrowsize=20)
        nx.draw_networkx_edges(grafo_dirigido, pos, edgelist=listado_aristas, edge_color='green', arrows=True, arrowsize=30, connectionstyle='arc3,rad=0.1')
        nx.draw_networkx_labels(grafo_dirigido, pos, font_size=15, font_color='white')
        peso = nx.get_edge_attributes(grafo_dirigido, 'weight')
        nx.draw_networkx_edge_labels(grafo_dirigido,pos, edge_labels=peso)
        plt.tight_layout()
        plt.savefig("grafo2.png", bbox_inches = 'tight')

    
    plt.close()


def get_info_arista_vertices():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT origen, destino, costo FROM ARISTA")
    casilla = cursor.fetchall()

    grafo = nx.DiGraph()

    for origen, destino, costo in casilla:
        if costo != None:
            grafo.add_edge(str(origen),str(destino),weight = float(costo))
    cursor.close()
    conn.close()

    return grafo

    
