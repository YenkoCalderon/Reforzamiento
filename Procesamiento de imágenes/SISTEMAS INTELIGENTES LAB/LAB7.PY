import numpy as np
import matplotlib.pyplot as plt

#DEFINIR DATOS

x1 = [3,4,5,6]
y1 = [5,6,3,4]
x2 = [2,5,8]
y2 = [3,4,3]

#APLICAMOS CONFIGURACION DE CARACTERISTICAS DEL GRAFICO

plt.bar(x1,y1,label="LINEA 1", linewidth=4,  color ="green")
plt.bar(x2,y2,label="LINEA 2", linewidth=4,  color ="blue")

#DEFINIR TITULO PARA EL GRAFICO

plt.title("Diagrama de BARRAS")
plt.ylabel("Eje Y")
plt.xlabel("Eje X")

#MOSTRAR LEYENDA , CUADRICULA Y FIGURA(GRAFICO)

plt.legend()
plt.grid()
plt.show()
