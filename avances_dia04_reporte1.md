# Avances del día 04/03/2024

## Laberinto y Teleportación

Este es un programa que genera un laberinto con características especiales y una función de teleportación. 

### Funcionalidades

- **`crear_laberinto(n)`**: Genera un laberinto de tamaño `n x n` con características especiales como casillas especiales y paredes aleatorias.
- **`teleportacion(laberinto, x, y)`**: Permite teletransportarse a otra casilla especial del laberinto.
- **`resolver_acertijo()`**: Función que solicita al jugador resolver un acertijo para avanzar.

### Detalles del Código

- El laberinto se genera con la función `crear_laberinto(n)`, donde se establece una entrada en la esquina superior izquierda y una salida en la esquina inferior derecha. También se crean casillas especiales como puntos de teletransportación y una que requiere resolver un acertijo.
- La función `teleportacion(laberinto, x, y)` permite al jugador teletransportarse a otra casilla especial diferente de la actual.
- El acertijo se resuelve con la función `resolver_acertijo()`.

### Desarrollo del Backend

El trabajo del backend fue realizado de la manera acordada en tiempo y forma, con las especificaciones dadas para el día de hoy.

#### Retos y Soluciones

Durante el desarrollo, se enfrentaron algunos retos que fueron superados con éxito:

1. **Aparición de Caracteres Especiales**: Uno de los desafíos fue asegurar que los caracteres especiales (casillas especiales) aparecieran de manera aleatoria en el laberinto. Esto se solucionó utilizando la función random para colocar estas casillas en posiciones aleatorias.

2. **Generación de Paredes y Caminos**: Otro desafío fue generar las paredes y los caminos del laberinto de manera aleatoria. Este problema se resolvió aplicando una lógica similar a la utilizada para las casillas especiales, utilizando la aleatoriedad proporcionada por la función random para decidir dónde colocar paredes y dónde dejar caminos.

Estas soluciones permitieron completar con éxito la generación del laberinto con todas sus características especiales.

## Frontend

### Generador de Laberintos con Tkinter

Este es un generador de laberintos básico utilizando la biblioteca Tkinter de Python.

#### Funcionalidades

- **`crear_laberinto()`**: Esta función ejecuta la lógica para crear el laberinto y muestra un mensaje de información con la ventana emergente de Tkinter.

#### Instrucciones de Ejecución

1. Clona este repositorio.
2. Abre el archivo `index.html` en tu navegador web para visualizar la ventana del laberinto.

#### Desarrollo del Frontend

El frontend no tuvo problemas con su parte, cumplió en tiempo y forma y con lo especificado. Está realizando mejoras visuales para hacer el juego del laberinto más interactivo y menos monótono.

## Reflexión del Equipo

Ha sido un gusto estar trabajando en equipo, ya que hemos estado aprendiendo cosas nuevas y cumpliendo las cosas que tenemos acordadas en tiempo y forma. Tenemos cosas que pulir y problemas que resolver, pero eso no nos va a detener para poder entregar el trabajo en tiempo y forma.

También es un esfuerzo que estamos haciendo para lograr que no solo el código funcione, sino que sea agradable a la vista del cliente e interactivo, para poder llegar a satisfacer las necesidades del cliente. El trabajo no es solo que funcione, sino que sea visualmente atractivo para poder seguir mejorando nuestras habilidades y el trabajo en equipo.
```
