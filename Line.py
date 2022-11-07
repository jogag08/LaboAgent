# This Python file uses the following encoding: utf-8

import pygame
from pygame import Surface

class Line:
    __x1:int
    __y1:int
    __x2:int
    __y2:int
    __color:int = []
    __width:int
    def __init__(self, color, x1, y1, x2, y2, width):
        self.setColor(color)
        self.setX1(x1)
        self.setY1(y1)
        self.setX2(x2)
        self.setY2(y2)
        self.setWidth(width)

    def renderLine(self, screen:Surface):
        if((self.__x1 != self.__x2) or (self.__y1 != self.__y2)):
            pygame.draw.line(screen, self.__color, (self.__x1, self.__y1), (self.__x2, self.__y2))



    def setX1(self, x1):
        self.__x1 = x1

    def getX1(self):
        return self.__x1;

    def setY1(self, y1):
        self.__y1 = y1

    def getY1(self):
        return self.__y1;



    def setX2(self, x2):
        self.__x2 = x2

    def getX2(self):
        return self.__x2;

    def setY2(self, y2):
        self.__y2 = y2

    def getY2(self):
        return self.__y2;

    def setColor(self, color):
        self.__color = color

    def setWidth(self, width):
        self.__width = width


