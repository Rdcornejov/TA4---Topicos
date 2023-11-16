
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
        for fish in self.agent.fish_list:
            # Cargar la imagen del pez
            fish_image = QImage("carrito.png")
            
            # Escalar la imagen al tamaño del pez
            fish_image = fish_image.scaled(fish.size*2, fish.size)

            # Dibujar la imagen del pez en lugar del rectángulo
            painter.drawImage(fish.x, fish.y, fish_image)