import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt6.QtGui import QPixmap, QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog
from main import Map

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.map = Map('москва', '0.1')
        self.my_bytes = None
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 900, 600)
        self.setWindowTitle('API_MAP')
        QL = QLineEdit('50, 50', self)
        QL.resize(100, 30)
        QL.move(725, 300)
        Coordinates = QL.text()

        but = QPushButton('Найти', self)
        but.resize(100, 40)
        but.move(725, 100)
        but.clicked.connect(lambda: self.change_map(Coordinates))
        qp = QPixmap()
        if self.my_bytes:
            qp.loadFromData(self.my_bytes)
        labelImage = QLabel(self)
        labelImage.setPixmap(qp)
        labelImage.move(50, 50)
        labelImage.show()

    def change_map(self, text):
        print('sss')
        self.map.change_location(text)
        self.my_bytes = self.map.update_map()
        print(self.my_bytes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
