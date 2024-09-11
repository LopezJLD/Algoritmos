import time
import math

def add_matrix(A, B):
    """Suma dos matrices A y B."""
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrix(A, B):
    """Resta la matriz B de A."""
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def strassen(A, B):
    """Multiplica dos matrices usando el algoritmo de Strassen."""
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Dividir las matrices en submatrices
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Calcular los productos intermedios
    P1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    P2 = strassen(add_matrix(A21, A22), B11)
    P3 = strassen(A11, subtract_matrix(B12, B22))
    P4 = strassen(A22, subtract_matrix(B21, B11))
    P5 = strassen(add_matrix(A11, A12), B22)
    P6 = strassen(subtract_matrix(A21, A11), add_matrix(B11, B12))
    P7 = strassen(subtract_matrix(A12, A22), add_matrix(B21, B22))

    # Combinar los productos intermedios en la matriz resultante
    C11 = add_matrix(subtract_matrix(add_matrix(P1, P4), P5), P7)
    C12 = add_matrix(P3, P5)
    C21 = add_matrix(P2, P4)
    C22 = add_matrix(subtract_matrix(add_matrix(P1, P3), P2), P6)

    # Unir las submatrices en la matriz resultante
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C

def adjust_to_power_of_two(matrix):
    """Ajusta la matriz para que tenga dimensiones de potencia de 2."""
    n = len(matrix)
    m = len(matrix[0])
    new_size = 2 ** math.ceil(math.log2(max(n, m)))  # Calcular el tamaño más cercano que sea potencia de 2

    # Crear una nueva matriz de tamaño new_size x new_size rellena de ceros
    new_matrix = [[0] * new_size for _ in range(new_size)]
    
    # Copiar los valores de la matriz original a la nueva
    for i in range(n):
        for j in range(m):
            new_matrix[i][j] = matrix[i][j]
    
    return new_matrix

def read_matrices_from_file(file_path):
    """Lee dos matrices desde un archivo de texto y ajusta sus tamaños a potencias de 2."""
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]  # Filtrar todas las líneas vacías

    mid_point = len(lines) // 2

    # Leer las matrices
    A = [[int(num) for num in line.split()] for line in lines[:mid_point]]
    B = [[int(num) for num in line.split()] for line in lines[mid_point:]]

    # Ajustar las matrices para que tengan dimensiones de potencia de 2
    A = adjust_to_power_of_two(A)
    B = adjust_to_power_of_two(B)

    return A, B

def multiply_and_time(file_path):
    """Multiplica matrices usando el algoritmo de Strassen desde un archivo de texto y mide el tiempo de ejecución."""
    A, B = read_matrices_from_file(file_path)

    start_time = time.time()  # Iniciar el cronómetro
    result = strassen(A, B)
    elapsed_time = time.time() - start_time  # Calcular el tiempo transcurrido

    print(f"Multiplicación con Strassen completada en {elapsed_time:.6f} segundos.")
    return result

# Llamada al código para recibir la ruta de un archivo de texto con las dos matrices
if __name__ == "__main__":
    # Lista de archivos en orden numérico
    datasets = [
    "20x10_10x30.txt",
    "56x6_6x80.txt",
    "100x50_50x80.txt",
    "64x64.txt",
    "100x100.txt",
    "200x200.txt",
    "400x400.txt",
    "500x500.txt",
    "1000x1000.txt"]

    for file_name in datasets:
        file_path = file_name  
        multiply_and_time(file_path)
