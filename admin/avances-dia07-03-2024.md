# Cambios en la Aplicación del Laberinto

## Frontend

### Cambios Realizados

- Se agregó la opción de crear el laberinto con la capacidad de ajustar la longitud del mismo. Esto brinda a los usuarios un mayor control sobre la complejidad de los laberintos generados.
  
### Problemas

- Se enfrentó un problema de importación del archivo del backend, lo que requirió agregar temporalmente funciones del backend al archivo del frontend para mantener la funcionalidad requerida. Este inconveniente afectó la integridad del código y la estructura del proyecto.

### Próximos Objetivos

- Eliminar el código del backend del archivo frontend y utilizar una importación apropiada para mejorar la organización del código y mantener una separación adecuada entre el frontend y el backend.
- Mejorar la estética de la ventana de la aplicación y optimizar la presentación visual del laberinto para una mejor experiencia del usuario.

## Backend

### Cambios Realizados

- Se implementó una función para la resolución del laberinto, lo que mejoró significativamente la capacidad de la aplicación para resolver los laberintos generados. Además, se realizaron mejoras en las funciones existentes para teletransportar y resolver acertijos, y se agregó una nueva pregunta para enriquecer la experiencia del usuario.
  
### Retos

- Se enfrentó inicialmente el desafío de dividir la matriz principal en matrices más pequeñas para encontrar el camino en el laberinto. Sin embargo, esta estrategia resultó poco práctica debido a la complejidad de conectar adecuadamente cada cuadrante. La solución adoptada fue dividir la búsqueda en pequeños cuadrantes en lugar de dividir la matriz completa, lo que simplificó el proceso de encontrar una solución adecuada para el laberinto.

### Funciones Principales

- Se creó la función `crear_laberinto` para generar el laberinto de manera aleatoria con todos los caracteres especiales.
- Se implementó la función `encontrar_camino` que toma la matriz del laberinto como argumento y encuentra el camino a través del laberinto.

### Evidencia

El código de los cambios realizados en el backend se encuentra en el enlace [aquí](enlace_git).

## Comentario del Administrador del Proyecto

Por parte del backend, cumplió con las expectativas y los objetivos dados y acordados a pesar de las dificultades y retos. Entre los dos pudimos encontrar soluciones a los problemas y así poder seguir adelante con el proyecto.

Por parte del frontend, cumplió ciertas expectativas y objetivos dados y acordados, aunque tuvo más problemas de los esperados. Estos problemas se acordaron solucionar en los próximos días ya que el día de hoy faltó apoyo brindado. Sin embargo, por mi parte como administrador, le daré más seguimiento al frontend para poder ayudarlo con posibles soluciones y así cumplir con todas las tareas acordadas.

Me siento satisfecho y un poco intrigado con lo que se ha podido resolver y poder resolver los próximos problemas ya que hoy no se pudo probar en su totalidad el juego ya que le faltan partes. Pero vamos a tener en los próximos días más pruebas del juego y su interfaz.
