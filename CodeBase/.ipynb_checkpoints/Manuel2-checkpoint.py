import math
import numpy as np

def calcular_estadisticas_intervalos(numeros):
    #Calcular rango
    rango = round(max(numeros) - min(numeros), 2)
    #Calcular el numero de clases
    clases = 1 + (3.3*math.log10(len(numeros)))
    #Calcular el ancho de las clases
    ancho = round(rango / math.floor(clases), 2)
    #Creacion de los arreglos vacios
    marcas_clases = []
    limite_inferior_A = []
    limite_superior_A = []
    limites_clases = []
    #Rellenar los arreglos 
    for i in range(int(clases)):
        limite_inferior = np.min(numeros) + i * ancho
        limite_superior = limite_inferior + ancho
        limites_clases.append((limite_inferior, limite_superior))
        limite_inferior_A.append(limite_inferior)
        limite_superior_A.append(limite_superior)

    # Cálculo de las marcas de clase
    marcas_clases = []
    for limite_inferior, limite_superior in limites_clases:
        marca_clase = (limite_inferior + limite_superior) / 2
        marcas_clases.append(marca_clase)


    #Retornar
    return limite_inferior_A, limite_superior_A, marcas_clases