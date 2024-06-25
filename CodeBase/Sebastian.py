def obtener_frecuencia_relativa(arreglo):
  """
  Función para obtener la frecuencia relativa de los elementos en un arreglo.
  """
  # Calcular la frecuencia relativa para cada elemento
    
  frecuencia_relativa = []
  for elemento in arreglo:
      
    frecuencia_relativa.append(elemento / sum(arreglo)*100)
  return frecuencia_relativa
