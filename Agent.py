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
    __maxSpeed:int = 100
    __minSpeed:int = 100
    __size:int
    __state:str
    __img:str
    __velocity:pygame.math.Vector2 = pygame.math.Vector2((0,0))
    __accel:int = 5
    __decel:int = 5
    __hasReachedDp = False
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

    def resetVelocity(self):
        self.__velocity = self.__velocity * 0

    def setAccel(self, a):
        self.__accel = a

    def resetHasReachedDp(self):
        self.__hasReachedDp = False


    def setState(self, state):
        self.__state = state

    def getState(self):
        return self.__state;

    def setMaxSpeed(self, speed):
        self.__maxSpeed = speed

    def getMaxSpeed(self):
        return self.__maxSpeed

    def setMinSpeed(self, speed):
        self.__minSpeed = speed

    def getMinSpeed(self):
        return self.__minSpeed

    def setImage(self, path:str):
        self.__img = pygame.image.load(path)

    def seekMove(self, totalDist, currDist, dir, minSpeed, maxSpeed, screenW, screenH, dt):
        dir.y = -dir.y
        vecPos = pygame.math.Vector2((self.getX(), self.getY()))
        self.__velocity += dir * self.__accel * dt
        self.Lerp(self.__velocity.length(), currDist, totalDist, dir, minSpeed, maxSpeed, 80)
        vecPos += self.__velocity
        self.setX(vecPos.x)
        self.setY(vecPos.y)
        self.setBoardX(self.getX(), screenW)
        self.setBoardY(self.getY(), screenH)
        if currDist >= totalDist - 10:
           self.resetVelocity()

    def fleeMove(self, totalDist, currDist, dir, minSpeed, maxSpeed, screenW, screenH, dt):
        dir.y = -dir.y
        vecPos = pygame.math.Vector2((self.getX(), self.getY()))
        self.__velocity += dir * self.__accel * dt
        self.Lerp(self.__velocity.length(), currDist, totalDist, dir, minSpeed, maxSpeed, 80)
        vecPos += self.__velocity
        self.setX(vecPos.x)
        self.setY(vecPos.y)
        self.setBoardX(self.getX(), screenW)
        self.setBoardY(self.getY(), screenH)
        print(self.__accel)
        if totalDist - currDist >= 300:
           self.__accel = 0
           self.resetVelocity()


    def Lerp(self,currSpeed, currDist, totalDist, dir, minSpeed, maxSpeed, dP):
        decelPoint:float = (dP * totalDist) / 100
        if currSpeed >= maxSpeed:
            self.__accel = 0
        if currSpeed <= minSpeed and self.__hasReachedDp:
            self.__accel = 0
        if currDist > decelPoint and self.__hasReachedDp == False:
            self.__accel = -5
            self.__hasReachedDp = True

    #def setAccel(self, currDist, totalDist, accel, dP, minSpeed, maxSpee):
    #    decelPoint:float = (dP * totalDist) / 100
    #    if currSpeed > maxSpeed:
    #        self.__accel = 1
    #    if currDist >= decelPoint:
    #        self.__accel = -accel
    #    if currDist >= totalDist - 10:
    #       self.__accel = accel
    #    #print(currDist)
    #    #print(totalDist)






