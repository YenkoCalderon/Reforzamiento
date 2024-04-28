import requests #Enviar Solicitud

def musica(enlace, ruta): #Descargar dentro de una carpeta
    try:
        # Enviamos una solicitud mediante el GET
        respuesta = requests.get(enlace, stream=True)
        respuesta.raise_for_status()  # Verificar si hubo algún error en la solicitud

        # Guardamos el contenido en MP3
        with open(ruta, 'wb') as archivo: #Estructura binaria
            for chunk in respuesta.iter_content(chunk_size=1024):
                archivo.write(chunk)

        print("Música descargada", ruta)
    except requests.exceptions.RequestException as e:
        print("Error al descargar la música:", e)


# Realizamos el Guardado
enlace = "https://www.youtube.com/watch?v=OxDgAVI29cQ"
ruta = "musica.mp3"

musica(enlace, ruta)
