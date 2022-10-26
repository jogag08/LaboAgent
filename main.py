# This Python file uses the following encoding: utf-8
import sys
import pygame

from Game import Game
from Window import Window
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QSlider
from PySide6.QtCore import QTimer

def main():
    app = QApplication(sys.argv)
    game = Game()
    exe = Window(game)
    app.setActiveWindow(exe)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
