import random
import tkinter as tk

# crea una ventana
ventana = tk.Tk()

# establece el título de la ventana
ventana.title("Generador de números aleatorios para Euromillones con Python")

# tamaño de la ventana
ventana.geometry("500x300")

# crea una fuente en negrita para el texto
font_negrita = ("TkDefaultFont", 12, "bold")

# crea dos widgets Label y muestra los números generados y los números aleatorios
texto_numeros = tk.Label(ventana, text="Los números son:", font=font_negrita)
texto_numeros.pack(pady=10)

canvas_numeros = tk.Canvas(ventana, width=300, height=80)
canvas_numeros.pack(pady=10)

texto_estrellas = tk.Label(ventana, text="Las estrellas son:", font=font_negrita)
texto_estrellas.pack(pady=5)

canvas_estrellas = tk.Canvas(ventana, width=100, height=80)
canvas_estrellas.pack(pady=5)

# función para dibujar los círculos de las estrellas
def dibujar_estrellas(estrellas):
    canvas_estrellas.delete("all")
    x = 10
    for i in range(2):
        color = "Blue"
        canvas_estrellas.create_oval(x, 5, x+30, 35, width=2, fill=color)  # cambiar tamaño de círculo
        canvas_estrellas.create_text(x+15, 20, text=str(estrellas[i]), fill="white")  # centrar texto en círculo
        x += 40
        

# función para dibujar los círculos de los números
def dibujar_numeros(numeros):
    canvas_numeros.delete("all")
    x = 30
    y = 30
    for num in numeros:
        canvas_numeros.create_oval(x-20, y-20, x+20, y+20, width=2, fill="yellow")
        canvas_numeros.create_text(x, y, text=str(num), font=font_negrita)
        x += 60
        if x > 270:
            x = 30
            y += 60

# genera 5 números aleatorios únicos entre 1 y 50
def generar_numeros():
    numeros_generados = random.sample(range(1, 51), 5)
    numeros_generados.sort()

    # genera dos números aleatorios únicos entre 1 y 12 para las estrellas
    estrellas = random.sample(range(1, 13), 2)
    estrellas.sort()

    # actualiza las etiquetas de texto con los nuevos números y estrellas
    dibujar_numeros(numeros_generados)
    dibujar_estrellas(estrellas)

# genera los números y estrellas por primera vez
generar_numeros()

# crea un botón para generar nuevos números
boton_generar = tk.Button(ventana, text="Generar nuevos números", command=generar_numeros)
boton_generar.pack(anchor="center", expand=True)

# muestra la ventana
ventana.mainloop()