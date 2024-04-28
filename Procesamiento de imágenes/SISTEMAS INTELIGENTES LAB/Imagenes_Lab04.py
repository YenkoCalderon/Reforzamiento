#Reconocimiento de imagenes en certado y minimizado

import numpy as np                      #Libreria Numpy
import cv2                              #Libreria de OpenCV

img = cv2.imread("Persona.jpg")         #Leer Imagen
h,w,canal=img.shape                     #Ancho y Altura de la forma de imagen

# Interpolaciòn
img_mitad = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

#Cortar una parte de la imagen
img_piece =  img[0:int(h/2), 0:int (w/2):w]  #Cortar la imagen 01
img_piece2 = img[int(h/2):h, int (w/2):w]    #Cortar la imagen 02


cv2.imshow("Imagen Principal",img)
cv2.imshow("Imagen Minimizada",img_mitad)

cv2.waitKey(0)                     #Esperar la tecla en 0 segundos
cv2.destroyAllWindows()            #Eliminar las ventanas

