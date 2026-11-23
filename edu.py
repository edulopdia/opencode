import pygame
import sys

VELOCIDAD = 5 
ANCHO_VENTANA = 800 
LARGO_VENTANA = 600
GRAVEDAD = 0.8  

# Colores
BLANCO = (255, 255, 255)  
ROJO = (255, 0, 0)   

reloj = pygame.time.Clock()

# Variables físicas con gravedad siempre presente
velocidad_1001x = 0
velocidad_y = 0
rect_x = ANCHO_VENTANA / 2 - 50
rect_y = LARGO_VENTANA / 2 - 50
rect_ancho = 100
rect_alto = 100   

ventana = pygame.display.set_mode((ANCHO_VENTANA, LARGO_VENTANA)) 
pygame.display.set_caption("Edu - Movimiento con gravedad")

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
    
    # Teclas presionadas (flechas y WASD controlan el movimiento)
    teclas = pygame.key.get_pressed()
    
    # Sumar gravedad constantemente hacia abajo siempre presente
    velocidad_y += GRAVEDAD
    
    # Mover horizontalmente: izquierda derecha independiente
    if teclas[pygame.K_LEFT]:
        velocidad_x = -VELOCIDAD
    elif teclas[pygame.K_RIGHT]:
        velocidad_x = VELOCIDAD
    
    # Mover verticalmente (sin elif, así se puede subir o bajar independientemente)
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        velocidad_y = -VELOCIDAD
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        velocidad_y = VELOCIDAD
    
    # Sumar velocidad acumulada para aplicar movimiento total
    rect_x += velocidad_x
    rect_y += velocidad_y
    
    # Rebote lateral cuando toca pared (invertir velocidad)
    if rect_x <= 0:
        velocidad_x = -velocidad_x
        rect_x = 0
    elif rect_x > ANCHO_VENTANA - rect_ancho:
        velocidad_x = -velocidad_x
        rect_x = ANCHO_VENTANA - rect_ancho
    
    if rect_y < 0:
        rect_y = 0
    elif rect_y > LARGO_VENTANA - rect_alto:
        rect_y = LARGO_VENTANA - rect_alto
    
    # Dibujar fondo blanco y cuadrado rojo
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, ROJO, (rect_x, rect_y, rect_ancho, rect_alto))
    pygame.display.flip()
    
    reloj.tick(60)
