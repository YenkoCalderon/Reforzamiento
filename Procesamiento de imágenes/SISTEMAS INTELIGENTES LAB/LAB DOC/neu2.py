import numpy as np
import tensorflow as tf

# Datos de entrenamiento: años de experiencia y salario
inputs = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
outputs = np.array([45000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000])

# Definir el modelo de la red neuronal
model = tf.keras.Sequential([
   tf.keras.layers.Dense(units=3, activation='relu', input_shape=[1]),
   tf.keras.layers.Dense(units=1)
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Entrenar el modelo
model.fit(inputs, outputs, epochs=1000, verbose=1)

# Utilizar el modelo para predecir un salario
input_data = np.array([[11]])  # Convertir la lista en una matriz NumPy
prediction = model.predict(input_data)
print("Predicción del salario para 11 años de experiencia:", prediction[0][0])
