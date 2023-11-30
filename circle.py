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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Random Circles Generator')
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.button = QPushButton('Add Circle', self)
        self.button.clicked.connect(self.add_circle)
        self.layout.addWidget(self.button)

        self.circles_view = CirclesView()
        self.layout.addWidget(self.circles_view)
