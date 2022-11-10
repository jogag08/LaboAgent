# This Python file uses the following encoding: utf-8
import pygame
import math

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
    __distAgentFromOrigin:int = [0,0]
    __screenColor:int = [25,65,145]
    __screenW:int = 800
    __screenH:int = 800
    __cbox:str = "Seek"
    __vecLen:float
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


        #Le setline utilise les positions 0 à 800 de ma window
    def setLine(self, x1, y1, x2, y2):
        self.screen.fill(self.__screenColor)
        self.__line.setX1(x1)
        self.__line.setY1(y1)
        self.__line.setX2(x2)
        self.__line.setY2(y2)
        self.__line.setColor([255,0,0])

    def setAngle(self, x1, y1, x2, y2):
        diffX = (x2 - x1)
        diffY = (y2 - x1)
        if(diffY != 0 and diffX != 0):
            radAngle = math.atan(diffY / diffX)
            degAngle = radAngle * (180/math.pi)
            self.setAngleIn360(degAngle)

    def setAngleIn360(self, degAngle):
        if (self.__localBoardMousePosition[0] > 0 and self.__localBoardMousePosition[1] > 0): #QUADRAN 1
            pass
        if (self.__localBoardMousePosition[0] > 0 and self.__localBoardMousePosition[1] < 0): #QUADRAN 2
            degAngle += 360
        if (self.__localBoardMousePosition[0] < 0 and self.__localBoardMousePosition[1] < 0): #QUADRAN 3
            degAngle += 180
        if (self.__localBoardMousePosition[0] < 0 and self.__localBoardMousePosition[1] > 0): #QUADRAN 4
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
        vecDir:pygame.math.Vector2 = pygame.math.Vector2(dist)
        vecDirNorm = pygame.math.Vector2(vecDir).normalize()
        self.__agent.seekMove(vecDir.length(), vecDirNorm, self.__screenW, self.__screenH, self.__timer.get_deltaTime())

    def onClick(self):
        self.setMousePosition()
        self.setBoardMousePosition(self.__mousePosition[0], self.__mousePosition[1])
        self.setDistanceAgentFromOrigin()
        self.setLocalBoardMousePosition()

    def agentMove(self):
        self.setVecLen(self.__agent.getBoardX(), self.__agent.getBoardY(), self.__boardMousePosition[0], self.__boardMousePosition[1])
        if (self.__boardMousePosition[0] != 0) and (self.__boardMousePosition[1] != 0) and self.__vecLen > 1:
            if(self.getCbox() == "Seek"):
                self.setLine(self.__agent.getX(), self.__agent.getY(), self.__mousePosition[0], self.__mousePosition[1])
                self.setAngle(0, 0, self.__localBoardMousePosition[0], self.__localBoardMousePosition[1])
                self.onSeek(0, 0, self.__localBoardMousePosition[0], self.__localBoardMousePosition[1])

            if(self.getCbox() == "Flee"):
                pass

            if(self.getCbox() == "Wander"):
                pass

    def setVecLen(self, x1, y1, x2, y2):
        dist:int = [0,0]
        dist[0] = x2 - x1
        dist[1] = y2 - y1
        self.__vecLen = int(pygame.math.Vector2(dist).length())



    def TEST(self):
        #print(self.__mousePosition)
        #print(self.__agent.getBoardX(), self.__agent.getBoardY())
        #self.setDistanceAgentFromOrigin()
        #self.setLocalBoardMousePosition()
        pass
