# This Python file uses the following encoding: utf-8

#SOURCE : https://www.youtube.com/watch?v=_TU6BEyBieE J'ai utilisé ce vidéo pour bien faire rotate l'agent

import pygame
from pygame import Surface

class Agent:
    __x:int
    __y:int
    __bx:int
    __by:int
    __dir:int
    __size:int
    __state:str
    __img:str
    def __init__(self, x, y, size, dir, state, img, screenW, screenH):
        self.setSize(size)
        self.setX(x)
        self.setY(y)
        self.setBoardX(x, screenW)
        self.setBoardY(y, screenH)
        self.setDir(dir)
        self.setState(state)
        self.setImage(img)

    def renderAgent(self, screen:Surface, mp0, mp1):
        resizedImage = pygame.transform.scale(self.__img, (self.__size, self.__size))
        rotatedImage = pygame.transform.rotate(resizedImage, self.__dir)
        #cellRect = pygame.Rect(self.__x, self.__y, self.__size, self.__size)
        #pygame.draw.rect(screen, [255,255,255], cellRect)
        #screen.blit(rotatedImage, (self.__x, self.__y))
        screen.blit(rotatedImage, (self.__x - int(rotatedImage.get_width() / 2), self.__y - int(rotatedImage.get_height() / 2)))




    def setX(self, x):
        self.__x = x

    def getX(self):
        return self.__x


    def setBoardX(self, x, screenW):
        self.__bx = int(x - (screenW / 2))

    def getBoardX(self):
        return self.__bx



    def setY(self, y):
        self.__y = y

    def getY(self):
        return self.__y;



    def setBoardY(self, y, screenH):
        self.__by = int((y * -1) + (screenH / 2))

    def getBoardY(self):
        return self.__by



    def setDir(self, dir):
        self.__dir = dir

    def getDir(self):
        return self.__dir;



    def setSize(self, size):
        self.__size = size

    def getSize(self):
        return self.__size



    def setState(self, state):
        self.__state = state

    def getState(self):
        return self.__state;


    def setImage(self, path:str):
        self.__img = pygame.image.load(path)

    def seekMove(self, dir, screenW, screenH):
        self.setX(self.getX() + dir)
        self.setY(self.getY() + dir)
        self.setBoardX(self.getX(), screenW)
        self.setBoardY(self.getY(), screenH)
        pass



