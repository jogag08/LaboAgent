# This Python file uses the following encoding: utf-8

import pygame
from pygame import Surface

class Agent:
    __x:int
    __y:int
    __lx:int
    __ly:int
    __dir:int
    __size:int
    __state:str
    __img:str
    def __init__(self, x, y, size, dir, state, img, screenW, screenH):
        self.setX(x)
        self.setY(y)
        self.setLocalX(x, screenW)
        self.setLocalY(y, screenH)
        self.setDir(dir)
        self.setSize(size)
        self.setState(state)
        self.setImage(img)

    def renderAgent(self, screen:Surface):
        resizedImage = pygame.transform.scale(self.__img, (self.__size, self.__size))
        rotatedImage = pygame.transform.rotate(resizedImage, self.__dir)
        screen.blit(rotatedImage, (self.__x, self.__y))




    def setX(self, x):
        self.__x = x

    def getX(self):
        return self.__x;


    def setLocalX(self, x, screenW):
        self.__lx = int(x - (screenW / 2))
        print("x",self.__lx)

    def getLocalX(self):
        return self.__lx



    def setY(self, y):
        self.__y = y

    def getY(self):
        return self.__y;



    def setLocalY(self, y, screenH):
        self.__ly = int(y  (screenH / 2))
        print("y", self.__ly)

    def getLocalY(self):
        return self.__ly



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
