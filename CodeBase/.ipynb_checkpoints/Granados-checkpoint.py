def fa_grouped(numeros, lim_inf, lim_sup):

  # Inicializar la lista de frecuencias
  frecuencias = [0] * len(lim_inf)

  # Contar las frecuencias para cada clase
  for numero in numeros:
    # Recorrer las clases
    for i, (limite_inf, limite_sup) in enumerate(zip(lim_inf, lim_sup)):
      # Si el número está dentro del intervalo (inclusivo para la última clase)
      if (limite_inf <= numero <= limite_sup) or (i == len(lim_inf) - 1 and numero == limite_sup):
        frecuencias[i] += 1
        break  # No es necesario seguir recorriendo si el número ya está en una clase

  return frecuencias



