import tkinter as tk
from tkinter import simpledialog, messagebox
import random

def crear_laberinto(n):
    laberinto = [[0] * n for _ in range(n)]

    # Establecemos la entrada en la esquina superior izquierda (0, 0) y la salida en la esquina inferior derecha (n-1, n-1)
    laberinto[0][0] = 0
    laberinto[n-1][n-1] = 2

    # Creamos las coordenadas de las casillas especiales
    x1, y1 = random.randint(0, n-1), random.randint(0, n-1)
    x2, y2 = random.randint(0, n-1), random.randint(0, n-1)

    # Verificamos que las casillas no sean ni la entrada ni la salida
    while (x1, y1) == (0, 0) or (x1, y1) == (n-1, n-1) or (x2, y2) == (0, 0) or (x2, y2) == (n-1, n-1):
        x1, y1 = random.randint(0, n-1), random.randint(0, n-1)
        x2, y2 = random.randint(0, n-1), random.randint(0, n-1)

    # Marcamos las casillas especiales
    laberinto[x1][y1] = 3  # Casilla especial 3
    laberinto[x2][y2] = 4  # Casilla especial 4

    # Agregamos una casilla especial que requiere resolver un acertijo antes de pasar
    x3, y3 = random.randint(0, n-1), random.randint(0, n-1)
    # Verificamos que la casilla no sea ni la entrada ni la salida
    while (x3, y3) == (0, 0) or (x3, y3) == (n-1, n-1):
        x3, y3 = random.randint(0, n-1), random.randint(0, n-1)
    laberinto[x3][y3] = 111  # Casilla especial que requiere resolver un acertijo antes de pasar

    # Colocamos paredes aleatorias en el laberinto
    for i in range(n):
        for j in range(n):
            if laberinto[i][j] == 0 and random.random() < 0.3:  # Probabilidad de 0.3 para colocar una pared en una celda vacía
                laberinto[i][j] = 1  # 1 representa una pared

    # Mostrar el laberinto en una ventana emergente
    laberinto_str = '\n'.join([' '.join(map(str, row)) for row in laberinto])
    messagebox.showinfo("Laberinto creado", laberinto_str)

def obtener_tamaño_laberinto():
    n = simpledialog.askinteger("Tamaño del laberinto", "Ingrese el tamaño del laberinto (n):", initialvalue=10)
    if n is not None:
        crear_laberinto(n)

# Crear la ventana
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

# Ejecutar el bucle de eventos
ventana.mainloop()