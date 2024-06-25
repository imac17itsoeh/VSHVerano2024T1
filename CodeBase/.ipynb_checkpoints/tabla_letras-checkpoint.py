import pandas as pd

def generar_tabla(clases, frec_absoluta, frec_relativa, frec_rel_acumulada):
  """
  Función que genera una tabla con datos de clases, frecuencias absolutas, frecuencias relativas y frecuencias relativas acumuladas.

  Parámetros:
    clases: Lista con las etiquetas de las clases.
    frec_absoluta: Lista con las frecuencias absolutas de cada clase.
    frec_relativa: Lista con las frecuencias relativas de cada clase.
    frec_rel_acumulada: Lista con las frecuencias relativas acumuladas de cada clase.

  Retorno:
    DataFrame: Un DataFrame de Pandas con los datos tabulados.
  """

  # Crear el DataFrame
  df = pd.DataFrame({
    "Clases": clases,
    "Frecuencia absoluta": frec_absoluta,
    "Frecuencia relativa": frec_relativa,
    "Frecuencia relativa acumulada": frec_rel_acumulada
  })

  # Mostrar la tabla
  print(df.to_string())

