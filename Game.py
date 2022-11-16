# This Python file uses the following encoding: utf-8
import pygame
import math
import random

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QTimer
from pygame import Surface

from Timer import Timer
from Agent import Agent
from Line import Line


class Game:
    __timer:Timer = Timer()
    __agent:Agent
    __line:Line
    __mousePosition:int = [400,400]
    __boardMousePosition:int = [0,0]
    __localBoardMousePosition:int = [0,0]
    __localBoardLineX2Y2Position:int = [0,0]
    __distAgentFromOrigin:int = [0,0]
    __screenColor:int = [25,65,145]
    __screenW:int = 800
    __screenH:int = 800
    __cbox:str = "Seek"
    __vecLen:float
    __rdmX:int
    __rdmX:int
    def __init__(self):
        pygame.init()
        self.timer = Timer()
        self.gameInit()
        self.__agent = Agent(100, 400, 50, 0, "Seek", "hitman.png", self.__screenW, self.__screenH)
        self.__line = Line([0,0,0], 0, 0, 0, 0, 1)
        self.shouldQuit = False

    def gameInit(self):
        self.size = self.__screenW, self.__screenH
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(self.__screenColor)

    def loop(self):
        self.__timer.update()
        self.agentMove()
        self.processInput()
        self.TEST()
        self.render()
        return self.shouldQuit

    def render(self):
        self.screen.fill(self.__screenColor)
        self.__agent.renderAgent(self.screen, self.__mousePosition[0], self.__mousePosition[1])
        self.__line.renderLine(self.screen)
        pygame.display.flip() #equivalent au render present dans SDL

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.shouldQuit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.onClick()
            #if event.type == pygame.MOUSEMOTION:
            #    self.onClick()

    def setMousePosition(self):
        self.__mousePosition = pygame.mouse.get_pos()

    def setBoardMousePosition(self, mp0, mp1):
        self.__boardMousePosition[0] = int(mp0 - (self.__screenW / 2))
        self.__boardMousePosition[1] = int((mp1 * -1) + (self.__screenH / 2))

    def setDistanceAgentFromOrigin(self):
        self.__distAgentFromOrigin[0] = self.__agent.getBoardX()
        self.__distAgentFromOrigin[1] = self.__agent.getBoardY()


    def setLocalBoardMousePosition(self):
        self.__localBoardMousePosition[0] = self.__boardMousePosition[0] - self.__distAgentFromOrigin[0]
        self.__localBoardMousePosition[1] = self.__boardMousePosition[1] - self.__distAgentFromOrigin[1]


    def setLocalLineXYPosition(self):
        self.__localBoardLineX2Y2Position[0] = self.__line.getBoardX2() - self.__distAgentFromOrigin[0]
        self.__localBoardLineX2Y2Position[1] = self.__line.getBoardY2() - self.__distAgentFromOrigin[1]
        #print('x',self.__localBoardLineX2Y2Position[0])
        #print('y',self.__localBoardLineX2Y2Position[1])


        #Le setline utilise les positions 0 à 800 de ma window
    def setLine(self, x1, y1, x2, y2, screenW, screenH):
        self.screen.fill(self.__screenColor)
        self.__line.setX1(x1)
        self.__line.setY1(y1)
        self.__line.setX2(x2)
        self.__line.setY2(y2)
        self.__line.setBoardX1(x1, screenW)
        self.__line.setBoardY1(y1, screenH)
        self.__line.setBoardX2(x2, screenW)
        self.__line.setBoardY2(y2, screenH)
        self.setLocalLineXYPosition()
        #print(self.__localBoardLineX2Y2Position)
        self.__line.setColor([255,0,0])

    def setAngle(self, x1, y1, x2, y2):
        diffX = (x2 - x1)
        diffY = (y2 - x1)
        if(diffY != 0 and diffX != 0):
            radAngle = math.atan(diffY / diffX)
            degAngle = radAngle * (180/math.pi)
            self.setAngleIn360(degAngle)

    #def setAngleIn360(self, degAngle):
    #    if (self.__localBoardMousePosition[0] > 0 and self.__localBoardMousePosition[1] > 0): #QUADRAN 1
    #        pass
    #    if (self.__localBoardMousePosition[0] > 0 and self.__localBoardMousePosition[1] < 0): #QUADRAN 2
    #        degAngle += 360
    #    if (self.__localBoardMousePosition[0] < 0 and self.__localBoardMousePosition[1] < 0): #QUADRAN 3
    #        degAngle += 180
    #    if (self.__localBoardMousePosition[0] < 0 and self.__localBoardMousePosition[1] > 0): #QUADRAN 4
    #        degAngle += 180
    #    if (degAngle == -0.0):
    #        degAngle = 180.0
    #    self.__agent.setDir(degAngle)

    def setAngleIn360(self, degAngle):
        if (self.__localBoardLineX2Y2Position[0] > 0 and self.__localBoardLineX2Y2Position[1] > 0): #QUADRAN 1
            pass
        if (self.__localBoardLineX2Y2Position[0] > 0 and self.__localBoardLineX2Y2Position[1] < 0): #QUADRAN 2
            degAngle += 360
        if (self.__localBoardLineX2Y2Position[0] < 0 and self.__localBoardLineX2Y2Position[1] < 0): #QUADRAN 3
            degAngle += 180
        if (self.__localBoardLineX2Y2Position[0] < 0 and self.__localBoardLineX2Y2Position[1] > 0): #QUADRAN 4
            degAngle += 180
        if (degAngle == -0.0):
            degAngle = 180.0
        self.__agent.setDir(degAngle)
        #print(degAngle)

    def setCbox(self, currState):
        self.__cbox = currState

    def getCbox(self):
        return self.__cbox

    def onSeek(self, x1, y1, x2, y2):
        dist:int = [0,0]
        dist[0] = x2 - x1
        dist[1] = y2 - y1
        if dist != [0,0]:
            vecDir:pygame.math.Vector2 = pygame.math.Vector2(dist)
            vecDirNorm = pygame.math.Vector2(vecDir).normalize()
            currDist = vecDir.length() - self.__vecLen
            self.__agent.seekMove(vecDir.length(), currDist, vecDirNorm, 1, 3, self.__screenW, self.__screenH, self.__timer.get_deltaTime())

    def onFlee(self, x1, y1, x2, y2):
        dist:int = [0,0]
        dist[0] = x2 - x1
        dist[1] = y2 - y1
        if dist != [0,0]:
            vecDir:pygame.math.Vector2 = pygame.math.Vector2(dist)
            vecDirNorm = pygame.math.Vector2(vecDir).normalize()
            currDist = vecDir.length() - self.__vecLen
            self.__agent.fleeMove(vecDir.length(), currDist, vecDirNorm, 1, 3, self.__screenW, self.__screenH, self.__timer.get_deltaTime())

    def onWander(self, x1, y1, x2, y2):
        dist:int = [0,0]
        dist[0] = x2 - x1
        dist[1] = y2 - y1
        if dist != [0,0]:
            vecDir:pygame.math.Vector2 = pygame.math.Vector2(dist)
            vecDirNorm = pygame.math.Vector2(vecDir).normalize()
            print(vecDir.length())
            print(self.__vecLen)
            currDist =  vecDir.length() - self.__vecLen
            self.__agent.wanderMove(vecDir.length(), currDist, vecDirNorm, 1, 3, self.__screenW, self.__screenH, self.__timer.get_deltaTime())


    def onClick(self):
        self.setMousePosition()
        self.setBoardMousePosition(self.__mousePosition[0], self.__mousePosition[1])
        #self.setDistanceAgentFromOrigin()
        self.setLocalBoardMousePosition()
        self.__agent.resetVelocity()
        self.__agent.setAccel(5)
        self.__agent.resetHasReachedDp()


    def agentMove(self):
        self.setDistanceAgentFromOrigin()
        if (self.__boardMousePosition[0] != 0) and (self.__boardMousePosition[1] != 0):
            if(self.getCbox() == "Seek"):
                self.__agent.setIsMoving(False)
                self.setVecLen(self.__agent.getBoardX(), self.__agent.getBoardY(), self.__boardMousePosition[0], self.__boardMousePosition[1])
                self.setLine(self.__agent.getX(), self.__agent.getY(), self.__mousePosition[0], self.__mousePosition[1], self.__screenW, self.__screenH)
                self.setAngle(0, 0, self.__localBoardMousePosition[0], self.__localBoardMousePosition[1])
                self.onSeek(0, 0, self.__localBoardMousePosition[0], self.__localBoardMousePosition[1])

            if(self.getCbox() == "Flee"):
                self.__agent.setIsMoving(False)
                self.setVecLen(self.__agent.getBoardX(), self.__agent.getBoardY(), self.__boardMousePosition[0], self.__boardMousePosition[1])
                self.setLine(self.__agent.getX(), self.__agent.getY(), self.__mousePosition[0], self.__mousePosition[1], self.__screenW, self.__screenH)
                self.setAngle(0, 0, self.__localBoardMousePosition[0], self.__localBoardMousePosition[1])
                self.onFlee(self.__localBoardMousePosition[0], self.__localBoardMousePosition[1],0,0)

        if(self.getCbox() == "Wander"):
            if self.__agent.getIsMoving() == False:
                self.__rdmX = random.randrange(0,800)
                self.__rdmY = random.randrange(0,800)
                self.setVecLen(self.__agent.getBoardX(), self.__agent.getBoardY(), self.__localBoardLineX2Y2Position[0], self.__localBoardLineX2Y2Position[1])
                self.setLine(self.__agent.getX(), self.__agent.getY(), self.__rdmX, self.__rdmY, self.__screenW, self.__screenH)
                self.setAngle(0, 0, self.__localBoardLineX2Y2Position[0], self.__localBoardLineX2Y2Position[1])
                self.__agent.setIsMoving(True)
            if self.__agent.getIsMoving() == True:
                #self.setVecLen(self.__agent.getBoardX(), self.__agent.getBoardY(), self.__localBoardLineX2Y2Position[0], self.__localBoardLineX2Y2Position[1])
                self.setLine(self.__agent.getX(), self.__agent.getY(), self.__rdmX, self.__rdmY, self.__screenW, self.__screenH)
                self.onWander(0, 0, self.__localBoardLineX2Y2Position[0], self.__localBoardLineX2Y2Position[1])
            #print(self.__agent.getIsMoving())




    def setVecLen(self, x1, y1, x2, y2):
        dist:int = [0,0]
        dist[0] = x2 - x1
        dist[1] = y2 - y1
        self.__vecLen = int(pygame.math.Vector2(dist).length())
        #print(pygame.math.Vector2(dist))

    #def generateNextMove(self):
    #    random.randrange(100,800)





    def TEST(self):
        #print(self.__agent.getState())
        #print(self.__mousePosition)
        #print(self.__agent.getBoardX(), self.__agent.getBoardY())
        #self.setDistanceAgentFromOrigin()
        #self.setLocalBoardMousePosition()
        pass
