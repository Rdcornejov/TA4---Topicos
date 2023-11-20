import random

from globals import Global
from pade.core.agent import Agent
from PySide6.QtGui import QColor

class CarritoAgent(Agent):
    def __init__(self) -> None:
        self.x = random.randint(30, 600)
        self.y = random.randint(30, 600)
        while ((self.x > 100 and self.y > 100) and (self.x < 500 and self.y < 500)):
            self.x = random.randint(30, 600)
            self.y = random.randint(30, 600)    
        self.size = random.randint(10, 20)
        self.speed = 5 * 25 / self.size
        self.status = -1

    def updateStatus(self):
    	if self.y > 500: self.x += self.speed
    	if self.y < 100: self.x -= self.speed
    	if self.x > 500: self.y -= self.speed
    	if self.x < 100: self.y += self.speed
                
    def swim(self):
        if self.status == 1: self.x += self.speed #Que se vaya a la derecha
        elif self.status == 2: self.x -= self.speed #Que se vaya  la izquierda
        elif self.status == 3: self.y -= self.speed #Que se vaya para arriba
        elif self.status == 4: self.y += self.speed  #Que se vaya para abajo
        
    def detect_collision(self, others):
        for other in others:
            if other != self and self.is_close_to(other):
                self.avoid_collision()

    def is_close_to(self, other):
        # Define un umbral de distancia para la detección de proximidad
        distance_threshold = self.size + other.size
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return distance < distance_threshold

    def avoid_collision(self):
        # Implementa lógica para cambiar dirección, reducir velocidad, etc.
        # Por ejemplo, cambiar la dirección:
        self.x -= self.speed
        self.y -= self.speed
        swim

