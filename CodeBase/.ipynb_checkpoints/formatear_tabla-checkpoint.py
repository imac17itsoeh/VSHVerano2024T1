import pandas as pd

def imptabla(clases, frec_absoluta, frec_relativa, frec_rel_acumulada):


  # Crear el DataFrame
  df = pd.DataFrame({
    "Clases": clases,
    "Frecuencia absoluta": frec_absoluta,
    "Frecuencia relativa": frec_relativa,
    "Frecuencia relativa acumulada": frec_rel_acumulada
  })

  # Mostrar la tabla
  print(df.to_string())
