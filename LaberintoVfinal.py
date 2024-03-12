import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import copy

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
    
    return laberinto

def encontrar_camino(laberinto):
    def encontrar_camino_recursivo(laberinto, fila, columna, camino_actual):
        # Verificar si estamos fuera de los límites del laberinto o en una pared
        if (fila < 0 or columna < 0 or fila >= len(laberinto) or columna >= len(laberinto[0]) or 
            laberinto[fila][columna] == 1):
            return False
        
        camino_actual.append((fila, columna))
        
        if laberinto[fila][columna] == 2:
            return True

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
    
    camino = []  # Este es el camino que toma
    encontrar_camino_recursivo(laberinto, 0, 0, camino)
    
    return camino


def pregunta_general():
    respuesta = simpledialog.askstring("Pregunta", "¿Cuál es la capital de Francia?")
    while respuesta.lower() != "paris":
        respuesta = simpledialog.askstring("Pregunta", "Respuesta incorrecta. Inténtalo de nuevo.\n¿Cuál es la capital de Francia?")
    return True

def mostrar_laberinto(canvas, maze, camino):
    print(maze)
    for paso in camino:
        i, j = paso
        if maze[i][j] == 111:  # Si es casilla especial 111, hacer la pregunta
            pregunta_general()
        elif maze[i][j] == 3:  # Si es casilla especial 3, transportar a la 4
            i, j = encontrar_casilla(maze, 4)
        elif maze[i][j] == 4:  # Si es casilla especial 4, transportar a la 3
            i, j = encontrar_casilla(maze, 3)
        canvas.create_rectangle(j * 20, i * 20, (j + 1) * 20, (i + 1) * 20, fill="violet")
        canvas.update()
        canvas.after(200)
    return True

def encontrar_casilla(laberinto, valor):
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if laberinto[fila][columna] == valor:
                return fila, columna
    return -1, -1  # Devolver un valor predeterminado cuando la casilla no se encuentra

def main():
    root = tk.Tk()
    root.title("Laberinto")
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    mi_laberinto = crear_laberinto(20)
    laberinto_original = copy.deepcopy(mi_laberinto)

    for fila in range(len(mi_laberinto)):
        for columna in range(len(mi_laberinto[0])):
            if mi_laberinto[fila][columna] == 1:  # Pared
                canvas.create_rectangle(columna * 20, fila * 20, (columna + 1) * 20, (fila + 1) * 20, fill="black")
            elif mi_laberinto[fila][columna] == 2:  # Salida
                canvas.create_rectangle(columna * 20, fila * 20, (columna + 1) * 20, (fila + 1) * 20, fill="red")
            elif mi_laberinto[fila][columna] == 3:  # Casilla especial 1
                canvas.create_rectangle(columna * 20, fila * 20, (columna + 1) * 20, (fila + 1) * 20, fill="blue")
            elif mi_laberinto[fila][columna] == 4:  # Casilla especial 2
                canvas.create_rectangle(columna * 20, fila * 20, (columna + 1) * 20, (fila + 1) * 20, fill="blue")
            elif mi_laberinto[fila][columna] == 111:  # Casilla especial 3
                canvas.create_rectangle(columna * 20, fila * 20, (columna + 1) * 20, (fila + 1) * 20, fill="yellow")

    camino_encontrado = encontrar_camino(mi_laberinto)
    if not camino_encontrado:
        messagebox.showinfo("Laberinto", "No se puede resolver el laberinto.")
    else:
        if mostrar_laberinto(canvas, laberinto_original, camino_encontrado):
            messagebox.showinfo("Laberinto", "Laberinto resuelto correctamente.")

    root.mainloop()

main()
