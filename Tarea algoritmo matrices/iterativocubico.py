import time

def multiplicar_matrices(A, B):
    """Multiplica dos matrices usando el algoritmo iterativo cúbico tradicional."""
    n = len(A)  # Número de filas de A
    m = len(A[0])  # Número de columnas de A (y número de filas de B)
    p = len(B[0])  # Número de columnas de B
    resultado = [[0] * p for _ in range(n)]  # Inicializa la matriz resultado

    # Multiplicación de matrices
    for i in range(n):
        for j in range(p):
            for k in range(m):
                resultado[i][j] += A[i][k] * B[k][j]
    return resultado

def leer_matrices_desde_archivo(ruta_archivo):
    """Lee dos matrices desde un archivo de texto, manejando múltiples líneas vacías."""
    with open(ruta_archivo, 'r') as archivo:
        lineas = [linea.strip() for linea in archivo if linea.strip()]  # Filtrar todas las líneas vacías

    # Encontrar el índice donde termina la primera matriz y comienza la segunda
    punto_medio = len(lineas) // 2

    # Leer la primera mitad como la primera matriz
    A = [[int(num) for num in linea.split()] for linea in lineas[:punto_medio]]

    # Leer la segunda mitad como la segunda matriz
    B = [[int(num) for num in linea.split()] for linea in lineas[punto_medio:]]

    return A, B

def multiplicar_y_medir_tiempo(ruta_archivo):
    """Multiplica matrices desde un archivo de texto y mide el tiempo de ejecución."""
    A, B = leer_matrices_desde_archivo(ruta_archivo)

    tiempo_inicio = time.time()  # Iniciar el cronómetro
    resultado = multiplicar_matrices(A, B)
    tiempo_transcurrido = time.time() - tiempo_inicio  # Calcular el tiempo transcurrido

    print(f"Multiplicación completada en {tiempo_transcurrido:.6f} segundos.")
    return resultado

# Ejecutar el código para procesar los archivos de matrices
if __name__ == "__main__":
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
for nombre_archivo in datasets:
        ruta_archivo = nombre_archivo  # Asegúrate de colocar la ruta correcta del archivo con las matrices
        multiplicar_y_medir_tiempo(ruta_archivo)

