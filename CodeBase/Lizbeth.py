def obtener_frecuencia_relativa_acumulada(fr):
    frecuencias_acumuladas = []
    suma = 0
    for elemento in fr:
        suma += elemento
        frecuencias_acumuladas.append(suma)
    return frecuencias_acumuladas