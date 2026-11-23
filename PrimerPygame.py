import pygame
import sys

# Inicializar Pygame
pygame.init()

#Definir tamaño
rect_x = 0
rect_y = 0
rect_ancho = 100
rect_alto = 100

# Segundo cuadrado (azul), mismas medidas, empieza en la esquina opuesta
rect2_x = 500
rect2_y = 300

# Definir colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Configurar ventana
ANCHO_VENTANA = 800
LARGO_VENTANA = 600

VELOCIDAD = 5


ventana = pygame.display.set_mode((ANCHO_VENTANA, LARGO_VENTANA))
pygame.display.set_caption("Mi primer Juego")

reloj = pygame.time.Clock()

# Bucle principal

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teclas presionadas: flechas mueven el cuadrado rojo, WASD el azul
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        rect_x -= VELOCIDAD
    if teclas[pygame.K_RIGHT]:
        rect_x += VELOCIDAD
    if teclas[pygame.K_UP]:
        rect_y -= VELOCIDAD
    if teclas[pygame.K_DOWN]:
        rect_y += VELOCIDAD

    if teclas[pygame.K_a]:
        rect2_x -= VELOCIDAD
    if teclas[pygame.K_d]:
        rect2_x += VELOCIDAD
    if teclas[pygame.K_w]:
        rect2_y -= VELOCIDAD
    if teclas[pygame.K_s]:
        rect2_y += VELOCIDAD

    # Evitar que salgan de la ventana
    rect_x = max(0, min(rect_x, ANCHO_VENTANA - rect_ancho))
    rect_y = max(0, min(rect_y, LARGO_VENTANA - rect_alto))
    rect2_x = max(0, min(rect2_x, ANCHO_VENTANA - rect_ancho))
    rect2_y = max(0, min(rect2_y, LARGO_VENTANA - rect_alto))

    # Dibujar escena
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, ROJO, (rect_x, rect_y, rect_ancho, rect_alto))
    pygame.draw.rect(ventana, AZUL, (rect2_x, rect2_y, rect_ancho, rect_alto))
    pygame.display.flip()
    reloj.tick(60)
