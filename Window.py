# This Python file uses the following encoding: utf-8
from Game import Game
from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import QTimer

class Window(QWidget):
    timer:QTimer #timer qui s'occupe d'appeler le pygameLoop
    game:Game        #référence vers l'instance Game, la mémoire n'est pas allouée encore
    def __init__(self, game:Game):  #à la création de la window, l'instance de la game est passée en param
        super().__init__()
        self.timer = QTimer()
        self.game = game
        self.timer.timeout.connect(self.pygameLoop)
        self.timer.start(0)
        self.initUi()

    def pygameLoop(self):
        if self.game.loop():
            self.close()

    def initUi(self):
        self.setWindowTitle("Dames")
        self.setGeometry(10,50,300,200) #grandeur de l'écran

        self.button = QPushButton("Bonjour",self)
        #self.button.setToolTip("Don't you dare !")
        self.button.move(100,70)
        self.button.clicked.connect(self.onClick)
        self.show()

    def onClick(self):
        print('ca clique')
