
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPainter, QPixmap
from PySide6.QtWidgets import QFrame

class Gui(QFrame):
    def __init__(self, agent) -> None:
        super(Gui, self).__init__()
        self.agent = agent
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFixedSize(640, 640)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        pista = QImage("pista.png")
        painter.drawImage(0,0,pista)
        for car in self.agent.cars:
            # Cargar la imagen del pez
            car_image = QImage("car.png")
            
            # Escalar la imagen al tamaño del pez
            car_image = car_image.scaled(car.size*2, car.size)

            # Dibujar la imagen del pez en lugar del rectángulo
            painter.drawImage(car.x, car.y, car_image)