import tkinter as tk
from tkinter import messagebox

def crear_laberinto():
    # Aquí iría la lógica para crear el laberinto
    messagebox.showinfo("Laberinto creado", "¡Se ha creado el laberinto!")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Generador de Laberintos")
ventana.geometry("400x200")
ventana.configure(bg="gray")

# Crear el título
titulo = tk.Label(ventana, text="Generador de Laberintos", font=("Arial", 16), bg="gray", fg="white")
titulo.pack(pady=10)

# Crear el botón para crear el laberinto
boton_crear_laberinto = tk.Button(ventana, text="Crear Laberinto", command=crear_laberinto)
boton_crear_laberinto.pack()

# Ejecutar el bucle de eventos
ventana.mainloop()
