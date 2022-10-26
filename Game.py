# This Python file uses the following encoding: utf-8
import pygame

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import QTimer
from pygame import Surface

class Game:
    def __init__(self):
        pygame.init()
        self.timer = Timer()
        self.gameInit()
        self.shouldQuit = False


    def gameInit(self):
        self.size = self.width, self.height = 800, 800
        black = [0,0,0]
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(black)

    def loop(self):
        self.timer.update()
        dt = self.timer.get_deltaTime
        self.processInput()
        self.render()
        return self.shouldQuit

    def render(self):
        pygame.display.flip() #equivalent au render present dans SDL

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.shouldQuit = True
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
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
