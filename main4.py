import pygame
from pygame.locals import *
from funciones import *
from MainSalir import *

from main5 import *
def main4(vidas):


###########################################################################
#PONGO FONDO PARA INICIAR JUEGO
    # Constantes
    WIDTH = 1200
    HEIGHT = 450

    #Abro la pantalla con las medidas detallas arriba
    screen = pygame.display.set_mode((WIDTH, HEIGHT))


    #Le pongo el titulo al juego
    pygame.display.set_caption("Buscando a Carl")



    #Pongo el fondo con la imagen antes cargada
    background_image = load_image('Nivel 4.jpg')
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
    ##Bucle hasta que quedas sin neuronas
    while vidas>0:
#######################################################################
#vector boobleano false false false en condiciones normales
        boolean = HizoClick()
#######################################################################



        #Si no hice click....
        if boolean.vectorBooleano[0] == 0:
            x, y = EsperarClick()
            print (x,y)
            xx = 344 ##Esto hay que cambiarlo xUbicacionWally
            yy = 111 #Esto hay que cambiarlo yUbicacionWally
            d = CalcularDistancia(x, y, xx, yy)
            vidas, respuesta = SegunDistancia(d, vidas)
            if respuesta == True:
                main5(vidas)
            if respuesta == False:
                 vidas = vidas
    MainFinDelJuego()



if __name__ == '__main__':
    pygame.init()
    main4()