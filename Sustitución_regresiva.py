#Importación de la biblioteca NumPy
import numpy as np
import sys

# Lectura del número de incógnitas
n = int(input('Ingrese el número de incógnitas: '))

# HRealizamos una matriz numpy de n x n + 1 tamaño e inicializamos  a cero para almacenar la matriz aumentada
a = np.zeros((n, n + 1))

# Realizamos una matriz numérica de tamaño n e iniciamos a cero para almacenar el vector de solución
x = np.zeros(n)

# Lectura de coeficientes matriciales aumentados
print('Ingrese los coeficientes de la matriz:')

for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))


print('La matriz ingresada es: ')
print(a)

# Aplicamos la eliminación de Gauss
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('División por cero detectada!')



    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]

        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]



# Realizamos la sustitución regresiva
x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = a[i][n]

    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]

    x[i] = x[i] / a[i][i]



# Visualizamos la solución
print('\n La solución requerida es: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')