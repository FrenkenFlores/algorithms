import sys
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QPen, QColor, QPolygonF
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel


class Square2(QWidget):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.draw = QPushButton('Рисовать', self)
        self.k = QLineEdit(self)
        self.n = QLineEdit(self)
        self.lbl1 = QLabel(self)
        self.lbl2 = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle('Квадрат-объектив — 2')
        self.lbl1.setFixedHeight(30)
        self.lbl1.setFixedWidth(30)
        self.lbl1.setText('K =')
        self.lbl1.move(40, 20)
        self.k.setFixedHeight(30)
        self.k.setFixedWidth(100)
        self.k.move(70, 20)

        self.lbl2.setFixedHeight(30)
        self.lbl2.setFixedWidth(30)
        self.lbl2.setText('N =')
        self.lbl2.move(180, 20)
        self.n.setFixedHeight(30)
        self.n.setFixedWidth(100)
        self.n.move(210, 20)

        self.draw.resize(150, 30)
        self.draw.move(320, 20)
        self.draw.clicked.connect(self.pp)
        self.do_paint = False
        self.color = QColor()
        self.color.setRgb(0, 0, 0)

    def pp(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(self.color)
            coords = [
                (150, 150),
                (350, 150),
                (350, 350),
                (150, 350)
            ]
            n = int(self.n.text())
            k = float(self.k.text())
            for _ in range(n):
                polygon = QPolygonF()
                for point in coords:
                    polygon.append(QPointF(point[0], point[1]))
                qp.drawPolygon(polygon)
                new_coords = []
                for i in range(len(coords)):
                    point = (
                        k * coords[i][0] + (1 - k) * coords[(i + 1) % len(coords)][0],
                        k * coords[i][1] + (1 - k) * coords[(i + 1) % len(coords)][1]
                    )
                    new_coords.append(point)
                coords = new_coords
            qp.end()
            self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square2()
    ex.show()
    sys.exit(app.exec())
