import requests

def descargar_musica(enlace, ruta):
    try:
        # Realizar la solicitud GET al enlace para descargar la música
        respuesta = requests.get(enlace, stream=True)
        respuesta.raise_for_status()  # Verificar si hubo algún error en la solicitud

        # Guardar el contenido de la música en un archivo MP3
        with open(ruta, 'wb') as archivo:
            for chunk in respuesta.iter_content(chunk_size=1024):
                archivo.write(chunk)

        print("Música descargada", ruta)
    except requests.exceptions.RequestException as e:
        print("Error al descargar la música:", e)

# Ejemplo de uso
enlace = "https://www.youtube.com/watch?v=RUd5doV6qps&ab_channel=Levi%27s"
ruta = "mGrupo5.mp3"

descargar_musica(enlace, ruta)
