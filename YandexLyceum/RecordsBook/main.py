import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QListWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.MyNotes = QtWidgets.QWidget(MainWindow)
        self.MyNotes.setObjectName("MyNotes")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MyNotes)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.MyNotes)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.header_layout = QtWidgets.QHBoxLayout()
        self.header_layout.setObjectName("header_layout")
        self.input_layout = QtWidgets.QVBoxLayout()
        self.input_layout.setObjectName("input_layout")
        self.name_layout = QtWidgets.QHBoxLayout()
        self.name_layout.setObjectName("name_layout")
        self.name_label = QtWidgets.QLabel(self.widget)
        self.name_label.setObjectName("name_label")
        self.name_layout.addWidget(self.name_label)
        self.contactName = QtWidgets.QLineEdit(self.widget)
        self.contactName.setObjectName("contactName")
        self.name_layout.addWidget(self.contactName)
        self.input_layout.addLayout(self.name_layout)
        self.telephone_layout = QtWidgets.QHBoxLayout()
        self.telephone_layout.setObjectName("telephone_layout")
        self.number_label = QtWidgets.QLabel(self.widget)
        self.number_label.setObjectName("number_label")
        self.telephone_layout.addWidget(self.number_label)
        self.contactNumber = QtWidgets.QLineEdit(self.widget)
        self.contactNumber.setObjectName("contactNumber")
        self.telephone_layout.addWidget(self.contactNumber)
        self.input_layout.addLayout(self.telephone_layout)
        self.header_layout.addLayout(self.input_layout)
        self.addContactBtn = QtWidgets.QPushButton(self.widget)
        self.addContactBtn.setObjectName("addContactBtn")
        self.header_layout.addWidget(self.addContactBtn)
        self.main_layout.addLayout(self.header_layout)
        self.contactList = QtWidgets.QListWidget(self.widget)
        self.contactList.setObjectName("contactList")
        self.main_layout.addWidget(self.contactList)
        self.verticalLayout_3.addLayout(self.main_layout)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.MyNotes)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Записная книжка"))
        self.name_label.setText(_translate("MainWindow", "Имя"))
        self.number_label.setText(_translate("MainWindow", "Телефон"))
        self.addContactBtn.setText(_translate("MainWindow", "Добавить"))


class MyNotes(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyNotes, self).__init__()
        self.setupUi(self)
        self.contactName: QLineEdit
        self.contactNumber: QLineEdit
        self.addContactBtn: QPushButton
        self.contactList: QListWidget
        self.addContactBtn.clicked.connect(self.add_contact_btn_action)

    def add_contact_btn_action(self):
        self.contactList.addItem(f"{self.contactName.text()} {self.contactNumber.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyNotes()
    win.show()
    sys.exit(app.exec())
