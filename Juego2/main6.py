import pygame
from pygame.locals import *
from funciones import *
from menu_mejorado import *
from main2 import *
from MainSalir import *




def main6(vidas):


    WIDTH = 1200
    HEIGHT = 448

    #
    screen = pygame.display.set_mode((WIDTH, HEIGHT))


    pygame.display.set_caption("Buscando a R2D2")

    background_image = load_image('Nivel 7.jpg')
##########################################################################




#########################################################################
    #Cargo y reproduzco la cancion
    PonerMusicaRandom()
########################################################################


#######################################################################
#Ubico y pongo la pantalla
    screen.blit(background_image, (0, 0))
    pygame.display.flip()
#######################################################################



#########################################################################
    ##Bucle hasta que quedas sin vidas
    while vidas>0:
#######################################################################
#vector boobleano false false false en condiciones normales
        boolean = HizoClick()
#######################################################################



        #Si no hice click....
        if boolean.vectorBooleano[0] == 0:
            x, y = EsperarClick()
            print (x,y)
            xx = 202 ##Esto hay que cambiarlo xUbicacionWally
            yy = 391 #Esto hay que cambiarlo yUbicacionWally
            d = CalcularDistancia(x, y, xx, yy)
            vidas,respuesta = SegunDistancia(d, vidas)
            if respuesta:
                main6(vidas)
    MainFinDelJuego()




if __name__ == '__main__':
    pygame.init()
    main6()

