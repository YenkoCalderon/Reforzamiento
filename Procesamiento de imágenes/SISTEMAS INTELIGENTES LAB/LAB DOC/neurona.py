import requests #Enviar una solicitud
import shutil

def gif(enlace, archivo):
    try:
        # Hacer una solicitud de Enlace
        respuesta = requests.get(enlace, stream=True)
        # Respuesta de la Solicitud
        if respuesta.status_code == 200:
            # #Estructura binaria
            with open(archivo, 'wb') as archivo:
                respuesta.raw.decode_content = True
                shutil.copyfileobj(respuesta.raw, archivo)# respuesta.raw (Datos del Gif Guardado)
            print("GIF guardado Correctamente:", archivo)
        else:
            print("Error al descargar el GIF:", respuesta.status_code)
    except Exception as e:
        print("Ocurrió un error:", str(e))

# Ejemplo de uso
enlace = "https://media3.giphy.com/media/jIMfuPWTrYgEw/giphy.gif" # Enlace Gif
archivo = "cr7.gif"  # Nombre del Gif

gif(enlace, archivo)



