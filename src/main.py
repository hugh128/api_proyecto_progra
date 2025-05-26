import multiprocessing
from app import create_app
import flet as ft
from interfaz import main as flet_main

def iniciar_api():

    app = create_app()
    app.run(debug=False, use_reloader=False)

if __name__ == '__main__':
    #Inicio de la API   
    multiprocessing.set_start_method('spawn')
    api= multiprocessing.Process(target=iniciar_api)
    api.start()
    #Inicio de la interfaz
    try:
        ft.app(target=flet_main)
    finally:
        api.terminate()
