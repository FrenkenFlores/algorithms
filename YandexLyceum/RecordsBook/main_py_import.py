import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QListWidget
from design import Ui_MainWindow


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
