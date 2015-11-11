import pygame
from pygame.locals import *
from funciones import *
from main import *
from main2 import *
from MainSalir import *




##############################################################################
def MainFinDelJuego():

###########################################################################
#PONGO FONDO PARA INICIAR JUEGO
    # Constantes
    WIDTH = 815
    HEIGHT = 510

    #Abro la pantalla con las medidas detallas arriba
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    #Pongo el fondo con la imagen antes cargada
    background_image = load_image('finDelJuego.jpg')
##########################################################################


#######################################################################
#Ubico y pongo la pantalla
    screen.blit(background_image, (0, 0))
    pygame.display.flip()
#######################################################################

    tiempo = 0
    while tiempo <= 1999000:
        tiempo = tiempo + 0.4
    salir_del_programa()




if __name__ == '__main__':
    pygame.init()
    MainFinDelJuego()