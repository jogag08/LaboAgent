# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QPushButton, QComboBox
from PySide6.QtCore import QTimer

from Game import Game

class Window(QWidget):
    timer:QTimer #timer qui s'occupe d'appeler le pygameLoop
    game:Game        #référence vers l'instance Game, la mémoire n'est pas allouée encore
    comboBox:QComboBox
    state:str
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
        self.setWindowTitle("Labo Agent")
        self.setGeometry(10,50,300,200) #grandeur de l'écran
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(["Seek","Flee", "Wander"])
        self.comboBox.move(100,70)
        self.comboBox.currentIndexChanged.connect(self.onStateChange)
        self.show()

    def onStateChange(self):
        comboBox:QComboBox = self.sender()
        self.game.setCbox(comboBox.currentText())

    def setChosenState(self, state):
        self.state = state

    def getChosenState(self):
        return self.state

    def onClickSeek(self):
        self.setChosenState("Seek")

    def onClickFlee(self):
        self.setChosenState("Flee")

    def onClickWander(self):
        self.setChosenState("Wander")
