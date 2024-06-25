def ordenar_cadenas(cadenas_formateadas):

  for i in range(len(cadenas_formateadas)):
    for j in range(i + 1, len(cadenas_formateadas)):
      if cadenas_formateadas[i] > cadenas_formateadas[j]:
        cadenas_formateadas[i], cadenas_formateadas[j] = cadenas_formateadas[j], cadenas_formateadas[i]

  return cadenas_formateadas