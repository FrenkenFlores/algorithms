import io
import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QStatusBar
from PyQt5 import uic


LAYOUT = """\
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Алфавитный указатель</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>791</width>
      <height>23</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <property name="spacing">
      <number>3</number>
     </property>
     <item>
      <widget class="QPushButton" name="btn_1">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>А</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_2">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Б</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_3">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>В</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_4">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Г</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_5">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Д</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_6">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Е</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_7">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Ё</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_8">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Ж</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_9">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>З</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_10">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>И</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_11">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Й</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_12">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>К</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_13">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Л</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_14">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>М</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_15">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Н</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_16">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>О</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_17">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>П</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_18">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Р</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_19">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>С</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_20">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Т</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_21">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>У</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_22">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Ф</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_23">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Х</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_24">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Ц</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_25">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Ч</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_26">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Ш</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_27">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Щ</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_28">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Ъ</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_29">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Ы</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_30">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Ь</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_31">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Э</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_32">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Ю</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btn_33">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>21</width>
         <height>21</height>
        </size>
       </property>
       <property name="text">
        <string>Я</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>40</y>
      <width>781</width>
      <height>511</height>
     </rect>
    </property>
    <column>
     <property name="text">
      <string>ID</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Название</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Год</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Жанр</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Продолжительность</string>
     </property>
    </column>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        with io.StringIO(LAYOUT) as f:
            uic.loadUi(f, self)
        self.buttons = [
            self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8,
            self.btn_9, self.btn_10, self.btn_11, self.btn_12, self.btn_13, self.btn_14, self.btn_15,
            self.btn_16, self.btn_17, self.btn_18, self.btn_19, self.btn_20, self.btn_21, self.btn_22,
            self.btn_23, self.btn_24, self.btn_25, self.btn_26, self.btn_27, self.btn_28, self.btn_29,
            self.btn_30, self.btn_31, self.btn_32, self.btn_33
        ]
        self.get_data()
        for btn in self.buttons:
            btn.clicked.connect(self.get_data)

    def get_data(self):
        try:
            upper_letter = self.sender().text()
        except AttributeError:
            upper_letter = 'А'
        lower_letter = upper_letter.lower()
        connection = sqlite3.connect('films_db.sqlite')
        cursor = connection.cursor()
        result = cursor.execute(f'''
        SELECT id, title, year, genre, duration FROM films
        WHERE title LIKE "{upper_letter}%" OR title LIKE "{lower_letter}%"
        ''').fetchall()
        genres = dict(cursor.execute('''
        SELECT id, title FROM genres
        ''').fetchall())
        self.tableWidget.setRowCount(len(result))
        if result:
            self.statusBar().showMessage(f'Нашлось {len(result)} записей')
            self.tableWidget.setColumnCount(len(result[0]))
        else:
            self.statusBar().showMessage(f'К сожалению, ничего не нашлось')
        for i, row in enumerate(result):
            for j, col in enumerate(row):
                if j == 3:
                    col = genres.get(col)
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
        self.tableWidget.resizeColumnsToContents()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
