from numpy import array, zeros, dot, diag
## Eliminación de Gauss mediante pivoteo parcial
A = array([[4., -1., -1., 0.], [-1., 4., 0., -1.], [0., -1., -1., 4.], [-1., 0., 4., -1.]])
B = array([[30.], [60.], [70.], [40.]])

def GEPP(A, b):
    n = len(A)
    if b.size != n:
        raise ValueError("Argumento no válido: tamaños incompatibles entre A y b.", b.size, n)
    # k representa la fila dinámica actual. Dado que GE atraviesa la matriz en la parte superior
    # triángulo rectángulo, también usamos k para indicar el k-ésimo índice de la columna diagonal.
    for k in range(n - 1):
        # Elejimos el elemento de pivote más grande a continuación (incluido) k
        maxindex = abs(A[k:, k]).argmax() + k
        if A[maxindex, k] == 0:
            raise ValueError("La matriz es singular .")
        # Intercambiamos filas
        if maxindex != k:
            A[[k, maxindex]] = A[[maxindex, k]]
            b[[k, maxindex]] = b[[maxindex, k]]
        for row in range(k + 1, n):
            multiplier = A[row][k] / A[k][k]
            # El único en esta columna ya que el resto son cero
            A[row][k] = multiplier
            for col in range(k + 1, n):
                A[row][col] = A[row][col] - multiplier * A[k][col]
            # Columna de solución de ecuación
            b[row] = b[row] - multiplier * b[k]
    # print A ;print b
    x = zeros(n)
    k = n - 1
    x[k] = b[k] / A[k, k]
    while k >= 0:
        x[k] = (b[k] - dot(A[k, k + 1:], x[k + 1:])) / A[k, k]
        k = k - 1
    return x


print(A)

print(B)
Aug = GEPP(A, B)
print('Las soluciones de x1, x2, x3, x4 respectivamente son :')
print (Aug)


# Sustitución regresiva
def eliminacion_adelante(A, b, n):
    """
    Calcula la parte delantera de la eliminación gaussiana.
    """
    for row in range(0, n - 1):
        for i in range(row + 1, n):
            factor = A[i, row] / A[row, row]
            for j in range(row, n):
                A[i, j] = A[i, j] - factor * A[row, j]

            b[i] = b[i] - factor * b[row]

    return A, b

def sustitucion_regresiva(a, b, n):

    x = zeros((n, 1))
    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for row in range(n - 2, -1, -1):
        sums = b[row]
        for j in range(row + 1, n):
            sums = sums - a[row, j] * x[j]
        x[row] = sums / a[row, row]
    return x

def gauss(A, b):
    """
    Esta función realiza la eliminación de Gauss con pivoteo parcial .
    """
    n = A.shape[0]

    # Comprobamos si hay elementos diagonales cero
    if any(diag(A) == 0):
        raise ZeroDivisionError(('Se producirá la división por cero ; '
                                 'pivotar actualmente no es compatible '))

    A, b = eliminacion_adelante(A, b, n)
    return sustitucion_regresiva(A, b, n)

x = gauss(A, B)