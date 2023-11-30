import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QColor, QBrush, QPen, QPainter
from PyQt5.QtCore import Qt
import random


class Circle:
    def __init__(self, diameter, color):
        self.diameter = diameter
        self.color = color


class CirclesView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

    def add_circle(self, diameter, color):
        circle = Circle(diameter, color)
        item = self.scene.addEllipse(0, 0, diameter, diameter, QPen(Qt.NoPen), QBrush(QColor(color)))
        item.setPos(random.randint(0, 300), random.randint(0, 300))
