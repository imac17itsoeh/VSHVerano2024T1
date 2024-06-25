import matplotlib.pyplot as plt
def generar_diagrama_barras_horizontal(fa_sorted, clases_sorted, marcas_clase, labelx, labely, titulo):
    """
    Genera un diagrama de barras horizontales con las características especificadas.

    Argumentos:
        fa_sorted: Lista con las frecuencias absolutas ordenadas para el eje Y.
        clases_sorted: Lista con los nombres de las clases (textos para las marcas del eje X).

    """
    # Configurar figura y tamaño
    plt.figure(figsize=(12, 6))

    # Diagrama de barras horizontales con:
    # - Barras ajustadas al 100% de altura (height = 0.8)
    # - Contorno negro (edgecolor = "k")
    # - Colores específicos para cada barra
    plt.barh(marcas_clase, fa_sorted, height=0.8, edgecolor="k",
            color=["#FF5733", "#33FFF3", "#FF33F9", "#3339FF", "#E6FF33", "#FF3346"])

    # Personalizar marcas del eje Y (inclinadas 45°) y tamaño de fuente
    plt.yticks(marcas_clase, clases_sorted, fontsize=15, rotation=45)

    # Etiquetas y título del gráfico con tamaño de fuente grande
    plt.ylabel(labelx, fontsize=25)  # Etiqueta del eje Y
    plt.xlabel(labely, fontsize=25)  # Etiqueta del eje X
    plt.title(titulo, fontsize=40)

    # Activar cuadrícula
    plt.grid()

    # Mostrar el gráfico
    plt.show()

