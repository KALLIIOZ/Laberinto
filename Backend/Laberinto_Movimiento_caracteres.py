import random

def movimiento():
#El movimiento se realizara guardando la solucion del laberinto en una lista e iterando
    #sobre ella por medio de "coordenadas de la matriz"
    movimiento = []
    return 0

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
    
    return laberinto

def teleportacion(laberinto, x, y):
    # Buscamos otra casilla teletransportadora diferente de la actual
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if (i != x or j != y) and laberinto[i][j] == 3:  # Buscamos otra casilla teletransportadora
                return (i, j)  # Retornamos las coordenadas de la otra casilla teletransportadora
    # Si no encontramos otra casilla teletransportadora, retornamos la posición actual
    return (x, y)

def resolver_acertijo():
    respuesta_correcta = "respuesta correcta"
    respuesta_jugador = input("Resuelve el acertijo: ")
    if respuesta_jugador == respuesta_correcta:
        print("¡Respuesta correcta! Puedes continuar.")
        return True
    else:
        print("Respuesta incorrecta. Intenta de nuevo.")
        return False


print(crear_laberinto(6))

