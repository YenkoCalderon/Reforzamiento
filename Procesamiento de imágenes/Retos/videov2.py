import requests #Enviar Solicitud

def video(enlace, archivo): #Descargar dentro de una carpeta
    try:
        respuesta = requests.get(enlace, stream=True)# Enviamos una solicitud mediante el GET
         # Guardamos el contenido en MP4
        with open(archivo, 'wb') as archivo:#Estructura binaria
            for chunk in respuesta.iter_content(chunk_size=1024):
                    archivo.write(chunk)
        print("DESCARGA EXITOSAMENTE!")
    except Exception as e:
        print("ERROR",e)

# Detalles
enlace = "https://youtu.be/c-8T88jQJSM" # URL del video 
archivo = "video.mp4"# Nombre del video
video(enlace, archivo) #Video(Enlace(Descargar),Archivo(Carpeta)
