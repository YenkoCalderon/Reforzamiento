import requests #Nos ayuda a realizar solicitudes  // obtener datos de una URL
from PIL import Image #Libreria para imagenes binarios
from io import BytesIO #proporciona clases y funciones

def print_imagen(url, nombre):
    try:
        # Obtener la imagen desde la URL
        response = requests.get(url) # Esto envía una solicitud
        if response.status_code == 200: #verifica si el código DE  RESPUESTA EXITOSA "200"
            # Abrir la imagen desde los datos binarios recibidos
            imagen = Image.open(BytesIO(response.content)) #// contiene los datos binarios de la respuesta.
            # Guardar la imagen en un archivo local
            imagen.save(nombre)
            print(f"La imagen se ha guardado Correctamente {nombre}")
        else:
            print("Fallo al obtener el URL.")
    except Exception as e:
        print("Fallo:", e)

# URL de la imagen a guardar
url_imagen = "https://www.ucv.edu.pe/wp-content/uploads/2022/08/Repositorio-UCV-751x521-1.png"
# Nombre del archivo 
nombre = "Reto.jpg"

# Funcion para imprimir el URL
print_imagen(url_imagen, nombre)

