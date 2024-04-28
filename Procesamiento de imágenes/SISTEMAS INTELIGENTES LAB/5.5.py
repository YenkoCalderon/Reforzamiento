import matplotlib.pyplot as plt #En forma Ordenada
import numpy as np
x = np.linspace(0, 3 , 20)
y = np.linspace(0, 9 , 20)

plt.plot(x,y)           #Grafica con linea continua
plt.plot(x,y , "o")     #Grafica con linea punteada
plt.show()              #EMostrar la Grafica (Python necesario)