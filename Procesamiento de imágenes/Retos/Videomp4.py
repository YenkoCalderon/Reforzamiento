import requests #Enviar Solicitud

def video(enlace,archivo): #Descargar dentro de una carpeta
    try:
        respuesta = requests.get(enlace, stream=True) # Enviamos una solicitud mediante el GET
        respuesta.raise_for_status()  # Verificar si hubo algún error en la solicitud
         # Guardamos el contenido en MP4
        with open(archivo, 'wb') as archivo: #Estructura binaria
            for chunk in respuesta.iter_content(chunk_size=1024):
                archivo.write(chunk)
        print("Descarga EXitosamente !")
    except Exception as e:
        print("Error al descargar el video:", e)

# URL del video 
enlace = "https://www.youtube.com/watch?v=iQIGgVwjWeQ&ab_channel=GOLDYLYRICS"
# Nombre del video
archivo = "Grupo5.mp4"
video(enlace, archivo)
