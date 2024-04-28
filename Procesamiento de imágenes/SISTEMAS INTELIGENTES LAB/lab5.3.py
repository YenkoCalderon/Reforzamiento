#MAPAS DE TRAZADO DE VARIABLES CATEGORICAS
import matplotlib.pyplot as plt

# Datos de las variables categóricas
data = {"manzana": 10, "naranja": 15, "limon": 5, "lima": 20}
names = list(data.keys())
values = list(data.values())

# Crear la figura y los ejes
fig, axs = plt.subplots(1, 3, figsize=(15, 4), sharey=True)

# Graficar barras en el primer eje
axs[0].bar(names, values)

# Graficar dispersión en el segundo eje
axs[1].scatter(names, values)

# Graficar línea en el tercer eje
axs[2].plot(names, values)

# Título de la figura
fig.suptitle("Trazado de Variables de Categorias")

# Mostrar la figura
plt.show()
