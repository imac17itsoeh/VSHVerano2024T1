import numpy as np

def calcular_estadisticas_intervalos(numeros):

  # Cálculo del rango
  rango = np.max(numeros) - np.min(numeros)

  # Cálculo del número de clases (Sturges)
  num_clases = 1 + 3.3 * np.log10(len(numeros))
  parte_entera = int(num_clases)
  parte_decimal = num_clases - parte_entera

  if parte_decimal < 0.5:
    # Redondear hacia abajo
    num_clases= parte_entera
  else:
    # Redondear hacia arriba
    num_clases= parte_entera + 1

  # Cálculo del ancho de clase
  ancho_clase = rango / num_clases

  # Definición de los límites de clase
  limites_clases = []
  limite_inferior_A=[]
  limite_superior_A=[]
    
   
  for i in range(int(num_clases)):
    limite_inferior = np.min(numeros) + i * ancho_clase
    limite_superior = limite_inferior + ancho_clase
    limites_clases.append((limite_inferior, limite_superior))
    limite_inferior_A.append(limite_inferior)
    limite_superior_A.append(limite_superior)

  # Cálculo de las marcas de clase
  marcas_clases = []
  for limite_inferior, limite_superior in limites_clases:
    marca_clase = (limite_inferior + limite_superior) / 2
    marcas_clases.append(marca_clase)

  return limite_inferior_A, limite_superior_A, marcas_clases


