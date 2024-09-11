import time

def ordenamiento_por_insercion(arreglo):
    """Ordena un arreglo utilizando el algoritmo de ordenamiento por inserción."""
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
        # Mover elementos de arreglo[0..i-1], que son mayores que la clave, a una posición adelante
        # de su posición actual.
        while j >= 0 and clave < arreglo[j]:
            arreglo[j + 1] = arreglo[j]
            j -= 1
        arreglo[j + 1] = clave
    return arreglo

def leer_datos_desde_archivo(ruta_archivo):
    """Lee datos desde un archivo y los convierte en una lista de enteros."""
    with open(ruta_archivo, 'r') as archivo:
        datos = [int(linea.strip()) for linea in archivo]
    return datos

def ordenar_y_medir_tiempo(ruta_archivo):
    """Ordena los datos leídos de un archivo y mide el tiempo de ejecución del ordenamiento."""
    datos = leer_datos_desde_archivo(ruta_archivo)
    tiempo_inicio = time.time()
    datos_ordenados = ordenamiento_por_insercion(datos)
    tiempo_transcurrido = time.time() - tiempo_inicio
    print(f"Ordenamiento completado para {ruta_archivo} en {tiempo_transcurrido:.6f} segundos.")
    return datos_ordenados

# Conjunto de datasets a ser probados
datasets = [
    'ordenados.txt',
    'semiordenados.txt',
    'valoresrepetidos.txt',
    'randoms.txt',
    'ordenadosalreves.txt'
]

for dataset in datasets:
    ordenar_y_medir_tiempo(dataset)
