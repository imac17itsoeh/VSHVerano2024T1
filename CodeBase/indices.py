def obtener_indices(arreglo_entrada):
  arreglo_salida=[]  
  for i, elemento in enumerate(arreglo_entrada):
    indice = arreglo_entrada.index(elemento)
    indice += 1
      
    arreglo_salida.append(indice)
  return arreglo_salida


