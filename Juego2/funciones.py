# Módulos
import pygame
from pygame.locals import *
from math import sqrt





###########################################################################
#Pre: ESTAS USAN PY GAME
########################################################################
# Clases que referencian al estado del click
#PRE: Necesitan tener pygame importado

#POST1: Devuelve la posicion del mouse al hacer click
#POST2: Devuelve el estado de los botones del mouse
# (false,false,false) inactivo

#Gerero la clase Click
class ClickRealizadoEn():
    def __init__(self):
        pygame.mouse.get_pos.__init__(self)
        self.vectorPosicion = pygame.mouse.get_pos()



#Gerero la clase Click
class HizoClick():
    def __init__(self):
        pygame.event.get.__init__(self)
        pygame.mouse.get_pressed.__init__(self)
        pygame.event.get()
        self.vectorBooleano = pygame.mouse.get_pressed()
##########################################################################


#########################################################################
#GENERO FUNCIONES QUE USARE

########################################################################
#Cargo la imagen
def load_image(filename, transparent=False):

        try: image = pygame.image.load(filename)
        except pygame.error as message:
                raise SystemExit(message)
        image = image.convert()
        if transparent:
                color = image.get_at((0, 0))
                image.set_colorkey(color, RLEACCEL)
        return image
########################################################################

########################################################################
#Espero el click
def EsperarClick():
        sinClick = True
        while sinClick==True:
            boolean = HizoClick()
            xy = ClickRealizadoEn()
            boolean.vectorBooleano[0]
            xy.vectorPosicion
            if boolean.vectorBooleano[0] == 1:
                sinClick = False
                return xy.vectorPosicion
########################################################################

########################################################################
#Calculo la distancia

#PRE: ingreso con x e y del click, y con x e y de respuesta correcta
#POST: devuelve la distancia

def CalcularDistancia(clickX, clickY, correctaX, correctaY):
    d = sqrt((clickX - correctaX) ** 2 + (clickY - correctaY) ** 2)
    return d
########################################################################


########################################################################

def SegunDistancia(d, vidas):  #Distancia, puntos y neuronas
    respuesta = True
    if d <= 40:
        pygame.mixer.init
        pygame.mixer.music.load("Gano.wav")
        pygame.mixer.music.play()
        vidas = vidas
        respuesta = True
    if d > 40:
        pygame.mixer.music.load("You Lose.wav")
        pygame.mixer.music.play()
        vidas = vidas - 1
        respuesta= False
    return vidas, respuesta
#########################################################################



if __name__ == '__main__':
    pygame.init()




#########################################################################
def PonerMusicaRandom():
    import random
    pygame.mixer.init()
    a = []
    a.append("Audio 1.mp3")
    a.append("Audio 2.mp3")
    a.append("Audio 3.ogg")
    a.append("Audio 4.ogg")
    a.append("Audio 5.wav")
    a.append("Audio 6.wav")
    a.append("Audio 7.mp3")
    a.append("Audio 8.ogg")
    pygame.mixer.music.load(a[random.randrange(6)])
    pygame.mixer.music.play(-2)




