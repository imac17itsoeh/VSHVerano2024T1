import matplotlib.pyplot as plt
def generar_pastel(clases_sorted, datos, titulo):
    plt.pie(datos, 
            labels = clases_sorted,
            colors = [ "#33FFF3", "#FF33F9", "#3339FF","#FF5733", "#E6FF33", "#FF3346"],
            autopct = "%0.01f%%",
            pctdistance = 0.8,
            counterclock = False,
            startangle = 90
           )
    plt.title(titulo, fontsize=40)
    plt.show() 
