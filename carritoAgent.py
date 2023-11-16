import random

from globals import Global
from pade.core.agent import Agent
from PySide6.QtGui import QColor

class CarritoAgent(Agent):
    def __init__(self) -> None:
        self.x = random.randint(30, 100)
        self.y = random.randint(30, 100)
        self.size = random.randint(10, 20)
        self.speed = 10 * 25 / self.size
        self.status = -1

    def updateStatus(self):
        if self.y < 600 and self.y >= 500:
            if self.x >= 30 and self.x <= 100:
                self.status = 1
            if self.x < 600 and self.x >= 500:
                self.status = 3
        if self.y < 100 and self.y >= 30:
            if self.x >= 500 and self.x <= 600:
                self.status = 2
            if self.x < 100 and self.x >= 30:
                self.status = 4
                
    def swim(self):
        if self.status == 1: self.x += self.speed #Que se vaya a la derecha
        elif self.status == 2: self.x -= self.speed #Que se vaya  la izquierda
        elif self.status == 3: self.y -= self.speed #Que se vaya para arriba
        elif self.status == 4: self.y += self.speed  #Que se vaya para abajo


