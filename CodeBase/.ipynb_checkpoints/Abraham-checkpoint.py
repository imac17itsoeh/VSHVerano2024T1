def generar_tabla_distribucion_frecuencias(datos, lim_inf, lim_sup, marcas_clase, fa, fr, fatum):


  # Encabezado de la tabla
  encabezado = "| N°| LimInf | LimSup| MarcaC| fa | fr | Facum |\n"
  linea_divisoria = "|---|--------|--------|-------|----|----|-----|\n"

  # Cuerpo de la tabla
  cuerpo_tabla = ""
  for i, (clase, lim_inf_valor, lim_sup_valor, marca_clase_valor, fa_valor, fr_valor, fatum_valor) in enumerate(zip(range(1, len(lim_inf) + 1), lim_inf, lim_sup, marcas_clase, fa, fr, fatum)):
    fila = f"| {clase} | {lim_inf_valor:.4f} | {lim_sup_valor:.4f} | {marca_clase_valor:.4f} | {fa_valor:.0f} | {fr_valor:.2f}% | {fatum_valor:.2f}% |\n"
    cuerpo_tabla += fila

  # Tabla completa
  tabla_completa = encabezado + linea_divisoria + cuerpo_tabla + linea_divisoria

  return tabla_completa