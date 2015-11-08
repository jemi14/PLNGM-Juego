# Módulos
import pygame
from pygame.locals import *
from math import sqrt

from funciones import *



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

def SegunDistancia(d, nivel):  #Distancia, puntos y neuronas
    if d <= 20:
        pygame.mixer.init
        pygame.mixer.music.load("ovacion.mp3")
        pygame.mixer.music.play()
        nivel = nivel + 1
    if d > 20:
        pygame.mixer.music.load("abucheo.mp3")
        pygame.mixer.music.play()
        nivel = nivel
    return nivel
#########################################################################



if __name__ == '__main__':
    pygame.init()




#########################################################################
def PonerMusicaRandom():
    import random
    pygame.mixer.init()
    a = []
    a.append("parajuego0.mp3")
    a.append("parajuego1.mp3")
    a.append("parajuego2.mp3")
    a.append("parajuego3.mp3")
    a.append("parajuego4.mp3")
    a.append("parajuego5.mp3")
    a.append("parajuego6.mp3")
    a.append("parajuego7.mp3")
    a.append("parajuego8.mp3")
    pygame.mixer.music.load(a[random.randrange(4)])
    pygame.mixer.music.play(-1)

