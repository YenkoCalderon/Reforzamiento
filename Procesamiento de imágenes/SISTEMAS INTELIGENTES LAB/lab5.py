#GRAFICO DE BARRAS VERTICALES

import matplotlib.pyplot as plt

fig, ax = plt.subplots() # Crear la figura y los ejes

# Datos de las frutas y sus conteos
fruits = ["manzana", "blueberry", "cereza", "naranja"]
counts = [40, 100, 30, 55]

# Etiquetas para las barras y colores correspondientes
bar_labels = ["red", "blue", "_red", "orange"]
bar_color = ["tab:red", "tab:blue", "tab:red", "tab:orange"]

# Crear el gráfico de barras
ax.bar(fruits, counts, label=bar_labels, color=bar_color)

# Configurar etiquetas y título del gráfico
ax.set_ylabel("Suministro de Frutas")
ax.set_title("Suministro de frutas por color")

# Añadir leyenda al gráfico
ax.legend(title="Color de Frutas")

# Mostrar el gráfico
plt.show()
