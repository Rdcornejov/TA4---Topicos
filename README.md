# TA4 - Topicos

### Integrantes:
- Jefferson Espinal Atencia
- Marc Diaz Quilia
- Ronaldo Cornejo Valencia

### Profesor : 
- Luis Canaval Sánchez

### Sección: CC65

### Ciclo: 2023-02

## Definición del Problema y motivación
- Definición del Problema: Desarrollar un sistema multi agente en el que cada agente representa un carro. El sistema debe permitir que los carros interactúen entre sí sin colisionar.
- Motivación: La necesidad de simular el comportamiento de los vehículos en un entorno controlado, posiblemente para estudiar y mejorar el flujo de tráfico o para desarrollar sistemas autónomos de transporte.

### Objetivos
- Programar a los agentes para evitar colisiones.
- Permitir que los agentes conozcan la posición de los carros cercanos.
- Definir un radio de visión para cada agente, sobre el cual basarán sus decisiones de velocidad y dirección.
- Asegurarse de que los agentes se comporten como tales y no como objetos estáticos sin interacción.

### Metodología
- PADE: Es adecuada para sistemas multiagentes debido a su enfoque específico en la creación y gestión de agentes autónomos que pueden comunicarse y actuar de manera coordinada. Además, proporciona la flexibilidad necesaria para escalar el sistema y ajustar comportamientos de agentes, lo cual es crucial en la simulación de un circuito de carreras.

- QT: Esta librería nos permite crear interfaces gráficas de usuario avanzadas, lo que es esencial para visualizar la simulación del circuito de carreras. Ofrece rendimiento, portabilidad y un modelo de señales y slots para manejar eventos en tiempo real, características fundamentales para desarrollar una aplicación interactiva y multiplataforma que requiere respuestas rápidas y eficientes a las acciones de los agentes.

### Implementación

```python
import random

from globals import Global
from pade.core.agent import Agent
from PySide6.QtGui import QColor

class CarritoAgent(Agent):
    def __init__(self, aid):
        super(CarritoAgent, self).__init__(aid=aid, debug=False)
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
```

![image](https://github.com/Rdcornejov/TA4---Topicos/assets/89090023/19da0a22-5e71-4f08-ad48-c30614fd8f4c)

### Enlace de Repositorio
[https://github.com/Rdcornejov/TA4---Topicos/tree/main](https://github.com/Rdcornejov/TA4---Topicos/tree/main)
