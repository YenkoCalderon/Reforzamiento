import numpy as np

# Crear un array de 24 elementos y darle forma de 2x3x4
b = np.arange(24).reshape(2, 3, 4)

# Aplanar el array 'b'
b.ravel()

# Imprimir el array 'b'
print(b)
