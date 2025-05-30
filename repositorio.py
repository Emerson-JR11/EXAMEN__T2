import random
import math


def generar_matriz(filas, columnas=2):
    return [[random.randint(-81, 81) for _ in range(columnas)] for _ in range(filas)]

def calcular_distancia(coordenada):
    x, y = coordenada
    return math.sqrt(x**2 + y**2)


def encontrar_mas_alejada(matriz):
    if not matriz:
        return None
    if len(matriz) == 1:
        x, y = matriz[0]
        return matriz[0] if x > 0 and y < 0 else None

    mitad = len(matriz) // 2
    izquierda = encontrar_mas_alejada(matriz[:mitad])
    derecha = encontrar_mas_alejada(matriz[mitad:])

    if izquierda and derecha:
        return izquierda if calcular_distancia(izquierda) > calcular_distancia(derecha) else derecha
    return izquierda or derecha


pares = int(input("Ingrese la cantidad de pares de coordenadas: "))


matriz_coordenadas = generar_matriz(pares)


print("\nCoordenadas generadas:")
for fila in matriz_coordenadas:
    print(fila)


resultado = encontrar_mas_alejada(matriz_coordenadas)


if resultado:
    print("\nLa coordenada más alejada con X positivo e Y negativo es:", resultado)
else:
    print("\nNo se encontró ninguna coordenada que cumpla la condición.")
