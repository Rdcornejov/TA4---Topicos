import random

from globals import Global
from pade.core.agent import Agent
from PySide6.QtGui import QColor

class CarritoAgent(Agent):
    def __init__(self) -> None:
        self.x = random.randint(30, 100)
        self.y = random.randint(30, 100)
        self.size = 15
        self.speed = 10 * 25 / self.size
        self.status = -1

    def updateStatus(self):
        if self.y < 550:
            self.status = 4
            if self.x > 40:
                self.status = 1

        elif self.y > 550:
            self.status = 3;
            if self.x < 40 :
                self.status = 1
        else:
            if self.x < 40:
                self.status = 1
            else:
                self.status = 2

    def swim(self):
        if self.status == 1: self.x += self.speed #Que se vaya a la derecha
        elif self.status == 2: self.x -= self.speed #Que se vaya  la izquierda
        elif self.status == 3: self.y -= self.speed #Que se vaya para arriba
        elif self.status == 4: self.y += self.speed  #Que se vaya para abajo


