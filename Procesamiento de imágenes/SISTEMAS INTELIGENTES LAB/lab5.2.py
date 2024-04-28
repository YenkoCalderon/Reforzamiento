#MAPAS DE COLOR
import matplotlib.pyplot as plt
import numpy as np  # Agregar la importación de numpy

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Generar datos aleatorios para el mapa de color
x = np.random.random((40, 80))

# Mostrar el mapa de color utilizando imshow
ax.imshow(x)

# Mostrar el gráfico
plt.show()
