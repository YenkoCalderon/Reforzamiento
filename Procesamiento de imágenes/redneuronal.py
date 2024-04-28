import tkinter as tk #  Proporciona una interfaz de Python 
from tkinter import messagebox #Muestra cuadros de diálogo emergentes   
import tensorflow as tf # Realizar cálculos numéricos
import numpy as np

# Función para construir y entrenar la red neuronal
def construir_entrenar_red(datos_entrenamiento):
    # Datos de entrada y salida
    X = np.array(datos_entrenamiento['experiencia']).reshape(-1, 1)  # Experiencia como entrada
    y = np.array(datos_entrenamiento['salario']).reshape(-1, 1)      # Salario como salida

    # Normalizar los datos
    X = X / np.max(X)
    y = y / np.max(y)

    # Definir la arquitectura de la red neuronal
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

    # Compilar el modelo
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Entrenar el modelo
    model.fit(X, y, epochs=500, verbose=0)

    return model

# Función para predecir salario
def predecir_salario(modelo, experiencia):
    experiencia_normalizada = experiencia / 30  # Normalizar la experiencia (suponiendo salario máximo después de 30 años)
    salario_predicho = modelo.predict(np.array([experiencia_normalizada]).reshape(-1, 1))
    salario_predicho = salario_predicho * 10000  # Desnormalizar el salario (suponiendo salario máximo de 10,000)
    return salario_predicho[0][0]

# Función para manejar la predicción
def predecir():
    experiencia = float(entry_experiencia.get())
    salario_predicho = predecir_salario(modelo, experiencia)
    messagebox.showinfo("Resultado", f"El salario Aproximado es: ${salario_predicho:.2f}")

# Datos de entrenamiento (ejemplo)
datos_entrenamiento = {
    'experiencia': [1, 2, 3, 4, 5],  # Años de experiencia
    'salario': [3000, 3500, 4000, 4500, 5000]  # Salario correspondiente
}

# Construir y entrenar la red neuronal
modelo = construir_entrenar_red(datos_entrenamiento)

# Interfaz gráfica
app = tk.Tk()
app.title("PREDICCIÒN SALARIAL")
app.geometry("300x300")  # Interfaz dimensiones
app.configure(bg="blue")  # Establecer el color de fondo de la interfaz en Azul

label_experiencia = tk.Label(app, text="AÑOS DE TRABAJO:\n", bg="blue", fg="white")
label_experiencia.pack()

# Utiliza un Label para mostrar texto en múltiples líneas
label_experiencia_multilinea = tk.Label(app, text="INGRESE LA EXPERIENCIA DEL TRABAJADOR\n", bg="blue", fg="white")
label_experiencia_multilinea.pack() , "\n"

entry_experiencia = tk.Entry(app, bg="white")
entry_experiencia.pack() , 

btn_predecir = tk.Button(app, text="RESULTADOS", command=predecir)
btn_predecir.pack()

# Agregar etiquetas de integrantes
label_integrantes = tk.Label(app, text="\nINTEGRANTES:\n", bg="blue", fg="white")
label_integrantes.pack()

label_integrante1 = tk.Label(app, text="HUANAQUIRI CALDERON YENKO KENLLI\n", bg="blue", fg="white")
label_integrante1.pack()

label_integrante2 = tk.Label(app, text="GARCIA GONZALES GIAN PAUL\n", bg="blue", fg="white")
label_integrante2.pack()

label_integrante3 = tk.Label(app, text="PAUCAR ROSAS PAOLO ENRIQUE\n", bg="blue", fg="white")
label_integrante3.pack()

label_integrante4 = tk.Label(app, text="OSORES SANCHEZ SAMUEL ALEXANDER\n", bg="blue", fg="white")
label_integrante4.pack()

app.mainloop()