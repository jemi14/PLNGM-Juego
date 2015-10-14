__author__ = 'aula'

#portamos la libreria
import pygame
#iniciamos la libreria
pygame.init()

# Definir algunos colores
NEGRO  = (  0,   0,   0)
BLANCO = (255, 255, 255)
VERDE  = (0,   255,   0)
ROJO   = (255,   0,   0)
VIOLETA = (110, 46 , 179)

#Dimensiones
dimensiones = (860, 196)
#Mostramos en pantalla
pantalla = pygame.display.set_mode(dimensiones)



#Iniciamos con la finalizacion en falso
finalizado = False


reloj = pygame.time.Clock()

# -------- Bucle Principal del Programa -----------


while not finalizado:

    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario pincha sobre cerrar
            finalizado = True # Esto que indica que hemos acabado y sale de este bucle




    imagen = pygame.image.load("Imagen1.jpg")
    pantalla = pygame.display.set_mode((860,196))
    # cargamos el fondo y una imagen (se crea objetos "Surface")


    pantalla.blit(imagen,(0,0))
    pygame.display.update()


    pygame.display.flip()
    # Limita a 20 fotogramas por segundo (frames per second)
    reloj.tick(20)

pygame.quit()