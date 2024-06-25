def formateando_str(nombres):
  """
  Función que quita los acentos y convierte a mayúsculas los elementos de un arreglo de nombres.

  Argumentos:
    nombres (list): El arreglo de nombres a formatear.

  Retorna:
    list: El arreglo de nombres formateado sin acentos y en mayúsculas.
  """

  # Diccionario de traducción de caracteres acentuados a sin acentos
  diccionario_acentos = {
      "á": "A",
      "é": "E",
      "í": "I",
      "ó": "O",
      "ú": "U"
  }
  nombres_formateados = []
  for nombre in nombres:
    nombre_sin_acentos = nombre.translate(str.maketrans(diccionario_acentos))

    nombre_final = nombre_sin_acentos.upper().replace(" ", "").strip()

    nombres_formateados.append(nombre_final)

  return nombres_formateados