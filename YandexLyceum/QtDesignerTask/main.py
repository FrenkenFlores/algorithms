import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QProgressBar, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('design.ui', self)
        self.progressBar: QProgressBar
        self.pushButton: QPushButton
        self.progressBar.setValue(0)
        self.pushButton.clicked.connect(self.increment)
        self.pushButton.setText("Increment")

    def increment(self):
        self.progressBar: QProgressBar
        current_value = self.progressBar.value()
        self.progressBar.setValue(current_value + 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())