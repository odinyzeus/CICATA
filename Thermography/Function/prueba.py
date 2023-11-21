import numpy as np

# Crear dos matrices de 10x10 con números complejos aleatorios
matriz1 = np.random.rand(10, 10) + 1j * np.random.rand(10, 10)
matriz2 = np.random.rand(10, 10) + 1j * np.random.rand(10, 10)

# Calcular el promedio de las dos matrices
matriz_promedio = (matriz1 + matriz2) / 2

print(matriz_promedio)
