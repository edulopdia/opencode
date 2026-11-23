import pygame, sys
'''
Para trabajar con este script basta con cambiar en bicho la imagen que queremos cargar
He dejado los movbicho con las coordenadas que representan cada movimento de hombreAndando y Ken1
Basta con descomentar y comentar los movbicho correspondientes
'''

 
pygame.init()

ANCHO = 400
ALTO = 400
visor = pygame.display.set_mode((ANCHO,ALTO))
 
pygame.display.set_caption("Movimientos Personaje desde lista")
#Vamos a trabajar con imÃ¡genes. En algÃºn sitio habrÃ¡ que decirle que suba esa imagen Â¿no? 
bicho = pygame.image.load('hombreAndando.png')

fondos = [pygame.image.load('fondo1.png'),
          pygame.image.load('fondo2.png'),
          pygame.image.load('fondo3.png')]

#Colores
BLANCO = (255, 255, 255)

#Reloj
reloj = pygame.time.Clock()
FPS = 60 

#Variables para el control del movimiento 
fase_mov = 0 #zona de la imagen a representar en la ventana
pos = 50 #posiciÃ³n x de la ventana donde se mostrarÃ¡ al personaje
contador_fondo = 0


#Las listas con las coordenadas de movimiento de los diferentes personajes
#[(margenizquierdo, posicion_mÃ¡s_alta, ancho, alto )]
 
#movbicho=[(0,0,50,50), (50,0,50,50),(100,0,50,50),(150,0,50,50)] 
#movbicho esquemÃ¡tico
#movbicho=[(0,0,200,400),(400,0,200,400),(600,0,200,400),(1000,0,200,400)]
#movbicho hombre andando
movbicho = ((0,0,90,175),(100,0,90,175),(200,0,90,175),(300,0,90,175),
           (400,0,90,175),(500,0,90,175),(600,0,90,175),(700,0,90,175),
           (800,0,90,175)) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                       
            
    teclasPulsadas = pygame.key.get_pressed()
    if teclasPulsadas[pygame.K_a]:
        #AquÃ­ hay un nÃºmero mÃ¡gico. CÃ¡mbialo
        pos -= 10
        fase_mov -= 1
        if fase_mov <0: 
            fase_mov = len(movbicho) - 1          
        if pos < 0:
            pos = ANCHO    
            if contador_fondo >= 0:
                contador_fondo -= 1
    if teclasPulsadas[pygame.K_s]:
        #AquÃ­ hay un nÃºmero mÃ¡gico. CÃ¡mbialo
        pos += 10
        fase_mov += 1
        if fase_mov >= len(movbicho):
            fase_mov = 0
        if pos > ANCHO:
            pos = 0
            if contador_fondo < len(fondos) - 1:     
                contador_fondo += 1
    
    visor.blit(fondos[contador_fondo],(0,0))
    # El 100 que aparece aquÃ­ Â¿no te parece un nÃºmero mÃ¡gico? Pues a cambiar esto
    # blit es un nuevo mÃ©todo que va a permitir dibujar imÃ¡genes externas en pygame.
    #isor.blit(bicho, (pos_x, pos_y), )
    visor.blit(bicho, (pos,100), movbicho[fase_mov])
    pygame.display.flip()
    reloj.tick(FPS)
    