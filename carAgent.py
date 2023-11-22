import random

from globals import Global
from pade.core.agent import Agent
from PySide6.QtGui import QColor
from pade.behaviours.protocols import TimedBehaviour

class ComportTemporal(TimedBehaviour):
    def __init__(self, agent, time):
        super(ComportTemporal, self).__init__(agent, time)
        self.agent = agent

    def on_time(self):
        super(ComportTemporal, self).on_time()
        self.agent.updateStatus()
        self.agent.swim()


class CarAgent(Agent):
    size = 1

    def __init__(self, aid, delay):
        super(CarAgent, self).__init__(aid=aid, debug=False)
        comp_temp = ComportTemporal(self, delay)
        self.behaviours.append(comp_temp)

        self.size = random.randint(10, 20)
        self.x1_limit = random.randint(30, 125 - self.size * 2)
        self.x2_limit = random.randint(514, 609 - self.size * 2)
        self.y1_limit = random.randint(30, 125 - self.size)
        self.y2_limit = random.randint(514, 609 - self.size)
        self.x = random.randint(30, 125 - self.size * 2)
        self.y = random.randint(30, 125 - self.size * 2)
        self.speed = 10 * 15 / self.size
        self.status = 2
        self.start_colision = False
        self.vivo = True

    def updateStatus(self):
        if self.y <= self.y1_limit:
            self.status = 1
            if self.x >= self.x2_limit:
                self.status = 4
        elif self.y >= self.y2_limit:
            self.status = 2
            if self.x <= self.x1_limit:
                self.status = 3
        else:
            if self.x <= self.x1_limit:
                self.status = 3
            elif self.x >= self.x2_limit:
                self.status = 4
                
    def swim(self):
        if self.status == 1: self.x += self.speed   #Que se vaya a la derecha
        elif self.status == 2: self.x -= self.speed #Que se vaya  la izquierda
        elif self.status == 3: 
            self.y -= self.speed #Que se vaya para arriba
            self.start_colision = True #Activar funcionalidad de colision
        elif self.status == 4: self.y += self.speed #Que se vaya para abajo

    def detect_collision(self, others):
        for other in others:
            if other != self and self.is_close_to(other):
                self.avoid_collision()

    def is_close_to(self, other):
        distance_threshold = self.size + other.size
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return distance < distance_threshold

    def avoid_collision(self):
        self.vivo = False