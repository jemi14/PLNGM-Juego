import pygame
from pygame.locals import *
from funciones import *


def main():


###########################################################################
#PONGO FONDO PARA INICIAR JUEGO
    # Constantes
    WIDTH = 1083
    HEIGHT = 448

    #Abro la pantalla con las medidas detallas arriba
    screen = pygame.display.set_mode((WIDTH, HEIGHT))


    #Le pongo el titulo al juego
    pygame.display.set_caption("Encuentra al personaje")



    #Pongo el fondo con la imagen antes cargada

##########################################################################




#########################################################################
    #Cargo y reproduzco la cancion
    PonerMusicaRandom()
########################################################################


#######################################################################
#Ubico y pongo la pantalla

#######################################################################



#########################################################################
    ##Bucle hasta que quedas sin neuronas
    nivel = 5
    while nivel>0 & nivel < 7:
#######################################################################
#vector boobleano false false false en condiciones normales
        boolean = HizoClick()
#######################################################################


            #Si no hice click....
        if boolean.vectorBooleano[0] == 0:
            if nivel == 5:

                background_image = load_image('1200-448.png')
                screen.blit(background_image, (0, 0))
                pygame.display.flip()
                x, y = EsperarClick()
                print (x,y)
                xx = 329 ##Esto hay que cambiarlo xUbicacionWally
                yy = 333 #Esto hay que cambiarlo yUbicacionWally
                d = CalcularDistancia(x, y, xx, yy)
                nivel = SegunDistancia(d, nivel)




            if nivel == 6:

                #Si no hice click....
                if boolean.vectorBooleano[0] == 0:
                    background_image = load_image('2.png')
                    screen.blit(background_image, (0, 0))
                    pygame.display.flip()
                    x, y = EsperarClick()
                    print (x,y)
                    xx = 673 ##Esto hay que cambiarlo xUbicacionWally
                    yy = 235 #Esto hay que cambiarlo yUbicacionWally
                    d = CalcularDistancia(x, y, xx, yy)
                    nivel = SegunDistancia(d, nivel)




            if nivel == 7:
                print("\nGracias por jugar!!!")
                finalizar = False
                while not finalizar:
                    # --- Bucle principal de eventos
                    for evento in pygame.event.get(): #Indicamos que el usuario hizo algo
                        if evento.type == pygame.QUIT: #Si el usuario sale..
                            finalizar = True #indica que hemos acabado y salimos del bucle

                pygame.quit()


if __name__ == '__main__':

    main()

