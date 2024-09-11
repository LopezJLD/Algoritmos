import time

def ordenamiento_por_fusión(arreglo):
    """Ordena un arreglo utilizando el algoritmo de ordenamiento por fusión (merge sort)."""
    if len(arreglo) > 1:
        mitad = len(arreglo) // 2
        mitad_izquierda = ordenamiento_por_fusión(arreglo[:mitad])
        mitad_derecha = ordenamiento_por_fusión(arreglo[mitad:])

        i = j = k = 0
        # Fusionar las mitades ordenadas
        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                arreglo[k] = mitad_izquierda[i]
                i += 1
            else:
                arreglo[k] = mitad_derecha[j]
                j += 1
            k += 1

        # Agregar elementos restantes de mitad_izquierda, si los hay
        while i < len(mitad_izquierda):
            arreglo[k] = mitad_izquierda[i]
            i += 1
            k += 1

        # Agregar elementos restantes de mitad_derecha, si los hay
        while j < len(mitad_derecha):
            arreglo[k] = mitad_derecha[j]
            j += 1
            k += 1

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
    datos_ordenados = ordenamiento_por_fusión(datos)
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

