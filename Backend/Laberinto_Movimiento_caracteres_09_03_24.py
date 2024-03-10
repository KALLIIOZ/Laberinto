import random
import tkinter as tk
from tkinter import messagebox

def crear_laberinto(n):
    laberinto = [[0] * n for _ in range(n)]  
    
    # Establecemos la entrada en la esquina superior izquierda (0, 0)
    laberinto[0][0] = 0  
    
    # Creamos las coordenadas de las casillas especiales
    x1, y1 = random.randint(0, n-1), random.randint(0, n-1)
    x2, y2 = random.randint(0, n-1), random.randint(0, n-1)
    x3, y3 = random.randint(0, n-1), random.randint(0, n-1)
    
    # Verificamos que las casillas no sean la misma ni la entrada
    while (x1, y1) == (0, 0) or (x2, y2) == (0, 0) or (x1, y1) == (x2, y2) or (x3, y3) == (0, 0) or (x3, y3) == (x1, y1) or (x3, y3) == (x2, y2):
        x1, y1 = random.randint(0, n-1), random.randint(0, n-1)
        x2, y2 = random.randint(0, n-1), random.randint(0, n-1)
        x3, y3 = random.randint(0, n-1), random.randint(0, n-1)
    
    # Marcamos las casillas especiales
    laberinto[x1][y1] = 3  
    laberinto[x2][y2] = 4  
    laberinto[x3][y3] = 111 
    # Establecemos la salida en una posición aleatoria
    x2, y2 = random.randint(0, n-1), random.randint(0, n-1)
    while (x2, y2) == (0, 0) or (x2, y2) == (x1, y1) or (x2, y2) == (x3, y3):
        x2, y2 = random.randint(0, n-1), random.randint(0, n-1)
    laberinto[x2][y2] = 2
    
    # Colocamos paredes aleatorias en el laberinto
    for i in range(n):
        for j in range(n):
            if laberinto[i][j] == 0 and random.random() < 0.3:  # Probabilidad de 0.3 para colocar una pared en una celda vacía
                laberinto[i][j] = 1  # 1 representa una pared
    
    # Imprimir la matriz generada
    print("Laberinto generado:")
    for fila in laberinto:
        print(fila)
    
    return laberinto

def encontrar_camino(laberinto, ventana):
    def encontrar_camino_recursivo(laberinto, fila, columna, camino_actual):
        # Verificar si estamos fuera de los límites del laberinto o en una pared
        if (fila < 0 or columna < 0 or fila >= len(laberinto) or columna >= len(laberinto[0]) or 
            laberinto[fila][columna] == 1):
            return False
        
        camino_actual.append((fila, columna))
        
        if laberinto[fila][columna] == 2:
            return True
        
        if laberinto[fila][columna] == 111:
            pregunta_general()

        elif laberinto[fila][columna] == 3:
            # Transportar al jugador a la casilla 4
            camino_actual.pop()  # Quitar la posición actual
            fila, columna = encontrar_casilla(laberinto, 4) 
            camino_actual.append((fila, columna))  

        elif laberinto[fila][columna] == 4:
            # Transportar al jugador a la casilla 3
            camino_actual.pop()  # Quitar la posición actual del camino
            fila, columna = encontrar_casilla(laberinto, 3)  
            camino_actual.append((fila, columna))  
        
        # Marcar la posición actual como visitada
        laberinto[fila][columna] = 1
        
        # Buscar alrededor de la casilla en posición actual
        if (encontrar_camino_recursivo(laberinto, fila + 1, columna, camino_actual) or
            encontrar_camino_recursivo(laberinto, fila - 1, columna, camino_actual) or
            encontrar_camino_recursivo(laberinto, fila, columna + 1, camino_actual) or
            encontrar_camino_recursivo(laberinto, fila, columna - 1, camino_actual)):
            return True
        
        # Si ninguna dirección lleva a la salida, retroceder y marcar la posición actual como no visitada
        camino_actual.pop()
        return False
    
    def encontrar_casilla(laberinto, valor):
        for fila in range(len(laberinto)):
            for columna in range(len(laberinto[0])):
                if laberinto[fila][columna] == valor:
                    return fila, columna
        return -1, -1  # Devolver un valor predeterminado cuando la casilla no se encuentra

    
    def pregunta_general():
        # Muestra la pregunta en una ventana separada
        ventana_pregunta = tk.Toplevel(ventana)
        ventana_pregunta.title("Pregunta Especial")

        # Modifica la pregunta según tus necesidades
        pregunta_label = tk.Label(ventana_pregunta, text="¿Cuál es la capital de Francia?")
        pregunta_label.pack()

        respuesta_entry = tk.Entry(ventana_pregunta)
        respuesta_entry.pack()

        # Agrega un botón para verificar la respuesta
        verificar_boton = tk.Button(ventana_pregunta, text="Verificar", command=lambda: verificar_respuesta(respuesta_entry.get(), ventana_pregunta))
        verificar_boton.pack()
    
    def verificar_respuesta(respuesta, ventana_pregunta):
        if respuesta.lower() == "paris":
            tk.messagebox.showinfo("¡Correcto!", "Respuesta correcta. Continúa tu camino.")
            ventana_pregunta.destroy()  # Cierra la ventana de la pregunta
        else:
            tk.messagebox.showerror("Incorrecto", "Respuesta incorrecta. Inténtalo de nuevo.")

    
    camino = []  # Este es el camino que toma
    encontrar_camino_recursivo(laberinto, 0, 0, camino)
    
    print("Camino encontrado:")
    for paso in camino:
        print(paso)
    
    return camino
