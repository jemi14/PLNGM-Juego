__author__ = 'Mean Girls'

#1- Importamos pygame
import pygame

#Declaramos pi para poder utilizarlo las adelante
PI = 3.141592653

#Inicializamos TODOS los modulos de python
pygame.init()

#Definimos los colores que utiliza el modelo
#Van en mayuscula por ser variables globales
NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
VERDE  = (0,   255,   0)
ROJO   = (255,   0,   0)
VIOLETA = (77,  33, 105)
CIELO   =(0,    255,255)
NUBE    = (255, 255,255)
SOL =      (255,  255,0)
FONDO =    (255,    176,38)
#http://www.colorpicker.com/

# Establecemos el largo y alto de la pantalla
largo_pantalla = 700
alto_pantalla = 448
#Define las dimensiones de la pantalla del juego
pantalla = pygame.display.set_mode([largo_pantalla, alto_pantalla])

#Definimos el titulo de la ventana
pygame.display.set_caption("Fantasmita")

#Para poder crear un bucle
finalizar = False

#Para establecer la rapidez en la actualizacion de la pantalla
reloj = pygame.time.Clock()
#Cargamos la imagen del fantasmita

personaje = pygame.image.load("fantasmita.png")
personaje.set_colorkey(BLANCO)
personajex, personajey = (-60,250)
# -------- Bucle principal de fantasmita -----------
while not finalizar:
    # --- Bucle principal de eventos
    for evento in pygame.event.get(): #Indicamos que el usuario hizo algo
        if evento.type == pygame.QUIT: #Si el usuario sale..
            finalizar = True #indica que hemos acabado y salimos del bucle



    #Obtiene la posicion actual del raton, devolviendola como una lista con dos numeros.
    #personajex, personajey = pygame.mouse.get_pos()


    # Realiza los movimientos del personaje con teclado
    teclas = pygame.key.get_pressed()
    #posicion_del_personaje = pygame.mouse.get_pos()

    if teclas[pygame.K_LEFT]:
        personajex -= 4
    elif teclas[pygame.K_RIGHT]:
        personajex += 4

    if teclas[pygame.K_DOWN]:
        personajey += 3
    elif teclas[pygame.K_UP]:
        personajey -= 3


        # Copia la imagen en pantalla:


    #Link con las cosas que podemos dibujar
    pantalla.fill(CIELO)
    pygame.draw.line(pantalla, VERDE, [5,445], [700,445], 10)
    pygame.draw.circle(pantalla,SOL,(700,100),120,0)
    #agregar elementos
    pantalla.blit(personaje, [personajex, personajey])

    # --- Avanzamos y actualizamos la pantalla con lo que dibujamos
    pygame.display.flip()

    #Configuramos los fotogramas
    FPS = 60
    frecuencia=pygame.time.Clock()

#Cerramos la ventana y salimos de fantasmita
pygame.quit()
