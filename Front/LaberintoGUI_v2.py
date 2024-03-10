import tkinter as tk
from tkinter import simpledialog, messagebox
import random
from Backend.Laberinto_Movimiento_caracteres import crear_laberinto, encontrar_camino

def obtener_tamaño_laberinto():
    n = simpledialog.askinteger("Tamaño del laberinto", "Ingrese el tamaño del laberinto (n):", initialvalue=10)
    if n is not None:
        mi_laberinto = crear_laberinto(n)

        # Llama a encontrar_camino con la ventana como parámetro
        camino_encontrado = encontrar_camino(mi_laberinto, ventana)

        # Mostrar el laberinto con la ruta coloreada en azul
        ventana_laberinto = tk.Tk()
        ventana_laberinto.title("Laberinto con Ruta")
        ventana_laberinto.geometry("400x400")

        # Imprimir el laberinto con la ruta coloreada
        for fila in range(len(mi_laberinto)):
            frame_fila = tk.Frame(ventana_laberinto)
            frame_fila.pack(side=tk.TOP)

            for columna in range(len(mi_laberinto[0])):
                celda = mi_laberinto[fila][columna]

                if (fila, columna) in camino_encontrado:
                    # Pinta las casillas de la ruta en azul
                    tk.Label(frame_fila, text=" ", width=2, height=1, relief="ridge", bg="blue").pack(side=tk.LEFT)
                    if celda == 2:
                        tk.Label(frame_fila, text="S", width=2, height=1, relief="ridge", bg="green").pack(side=tk.LEFT)
                else:
                    # Pinta las demás casillas según su valor
                    if celda == 0:
                        tk.Label(frame_fila, text="█", width=2, height=1, relief="ridge", bg="black").pack(side=tk.LEFT)
                    elif celda == 1:
                        tk.Label(frame_fila, text="█", width=2, height=1, relief="ridge", bg="black").pack(side=tk.LEFT)
                    elif celda == 2:
                        tk.Label(frame_fila, text="S", width=2, height=1, relief="ridge", bg="green").pack(side=tk.LEFT)
                    elif celda == 3:
                        tk.Label(frame_fila, text="3", width=2, height=1, relief="ridge", bg="yellow").pack(side=tk.LEFT)
                    elif celda == 4:
                        tk.Label(frame_fila, text="4", width=2, height=1, relief="ridge", bg="yellow").pack(side=tk.LEFT)
                    elif celda == 111:
                        tk.Label(frame_fila, text="111", width=2, height=1, relief="ridge", bg="yellow").pack(side=tk.LEFT)

            tk.Label(ventana_laberinto, text="\n").pack()

        # Ejecutar el bucle de eventos para la nueva ventana
        ventana_laberinto.mainloop()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Laberintos")
ventana.geometry("400x200")
ventana.configure(bg="gray")

# Crear el título
titulo = tk.Label(ventana, text="Generador de Laberintos", font=("Arial", 16), bg="gray", fg="white")
titulo.pack(pady=10)

# Crear el botón para crear el laberinto
boton_crear_laberinto = tk.Button(ventana, text="Crear Laberinto", command=obtener_tamaño_laberinto)
boton_crear_laberinto.pack()

# Ejecutar el bucle de eventos para la ventana principal
ventana.mainloop()

