import io
import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


LAYOUT = """\
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>500</height>
   </rect>
  </property>
  <property name="mouseTracking">
   <bool>true</bool>
  </property>
  <property name="windowTitle">
   <string>Убегающая кнопка</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="mouseTracking">
    <bool>true</bool>
   </property>
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>200</y>
      <width>91</width>
      <height>41</height>
     </rect>
    </property>
    <property name="mouseTracking">
     <bool>true</bool>
    </property>
    <property name="text">
     <string>Нажми меня</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        with io.StringIO(LAYOUT) as f:
            uic.loadUi(f, self)
        self.setMouseTracking(True)
        self.w, self.h = self.width() - self.button.width(), self.height() - self.button.height()

    def mouseMoveEvent(self, event):
        x, y = event.x(), event.y()
        x0, y0 = self.button.x(), self.button.y()
        x1, y1 = x0 + self.button.width(), y0 + self.button.height()
        if x0 <= x <= x1 and y0 <= y <= y1:
            self.move_btn(x, y)

    def move_btn(self, x, y):
        correct = False
        x0, y0 = 0, 0
        w, h = self.button.width(), self.button.height()
        while not correct:
            x0, y0 = randint(0, 500 - w), randint(0, 500 - h)
            if not (x0 <= x <= x0 + w and y0 <= y <= y0 + h):
                correct = True
        self.button.move(x0, y0)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
