#GRAFICO LINEAL V2
import numpy as np
import matplotlib.pyplot as plt
#DEFINIR DATOS
x1 = [3,4,5,6]
y1 = [5,6,3,4]
x2 = [2,5,8]
y2 = [3,4,3]
#APLICAMOS CONFIGURACION DE CARACTERISTICAS DEL GRAFICO
plt.plot(x1,y1,label="GRAFICO 1", linewidth=4,  color ="Red")
plt.plot(x2,y2,label="GRAFICO 2", linewidth=4,  color ="Black")
#DEFINIR TITULO PARA EL GRAFICO
plt.title("Diagrama de Lineas")
plt.ylabel("Eje Y")
plt.xlabel("Eje X")
#MOSTRAR LEYENDA , CUADRICULA Y FIGURA(GRAFICO)
plt.legend()
plt.grid()
plt.show()
