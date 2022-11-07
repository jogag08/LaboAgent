# This Python file uses the following encoding: utf-8
import pygame
import math

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QTimer
from pygame import Surface

from Agent import Agent
from Line import Line

class Game:
    __agent:Agent
    __line:Line
    __mousePosition:int = [0,0]
    __localMousePosition:int = [0,0]
    __screenColor:int = [25,65,145]
    __screenW:int = 800
    __screenH:int = 800
    def __init__(self):
        pygame.init()
        self.timer = Timer()
        self.gameInit()
        self.__agent = Agent(400, 400, 50, 0, "Idle", "hitman.png", self.__screenW, self.__screenH)
        self.__line = Line([0,0,0], 0, 0, 0, 0, 1)
        self.shouldQuit = False

    def gameInit(self):
        self.size = self.__screenW, self.__screenH
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(self.__screenColor)

    def loop(self):
        self.timer.update()
        dt = self.timer.get_deltaTime
        self.processInput()
        self.TEST()
        self.render()
        return self.shouldQuit

    def render(self):
        self.__agent.renderAgent(self.screen)
        self.__line.renderLine(self.screen)
        pygame.display.flip() #equivalent au render present dans SDL

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.shouldQuit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.onClick()

    def setMousePosition(self):
        self.__mousePosition = pygame.mouse.get_pos()

    def setLocalMousePosition(self, mp0, mp1):
        self.__localMousePosition[0] = int(mp0 - (self.__screenW / 2))
        self.__localMousePosition[1] = int((mp1 * -1) + (self.__screenH / 2))


    def setLine(self, x1, y1, x2, y2):
        self.screen.fill(self.__screenColor)
        agentMidX = int(x1 + (self.__agent.getSize() / 2))
        agentMidY = int(y1 + (self.__agent.getSize() / 2))
        self.__line.setX1(agentMidX)
        self.__line.setY1(agentMidY)
        self.__line.setX2(x2)
        self.__line.setY2(y2)
        self.__line.setColor([255,0,0])

    def setAngle(self, x1, y1, x2, y2):
        agentMidX = int(x1)  #agentMidX = int(x1 + (self.__agent.getSize() / 2))
        agentMidY = int(y1)  #agentMidY = int(y1 + (self.__agent.getSize() / 2))
        diffX = (x2 - agentMidX)
        diffY = (y2 - agentMidY)
        radAngle = math.atan(diffY / diffX)
        degAngle = int(radAngle * (180/math.pi))
        self.setAngleIn360(degAngle)
        #print("diffX:", diffX, "diffY", diffY)
        #print(degAngle)
        #self.__agent.setDir(degAngle)

    def setAngleIn360(self, degAngle):
        if (self.__localMousePosition[0] >= 0 and self.__localMousePosition[1] >= 0): #QUADRAN 1
            pass
        if (self.__localMousePosition[0] >= 0 and self.__localMousePosition[1] <= 0): #QUADRAN 2
            pass
        if (self.__localMousePosition[0] <= 0 and self.__localMousePosition[1] <= 0): #QUADRAN 3
            degAngle -= 180
        if (self.__localMousePosition[0] < 0 and self.__localMousePosition[1] >= 0): #QUADRAN 4
            degAngle += 180
        #print(degAngle)
        self.__agent.setDir(degAngle)



    def onClick(self):
        self.setMousePosition()
        self.setLocalMousePosition(self.__mousePosition[0], self.__mousePosition[1])
        self.setLine(self.__agent.getX(), self.__agent.getY(), self.__mousePosition[0], self.__mousePosition[1])
        self.setAngle(self.__agent.getLocalX(), self.__agent.getLocalY(), self.__localMousePosition[0], self.__localMousePosition[1])



    def TEST(self):
        #print(self.__mousePosition)
        pass


class Timer:
    _clock = None
    _dt:float = 0.016

    def __init__(self):
        self._clock = pygame.time.Clock()

    def update(self):
        self._dt = self._clock.tick(60)/1000

    def get_deltaTime(self):
        return self._dt
