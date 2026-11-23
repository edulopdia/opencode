import pygame, sys
'''
Para trabajar con este script basta con cambiar en bicho la imagen que queremos cargar
He dejado los movbicho con las coordenadas que representan cada movimiento de Ken1
Basta con descomentar y comentar los movbicho correspondientes
'''

pygame.init()

ANCHO = 2500
ALTO = 2000
visor = pygame.display.set_mode((ANCHO, ALTO))

pygame.display.set_caption("Movimientos Personaje desde lista")
# Cargamos la imagen del personaje (Ken1.png)
bicho = pygame.image.load('Ken1.png').convert_alpha()

# Cargamos y escalamos los fondos al tamaño de la ventana
fondos = []
fondo1 = pygame.image.load('fondo1.png').convert()
fondo1 = pygame.transform.scale(fondo1, (ANCHO, ALTO))
fondos.append(fondo1)

fondo2 = pygame.image.load('fondo2.png').convert()
fondo2 = pygame.transform.scale(fondo2, (ANCHO, ALTO))
fondos.append(fondo2)

fondo3 = pygame.image.load('fondo3.png').convert()
fondo3 = pygame.transform.scale(fondo3, (ANCHO, ALTO))
fondos.append(fondo3)

# Índice del fondo actual (0 = fondo1, 1 = fondo2, 2 = fondo3)
fondo_actual = 0

# Colores
BLANCO = (255, 255, 255)

# Reloj
reloj = pygame.time.Clock()
FPS = 60

# Variables para el control del movimiento
fase_mov = 0          # zona de la imagen a representar en la ventana
pos = 50              # posición x de la ventana donde se mostrará al personaje
pos_y = 100           # posición y de la ventana donde se mostrará al personaje
VELOCIDAD = 4         # velocidad de desplazamiento (pixeles por frame)

# Control de velocidad de animación (para que no cambie de imagen tan rápido)
contador_animacion = 0
VELOCIDAD_ANIMACION = 8  # cambia de frame cada 8 frames del bucle (más alto = más lento)

# Coordenadas de los 4 recortes en Ken1.png (200x50 -> 4 frames de 50x50)
# [(margenizquierdo, posicion_más_alta, ancho, alto)]
recortes = ((0, 0, 50, 50), (50, 0, 50, 50), (100, 0, 50, 50), (150, 0, 50, 50))

# Tamaño al que se escala cada frame en función del tamaño de la ventana
# (para ventana de 2500 -> cada frame se dibuja a 250x250)
tam_frame = ANCHO // 10

# Escalar cada recorte para que el muñeco se vea más grande
frames = []
for recorte in recortes:
    sub = bicho.subsurface(pygame.Rect(recorte))
    escalado = pygame.transform.scale(sub, (tam_frame, tam_frame))
    frames.append(escalado)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Cambiar de fondo al pulsar la tecla C
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                if fondo_actual < len(fondos) - 1:
                    fondo_actual += 1

    teclasPulsadas = pygame.key.get_pressed()

    # Control de animación: avanza el contador cada frame
    contador_animacion += 1
    cambiar_frame = contador_animacion >= VELOCIDAD_ANIMACION
    if cambiar_frame:
        contador_animacion = 0

    # Mover a la izquierda (flecha izquierda o tecla A)
    if teclasPulsadas[pygame.K_LEFT] or teclasPulsadas[pygame.K_a]:
        pos -= VELOCIDAD
        if cambiar_frame:
            fase_mov -= 1
            if fase_mov < 0:
                fase_mov = len(frames) - 1

    # Mover a la derecha (flecha derecha o tecla D)
    if teclasPulsadas[pygame.K_RIGHT] or teclasPulsadas[pygame.K_d]:
        pos += VELOCIDAD
        if cambiar_frame:
            fase_mov += 1
            if fase_mov >= len(frames):
                fase_mov = 0

    # Mover hacia arriba (flecha arriba o tecla W)
    if teclasPulsadas[pygame.K_UP] or teclasPulsadas[pygame.K_w]:
        pos_y -= VELOCIDAD

    # Mover hacia abajo (flecha abajo o tecla S)
    if teclasPulsadas[pygame.K_DOWN] or teclasPulsadas[pygame.K_s]:
        pos_y += VELOCIDAD

    # Evitar que salga de la ventana por los lados (usando tamaño escalado real)
    ancho_frame = frames[fase_mov].get_width()
    alto_frame = frames[fase_mov].get_height()
    pos = max(0, min(pos, ANCHO - ancho_frame))
    pos_y = max(0, min(pos_y, ALTO - alto_frame))

    # Dibujar el fondo actual
    visor.blit(fondos[fondo_actual], (0, 0))

    # Dibujar el frame escalado en la posición actual
    visor.blit(frames[fase_mov], (pos, pos_y))
    pygame.display.flip()
    reloj.tick(FPS)
